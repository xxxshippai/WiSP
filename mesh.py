import numpy as np


class Mesh:

    def get_vertex_data_cuboid(self, x=0, y=0, z=0, a=2, b=2, c=2):
        vertices = [(x + -(a / 2), y + -(b / 2), z + (c / 2)),
                    (x + (a / 2), y + -(b / 2), z + (c / 2)),
                    (x + (a / 2), y + (b / 2), z + (c / 2)),
                    (x + -(a / 2), y + (b / 2), z + (c / 2)),
                    (x + -(a / 2), y + (b / 2), z + -(c / 2)),
                    (x + -(a / 2), y + -(b / 2), z + -(c / 2)),
                    (x + (a / 2), y + -(b / 2), z + -(c / 2)),
                    (x + (a / 2), y + (b / 2), z + -(c / 2))]

        indices = [(0, 2, 3), (0, 1, 2),
                   (1, 7, 2), (1, 6, 7),
                   (6, 5, 4), (4, 7, 6),
                   (3, 4, 5), (3, 5, 0),
                   (3, 7, 4), (3, 2, 7),
                   (0, 6, 1), (0, 5, 6)]

        vertex_data = self.get_data(vertices, indices)
        return vertex_data

    def get_vertex_data_pyramid(self, x=0, y=0, z=0, a=2, h=2):
        vertices = [(x + -(a / 2), y + -(h / 2), z + (a / 2)),
                    (x + (a / 2), y + -(h / 2), z + (a / 2)),
                    (x + (a / 2), y + -(h / 2), z + -(a / 2)),
                    (x + -(a / 2), y + -(h / 2), z + -(a / 2)),
                    (x + 0, y + (h / 2), z + 0)]
        # Indices declarations, do not change
        indices = [(0, 1, 2), (0, 2, 3),
                   (0, 1, 4), (1, 2, 4),
                   (2, 3, 4), (3, 0, 4)]

        # Parse indice and vertice data together
        vertex_data = self.get_data(vertices, indices)
        return vertex_data

    def get_vertex_data_cylinder(self, x=0, y=0, z=0, r=1, h=2):

        vertices = []
        indices = []

        angle_increment = 360. / 40
        angle_increment *= np.pi / 180.

        angle = 0.

        # Vertices handling
        for j in range(40):
            vertices.append((x + (r * np.cos(angle)), y + -(h/2), z + (r * np.sin(angle))))

            angle += angle_increment

        for j in range(40):
            vertices.append((x + (r * np.cos(angle)), y + (h/2), z + (r * np.sin(angle))))

            angle += angle_increment

        vertices.append((x, y + -(h/2), z))
        vertices.append((x, y + (h/2), z))

        # # Indices declarations, do not change
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
            indices.append((40 + j, 41 + j, 81))
        indices.append((79, 40, 81))

        # Parse indice and vertice data together
        vertex_data = self.get_data(vertices, indices)
        return vertex_data

    def get_vertex_data_cone(self, x=0, y=0, z=0, r=1, h=2):
        vertices = []
        indices = []

        angle_increment = 360. / 40
        angle_increment *= np.pi / 180.

        angle = 0.

        # Vertices handling
        for j in range(40):
            vertices.append((x + (r * np.cos(angle)), y + -(h/2), z + (r * np.sin(angle))))
            if j == 39:
                h = 2

            angle += angle_increment

        vertices.append((x + 0, y + -(h/2), z + 0))
        vertices.append((x + 0, y + (h/2), z + 0))

        # # Indices declarations, do not change
        for i in range(39):
            indices.append((0 + i, 1 + i, 41))

        indices.append((39, 0, 41))

        # Base
        for i in range(39):
            indices.append((0 + i, 1 + i, 40))
        indices.append((39, 0, 40))

        # Parse indice and vertice data together
        vertex_data = self.get_data(vertices, indices)
        return vertex_data

    @staticmethod
    def get_data(vertices, indices):
        data = [vertices[ind] for triangle in indices for ind in triangle]
        return np.array(data, dtype='f4')
