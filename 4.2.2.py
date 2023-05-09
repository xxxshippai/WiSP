from OpenGL.GLUT import *
from OpenGL.GL import *
import numpy as np

from Custom.pyramid import pyramid

d = float(input("Please provide d: "))
h = float(input("Please provide h: "))
average = (h+d)/2
def show():
  glClearColor(0, 0, 0, 1)
  glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
  glViewport(0, 0, 640, 480)
  glMatrixMode(GL_PROJECTION)
  glLoadIdentity()
  # Program 05a
  #glFrustum(-2, 2, -2, 2, 1, 10)
  # Program 05b
  glOrtho(-2, 2, -2, 2, 1, 10)
  glMatrixMode(GL_MODELVIEW)
  glLoadIdentity()
  glPushMatrix()
  glTranslate(0, -1, -3)
  glRotate(35, 0, 1, 1)
  pyramid(0,0,0,d,h).draw((1,1,0))
  glPopMatrix()
  #glTranslate(-1 ,2, -3)
  #pyramid(0,0,0,d,h).draw((1,1,0))
  #glTranslate(-3 ,2, -3)
  #pyramid(0,0,0,d,h).draw((1,1,0))
  glutSwapBuffers()

glutInit()
glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE)
glutInitWindowSize(640, 480)
glutInitWindowPosition(100, 100)
glutCreateWindow("L4.2.2")
glClearColor(1.0, 1.0, 1.0, 1.0)
glutDisplayFunc(show)
glutMainLoop()

