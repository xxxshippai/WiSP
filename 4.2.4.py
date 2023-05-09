from OpenGL.GLUT import *
from OpenGL.GL import *
import numpy as np

from Custom.cone import cone

h = float(input("Please provide h: "))
r = float(input("Please provide r: "))

n=30 # circle approximation

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
  glTranslate(0, 0, -3)
  glRotate(185, 1, 0, 0)
  cone(0,0,0,r,h,n).draw((1,1,0))
  glPopMatrix()
  #glTranslate(-1 ,2, -3)
  #cone(0,0,0,r,h,n).draw((1,1,0))
  glutSwapBuffers()

glutInit()
glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE)
glutInitWindowSize(640, 480)
glutInitWindowPosition(100, 100)
glutCreateWindow("L4.2.4")
glClearColor(1.0, 1.0, 1.0, 1.0)
glutDisplayFunc(show)
glutMainLoop()

