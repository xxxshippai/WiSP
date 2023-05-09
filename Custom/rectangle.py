from OpenGL.GLUT import *
from OpenGL.GL import *

from Custom.line import line

class rectangle:
  vertices = []

  def __init__(self,x,y,z,a,b):      
    self.vertices = [
      (x,y,z), 
      (x+a,y,z),
      (x+a,y+b,z),
      (x,y+b,z),
    ]

  def __init__(self, v1,v2,v3,v4):
    self.vertices = [v1,v2,v3,v4]

  def draw(self, color):
    glColor3f(*color)
    glBegin(GL_QUADS)
    for i in range(4):
      glVertex3f(*self.vertices[i])
    glEnd()