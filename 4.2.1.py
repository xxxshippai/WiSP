from OpenGL.GLUT import *
from OpenGL.GL import *
import numpy as np

from Custom.cube import cube

a = int(input("a: "))
b = int(input("b: "))
c = int(input("c: "))

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
  glTranslate(0, 0, -2)
  glRotate(90, 0, 1, 1)
  cube(0,0,0,a,b,c,).draw((1,1,0))
  glPopMatrix()
  #glTranslate(-1 ,2, -3)
  #cube(0,0,0,a,b,c,).draw((1,1,0))
  #glTranslate(-3 ,2, -3)
  #cube(0,0,0,a,b,c,).draw((1,1,0))
  glutSwapBuffers()

glutInit()
glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_DEPTH)
glutInitWindowSize(640, 640)
glutInitWindowPosition(100, 100)
glutCreateWindow("L4.2.1")
glClearColor(1.0, 1.0, 1.0, 1.0)
glEnable(GL_DEPTH_TEST)
glDepthFunc(GL_LESS)
glutDisplayFunc(show)
glutMainLoop()