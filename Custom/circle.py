from OpenGL.GLUT import *
from OpenGL.GL import *
import numpy as np
from Custom.line import line

class circle:
  vertices = []

  def __init__(self,x,y,z,r,approximation=40):
    angleIncrement = 360. / approximation
    angleIncrement *= np.pi / 180.

    angle = 0.

    for _ in range(approximation):
      self.vertices.append((x+r * np.cos(angle), y+r * np.sin(angle), z))
      angle += angleIncrement


  @staticmethod
  def draw_explicit(vertices, color, draw_lines):
    glColor3f(*color)
    glBegin(GL_TRIANGLE_FAN)
    for v in vertices:
      glVertex3f(*v)
    glEnd()
    if draw_lines:
      line(*vertices).draw((1,1,1))

  def draw(self, color, draw_lines=True):
    circle.draw_explicit(self.vertices, color, draw_lines)