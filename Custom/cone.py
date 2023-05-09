from OpenGL.GLUT import *
from OpenGL.GL import *
import numpy as np

from Custom.triangle import triangle
from Custom.circle import circle

class cone:
  x,y,z,r,h,approximation=0,0,0,0,0,0
  vertices = []

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
      self.vertices.append(((x+r) * np.cos(angle), y+0, (z+r) * np.sin(angle)))
      angle+=angleIncrement

  def draw(self, color):
    circle.draw_explicit(vertices=self.vertices,color=color, draw_lines=True)
    glColor3f(*color)
    glBegin(GL_TRIANGLE_FAN)
    glVertex3f(self.x,self.y+self.h,self.z)
    for v in self.vertices:
      glVertex3f(*v)
    glEnd()