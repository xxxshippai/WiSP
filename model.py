import numpy as np
import glm


class Figure:

    def __init__(self, app):
        self.app = app
        self.ctx = app.ctx
        self.vbo = self.get_vbo()
        self.shader_program = self.get_shader_program('default')
        self.vao = self.get_vao()
        self.m_model = self.get_model_matrix()
        self.on_init()

    def update(self):
        m_model = glm.rotate(self.m_model, self.app.time_counter, glm.vec3(self.app.direction_x, self.app.direction_y, 0))
        self.shader_program['m_model'].write(m_model)

    def get_model_matrix(self):
        m_model = glm.mat4()
        return m_model

    def on_init(self):
        # MVP
        self.shader_program['m_proj'].write(self.app.camera.m_proj)
        self.shader_program['m_view'].write(self.app.camera.m_view)
        self.shader_program['m_model'].write(self.m_model)

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

    def get_vertex_data(self):
        if self.app.figure_type == 1:
            vertices = [(-1, -1, 1), (1, -1, 1), (1, 1, 1), (-1, 1, 1),
                        (-1, 1, -1), (-1, -1, -1), (1, -1, -1), (1, 1, -1)]

            indices = [(0, 2, 3), (0, 1, 2),
                       (1, 7, 2), (1, 6, 7),
                       (6, 5, 4), (4, 7, 6),
                       (3, 4, 5), (3, 5, 0),
                       (3, 7, 4), (3, 2, 7),
                       (0, 6, 1), (0, 5, 6)]
        elif self.app.figure_type == 2:
            vertices = [(-1, -1, 1), (1, -1, 1),
                        (1, -1, -1), (-1, -1, -1),
                        (0, 1, 0)]

            indices = [(0, 1, 2), (0, 2, 3),
                       (0, 1, 4), (1, 2, 4),
                       (2, 3, 4), (3, 0, 4)]

        elif self.app.figure_type == 3:
            vertices = []
            indices = []

            angle_increment = 360. / 40
            angle_increment *= np.pi / 180.

            angle = 0.
            h = 0

            # Vertices handling
            for j in range(80):
                vertices.append((1 * np.cos(angle), -1 + h, 1 * np.sin(angle)))
                if j == 39:
                    h = 2

                angle += angle_increment

            vertices.append((0, 0, -1))
            vertices.append((0, 0, 1))

            # Indices handling
            for i in range(39):
                indices.append((0 + i, 1 + i, 41 + i))
                indices.append((0 + i, 41 + i, 40 + i))

            indices.append((39, 0, 40))
            indices.append((39, 40, 79))

            # Base
            for i in range(39):
                indices.append((0 + i, 1 + i, 80))
            indices.append((39, 0, 80))
            # Top
            for j in range(39):
                indices.append((40 + i, 41 + i, 81))
            indices.append((79, 40, 81))

        elif self.app.figure_type == 4:
            vertices = []
            indices = []

            angle_increment = 360. / 40
            angle_increment *= np.pi / 180.

            angle = 0.
            h = 0

            # Vertices handling
            for j in range(40):
                vertices.append((1 * np.cos(angle), -1 + h, 1 * np.sin(angle)))
                if j == 39:
                    h = 2

                angle += angle_increment

            vertices.append((0, -1, 0))
            vertices.append((0, 1, 0))

            # Indices handling
            for i in range(39):
                indices.append((0 + i, 1 + i, 41))

            indices.append((39, 0, 41))

            # Base
            for i in range(39):
                indices.append((0 + i, 1 + i, 40))
            indices.append((39, 0, 40))

        vertex_data = self.get_data(vertices, indices)
        return vertex_data

    @staticmethod
    def get_data(vertices, indices):
        data = [vertices[ind] for triangle in indices for ind in triangle]
        return np.array(data, dtype='f4')

    # Vertex buffer object definition
    def get_vbo(self):
        vertex_data = self.get_vertex_data()
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
