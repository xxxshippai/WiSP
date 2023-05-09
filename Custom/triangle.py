from OpenGL.GLUT import *
from OpenGL.GL import *
import numpy as np
from Custom.line import line

class triangle:
  vertices = []

  def __init__(self,x,y,z,a):      
    r = a / (2 * np.sin(a / 2))
    self.vertices = [
      (x+r, y+r, z+0.),
      ((x+r) * np.cos(120), (y+r) * np.sin(120), z+0.),
      ((x+r) * np.cos(240), (y+r) * np.sin(240), z+0.),
    ]

  def __init__(self, v1,v2,v3):
    self.vertices = [v1,v2,v3]

  def draw(self, color):
    glColor3f(*color)
    glBegin(GL_TRIANGLES)
    for i in range(3):
      glVertex3f(*self.vertices[i])
    glEnd()