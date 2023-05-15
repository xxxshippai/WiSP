import pygame as pg
import moderngl as mgl
import sys
import numpy as np
import glm
from model import *
from camera import Camera
from command import CommandHandler


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
        # Command handler
        self.command = CommandHandler(self)
        self.rotation_flag = 0
        self.time_counter = 0
        self.figure_type = 0
        self.override_flag = 0
        self.command_parsed = "sphere 0 0 0 0 1 0 2 10"
        self.command_read = "sphere 0 0 0 0 1 0 2 10"
        self.figure_color_flag = 0
        self.figure_color = glm.vec3(1, 0, 0)
        self.command_parsed = self.command.split_command(self.command_parsed)
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
                self.override_flag = 1
                self.figure_type = 1
                self.keydown_selection()

            elif event.type == pg.KEYDOWN and event.key == pg.K_2:
                self.override_flag = 1
                self.figure_type = 2
                self.keydown_selection()

            elif event.type == pg.KEYDOWN and event.key == pg.K_3:
                self.override_flag = 1
                self.figure_type = 3
                self.keydown_selection()

            elif event.type == pg.KEYDOWN and event.key == pg.K_4:
                self.override_flag = 1
                self.figure_type = 4
                self.keydown_selection()

            elif event.type == pg.KEYDOWN and event.key == pg.K_t:
                command_unparsed = input("\n<figure type> <origin coordinates> <rotation> <dimensions>  \n")
                self.command_read = self.command.command_handler(command_unparsed)
                if self.command_read[0] != "-":
                    self.command_parsed = self.command_read
                if self.figure_color_flag == 1:
                    self.figure_color = glm.vec3(float(self.command_read[2]),
                                                 float(self.command_read[3]),
                                                 float(self.command_read[4]))
                    self.figure_color_flag = 0
                self.override_flag = 0
                self.scene = Figure(self)

            elif event.type == pg.KEYDOWN and event.key == pg.K_u:
                self.scene = Figure(self)

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

    def keydown_selection(self):

        self.scene.destroy()
        self.scene = Figure(self)

        self.command_parsed[4] = "0"
        self.command_parsed[5] = "1"
        self.command_parsed[6] = "0"


if __name__ == '__main__':
    app = GraphicsEngine()
    app.run()
