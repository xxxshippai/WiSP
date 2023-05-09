from OpenGL.GLUT import *
from OpenGL.GL import *
import numpy as np

from Custom.rectangle import rectangle
from Custom.line import line

class cube:
  vertices, walls = [],[] 

  def __init__(self,x,y,z,a,b,c):      
    self.vertices = np.array([
      # A,B,D,C,E,F,H,G
      (x - (1 / 2) * a, y - (1 / 2) * b, z - (1 / 2) * c),
      (x + (1 / 2) * a, y - (1 / 2) * b, z - (1 / 2) * c),
      (x + (1 / 2) * a, y + (1 / 2) * b, z - (1 / 2) * c),
      (x - (1 / 2) * a, y + (1 / 2) * b, z - (1 / 2) * c),
      (x - (1 / 2) * a, y - (1 / 2) * b, z + (1 / 2) * c),
      (x + (1 / 2) * a, y - (1 / 2) * b, z + (1 / 2) * c),
      (x + (1 / 2) * a, y + (1 / 2) * b, z + (1 / 2) * c),
      (x - (1 / 2) * a, y + (1 / 2) * b, z + (1 / 2) * c)
    ])

    self.walls = [
      self.vertices[[0,1,2,3]],
      self.vertices[[1,5,6,2]],
      self.vertices[[2,6,7,3]],
      self.vertices[[0,4,7,3]],
      self.vertices[[0,1,5,4]],
      self.vertices[[4,5,6,7]]
    ]

  def draw(self, color):
    for wall in self.walls:
      line(*wall).draw((1,1,1))
    for wall in self.walls:
      rectangle(*wall).draw(color)