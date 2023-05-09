from OpenGL.GLUT import *
from OpenGL.GL import *
import numpy as np

from Custom.triangle import triangle
from Custom.line import line

class pyramid:
  vertices, walls = [],[] 

  def __init__(self,x,y,z,a,h):      
    r = a / (2 * np.sin(a / 2))
    self.vertices = np.array([
      (x+r, y+r, z+0.),
      ((x+r) * np.cos(120), (y+r) * np.sin(120), z+0.),
      ((x+r) * np.cos(240), (y+r) * np.sin(240), z+0.),
      (x+r, y+r + a * np.sqrt(3)/2, z+h),
    ])

    self.walls = [
      self.vertices[[0,1,2]],
      self.vertices[[0,1,3]],
      self.vertices[[1,3,2]],
      self.vertices[[2,0,3]]
    ]

  def draw(self, color):
    for wall in self.walls:
      line(*wall).draw((1,1,1))
    for wall in self.walls:
      triangle(*wall).draw(color)