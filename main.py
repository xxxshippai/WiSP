import pygame as pg
import moderngl as mgl
import sys
from model import *
from camera import Camera


class GraphicsEngine:
    def __init__(self, win_size=(1600, 900)):
        pg.init()
        self.WIN_SIZE = win_size
        # Assigning OpenGL version 3.3, setting flag not to use deprecated version
        pg.display.gl_set_attribute(pg.GL_CONTEXT_MAJOR_VERSION, 3)
        pg.display.gl_set_attribute(pg.GL_CONTEXT_MINOR_VERSION, 3)
        pg.display.gl_set_attribute(pg.GL_CONTEXT_PROFILE_MASK, pg.GL_CONTEXT_PROFILE_CORE)
        # Create context
        pg.display.set_mode(self.WIN_SIZE, flags=pg.OPENGL | pg.DOUBLEBUF)
        # Detect context with pygame
        self.ctx = mgl.create_context()
        # Create clock
        self.clock = pg.time.Clock()
        self.time = 0
        self.rotation_flag = 1
        self.time_counter = 0
        self.figure_type = 1
        self.direction_x = 1
        self.direction_y = 1
        # Camera
        self.camera = Camera(self)
        # Scene
        self.scene = Figure(self)

    def check_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
                self.scene.destroy()
                pg.quit()
                sys.exit()

            elif event.type == pg.KEYDOWN and event.key == pg.K_r:
                self.rotation_flag = not self.rotation_flag

            elif event.type == pg.KEYDOWN and event.key == pg.K_1:
                self.scene.destroy()
                self.figure_type = 1
                self.scene = Figure(self)

            elif event.type == pg.KEYDOWN and event.key == pg.K_2:
                self.scene.destroy()
                self.figure_type = 2
                self.scene = Figure(self)

            elif event.type == pg.KEYDOWN and event.key == pg.K_3:
                self.scene.destroy()
                self.figure_type = 3
                self.scene = Figure(self)

            elif event.type == pg.KEYDOWN and event.key == pg.K_4:
                self.scene.destroy()
                self.figure_type = 4
                self.scene = Figure(self)

            elif event.type == pg.KEYDOWN and event.key == pg.K_d:
                self.scene.destroy()
                self.figure_type = 0

            elif event.type == pg.KEYDOWN and event.key == pg.K_RIGHT:
                self.direction_y = 1

            elif event.type == pg.KEYDOWN and event.key == pg.K_LEFT:
                self.direction_y = -1

            elif event.type == pg.KEYDOWN and event.key == pg.K_UP:
                self.direction_x = 1

            elif event.type == pg.KEYDOWN and event.key == pg.K_DOWN:
                self.direction_x = -1

            elif event.type == pg.KEYDOWN and event.key == pg.K_c:
                self.direction_x = 0
                self.direction_y = 1


    def render(self):
        # Clearing frame buffer
        self.ctx.clear(color=(0.1, 0.1, 0.1))
        # Render scene
        self.scene.render()
        # Swapping buffers
        pg.display.flip()

    def get_time(self):
        if self.rotation_flag == 1:
            self.time_counter = self.time_counter + 0.01

    def run(self):
        while True:
            self.get_time()
            self.check_events()
            self.render()
            self.clock.tick(60)


if __name__ == '__main__':
    app = GraphicsEngine()
    app.run()
