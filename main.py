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
        # PyGame events
        pg.event.set_grab(True)
        pg.mouse.set_visible(False)
        # Detect context with pygame
        self.ctx = mgl.create_context()
        # Create clock
        self.clock = pg.time.Clock()
        self.time = 0
        self.delta_time = 0
        # Command handler
        self.command = CommandHandler(self)
        # Flags
        self.projection_type = 1
        self.rotation_flag = 0
        self.figure_color_flag = 0
        self.figure_loaded = 0
        # Counters
        self.time_counter = 0
        # Strings
        self.command_parsed = "cuboid 0 0 0 0 1 0 2 2 2"
        self.command_read = "cuboid 0 0 0 0 1 0 2 2 2"
        self.cached_vertex = ""
        self.file_name = ""
        self.command_parsed = self.command.split_command(self.command_parsed)
        # Variables
        self.figure_color = glm.vec3(1, 0, 0)
        self.camera_near = 0.1
        self.camera_far = 100
        # Camera
        self.camera = Camera(self, self.projection_type, self.camera_near, self.camera_far)
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

            elif event.type == pg.KEYDOWN and event.key == pg.K_t:
                command_unparsed = input("\n<figure type> <origin coordinates> <rotation> <dimensions>  \n")
                self.command_read = self.command.command_handler(command_unparsed)
                if self.command_read[0] != "-":
                    self.figure_loaded = 0
                    self.command_parsed = self.command_read
                self.camera = Camera(self, self.projection_type, self.camera_near, self.camera_far)
                self.scene = Figure(self)

            elif event.type == pg.KEYDOWN and event.key == pg.K_u:
                self.camera = Camera(self, self.projection_type, self.camera_near, self.camera_far)
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
            self.camera.update()
            self.render()
            self.clock.tick(60)
            self.delta_time = self.clock.tick(60)

    def keydown_selection(self):

        self.scene.destroy()
        self.scene = Figure(self)

        self.command_parsed[4] = "0"
        self.command_parsed[5] = "1"
        self.command_parsed[6] = "0"


if __name__ == '__main__':
    app = GraphicsEngine()
    app.run()
