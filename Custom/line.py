from OpenGL.GLUT import *
from OpenGL.GL import *

class line:
  vertices = []

  def __init__(self, *vertices):      
    self.vertices = vertices

  def draw(self, color):
    glColor3f(*color)
    glBegin(GL_LINE_LOOP)
    for v in self.vertices:
      glVertex3f(*v)
    glEnd()