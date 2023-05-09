from OpenGL.GLUT import *
from OpenGL.GL import *
import numpy as np
import math


#User input for length and number of sides for polygon
sideNumber = int(input("Input number of sides for polygon: "))
sideLength = float(input("Input length of each side for polygon: "))


def show():
    angle = 2 * math.pi / sideNumber

    glBegin(GL_POLYGON)
    glColor3f(1.0, 1.0, 0.0)

    for i in range(sideNumber):
        x = sideLength * math.cos(i * angle)
        y = sideLength * math.sin(i * angle)
        glVertex2f(x, y)

    glEnd()
    glutSwapBuffers()

glutInit()
glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE)
glutInitWindowSize(800, 800)
glutInitWindowPosition(100, 100)
glutCreateWindow("L4.1")
glClearColor(1.0, 1.0, 1.0, 1.0)
glutDisplayFunc(show)
glutMainLoop()