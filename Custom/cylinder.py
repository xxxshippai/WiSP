from OpenGL.GLUT import *
from OpenGL.GL import *
import numpy as np

from Custom.rectangle import rectangle
from Custom.circle import circle

class cylinder:
  x,y,z,r,h,approximation=0,0,0,0,0,0
  # walls = []
  top_vertices = []
  bottom_vertices = []
  def __init__(self,x,y,z,r,h, approximation=40):
    self.x=x
    self.y=y
    self.z=z
    self.r=r
    self.h=h
    self.approximation=approximation
    
    angleIncrement = 360. / approximation
    angleIncrement *= np.pi / 180.

    angle = 0.

    for _ in range(approximation):
      self.bottom_vertices.append(((x+r) * np.cos(angle), y+0, (z+r) * np.sin(angle)))
      self.top_vertices.append(((x+r) * np.cos(angle), y+h, (z+r) * np.sin(angle)))
      # self.walls.append((
      #   ((x+r) * np.cos(angle), (y+r) * np.sin(angle), z+0),
      #   ((x+r) * np.cos(angle), (y+r) * np.sin(angle), z+h),
      #   ((x+r) * np.cos(angle+angleIncrement), (y+r) * np.sin(angle+angleIncrement), z+h),
      #   ((x+r) * np.cos(angle+angleIncrement), (y+r) * np.sin(angle+angleIncrement), z+0)))
      angle+=angleIncrement

  def draw(self, color):
    circle.draw_explicit(self.top_vertices, color, True)
    circle.draw_explicit(self.bottom_vertices, color, True)
    glColor3f(*color)
    glBegin(GL_TRIANGLE_STRIP)
    for v,v2 in zip(self.top_vertices,self.bottom_vertices):
      glVertex3f(*v)
      glVertex3f(*v2)
    glVertex3f(*self.top_vertices[0])
    glEnd()