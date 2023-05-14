import shlex
import numpy as np


class CommandHandler:

    def __init__(self, app):
        self.app = app

    def split_command(self, command_string):
        command_parsed = shlex.split(command_string)
        return list(command_parsed)

    def command_handler(self, command_string):
        command_parsed = self.split_command(command_string)
        command_float = [.0, .0, .0]

        # Command structure
        # --(action type)-- (figure type) (origin coordinates) (rotation) (user dimensions)
        # Command list
        # -rotate -move
        # -cuboid -pyramid -cylinder -cone
        # x y z
        # x y z
        # dependent on figure, a b c, a h, r h
        if command_parsed[0] == "-":
            if command_parsed[1] == "rotate":
                if command_parsed[2] == "moving":
                    self.app.command_parsed[4] = command_parsed[3]
                    self.app.command_parsed[5] = command_parsed[4]
                    self.app.command_parsed[6] = command_parsed[5]
                    self.app.rotation_flag = 1
                elif command_parsed[2] == "static":
                    if command_parsed[3] == "add":
                        command_float[0] = float(self.app.command_parsed[4]) + float(command_parsed[4])
                        command_float[1] = float(self.app.command_parsed[5]) + float(command_parsed[5])
                        command_float[2] = float(self.app.command_parsed[6]) + float(command_parsed[6])
                        command_parsed[4] = str(command_float[0])
                        command_parsed[5] = str(command_float[1])
                        command_parsed[6] = str(command_float[2])
                        self.app.command_parsed[4] = command_parsed[4]
                        self.app.command_parsed[5] = command_parsed[5]
                        self.app.command_parsed[6] = command_parsed[6]
                        self.app.time_counter += (np.pi * float(command_parsed[7])) / 180
                    elif command_parsed[3] == "origin":
                        self.app.command_parsed[4] = command_parsed[4]
                        self.app.command_parsed[5] = command_parsed[5]
                        self.app.command_parsed[6] = command_parsed[6]
                        self.app.time_counter = (np.pi * float(command_parsed[7])) / 180
                    self.app.rotation_flag = 0

            elif command_parsed[1] == "move":
                command_float[0] = float(self.app.command_parsed[1]) + float(command_parsed[2])
                command_float[1] = float(self.app.command_parsed[2]) + float(command_parsed[3])
                command_float[2] = float(self.app.command_parsed[3]) + float(command_parsed[4])
                command_parsed[2] = str(command_float[0])
                command_parsed[3] = str(command_float[1])
                command_parsed[4] = str(command_float[2])
                self.app.command_parsed[1] = command_parsed[2]
                self.app.command_parsed[2] = command_parsed[3]
                self.app.command_parsed[3] = command_parsed[4]

            elif command_parsed[1] == "color":
                self.app.figure_color_flag = 1

            elif command_parsed[1] == "figure":
                self.app.command_parsed[0] = command_parsed[2]



        return list(command_parsed)
