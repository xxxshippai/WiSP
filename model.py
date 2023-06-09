import numpy as np
import glm
from mesh import Mesh


class Figure:

    def __init__(self, app):
        self.app = app
        self.ctx = app.ctx
        self.rotation_x = 0
        self.rotation_y = 1
        self.rotation_z = 0
        self.mesh = Mesh(self.app)
        self.vbo = self.get_vbo()
        self.shader_program = self.get_shader_program('default')
        self.vao = self.get_vao()
        self.m_model = self.get_model_matrix()
        self.on_init()

    def update(self):
        # Rotation vector
        self.rotation_x = float(self.app.command_parsed[4])
        self.rotation_y = float(self.app.command_parsed[5])
        self.rotation_z = float(self.app.command_parsed[6])
        m_model = glm.rotate(self.m_model, self.app.time_counter,
                             glm.vec3(self.rotation_x, self.rotation_y, self.rotation_z))
        self.shader_program['m_model'].write(m_model)
        self.shader_program['m_view'].write(self.app.camera.m_view)
        self.shader_program['color'].write(self.app.figure_color)

    def get_model_matrix(self):
        m_model = glm.mat4()
        return m_model

    def on_init(self):
        # MVP
        self.shader_program['m_proj'].write(self.app.camera.m_proj)
        self.shader_program['m_view'].write(self.app.camera.m_view)
        self.shader_program['m_model'].write(self.m_model)
        self.shader_program['color'].write(self.app.figure_color)

    def render(self):
        self.update()
        self.vao.render()

    def destroy(self):
        self.vbo.release()
        self.shader_program.release()
        self.vao.release()

    # Vertex array object for combining VBO data and shaders
    def get_vao(self):
        vao = self.ctx.vertex_array(self.shader_program, [(self.vbo, '3f', 'in_position')])
        return vao

    def get_mesh(self):

        if self.app.figure_loaded == 1:
            # Load structures from file
            if self.app.command_read[1] == "load":
                self.app.file_name = self.app.command_read[2]
                self.app.command_parsed[1] = self.app.command_read[3]
                self.app.command_parsed[2] = self.app.command_read[4]
                self.app.command_parsed[3] = self.app.command_read[5]

        # Origin coordinates
        x = float(self.app.command_parsed[1])
        y = float(self.app.command_parsed[2])
        z = float(self.app.command_parsed[3])

        if self.app.figure_loaded == 0:
            # Create prefab structures
            if self.app.command_parsed[0] == "cuboid":
                vertex_data = self.mesh.get_vertex_data_cuboid(x, y, z,
                                                               float(self.app.command_parsed[7]),
                                                               float(self.app.command_parsed[8]),
                                                               float(self.app.command_parsed[9]))
            elif self.app.command_parsed[0] == "pyramid":
                vertex_data = self.mesh.get_vertex_data_pyramid(x, y, z,
                                                                float(self.app.command_parsed[7]),
                                                                float(self.app.command_parsed[8]))
            elif self.app.command_parsed[0] == "cylinder":
                vertex_data = self.mesh.get_vertex_data_cylinder(x, y, z,
                                                                 float(self.app.command_parsed[7]),
                                                                 float(self.app.command_parsed[8]))
            elif self.app.command_parsed[0] == "cone":
                vertex_data = self.mesh.get_vertex_data_cone(x, y, z,
                                                             float(self.app.command_parsed[7]),
                                                             float(self.app.command_parsed[8]))
            elif self.app.command_parsed[0] == "sphere":
                vertex_data = self.mesh.get_vertex_data_sphere(x, y, z,
                                                               int(self.app.command_parsed[7]),
                                                               int(self.app.command_parsed[8]))
        elif self.app.figure_loaded == 1:
            # Load structures from file
            vertex_data = self.mesh.load_vertex_data(self.app.file_name, x, y, z)

        if self.app.command_read[1] == "save":
            print("Saving")
            file_name = self.app.command_read[2]
            self.mesh.save_vertex_data(file_name, self.app.cached_vertex)

        return vertex_data

    @staticmethod
    def get_data(vertices, indices):
        data = [vertices[ind] for triangle in indices for ind in triangle]
        return np.array(data, dtype='f4')

    # Vertex buffer object definition
    def get_vbo(self):
        vertex_data = self.get_mesh()
        vbo = self.ctx.buffer(vertex_data)
        return vbo

    # Open shaders
    def get_shader_program(self, shader_name):
        with open(f'shaders/{shader_name}.vert') as file:
            vertex_shader = file.read()

        with open(f'shaders/{shader_name}.frag') as file:
            fragment_shader = file.read()

        program = self.ctx.program(vertex_shader=vertex_shader, fragment_shader=fragment_shader)
        return program
