import glm

FOV = 50


class Camera:
    def __init__(self, app, projection_type=1, NEAR=0.1, FAR=100):
        self.app = app
        self.NEAR = NEAR
        self.FAR = FAR
        self.aspect_ratio = app.WIN_SIZE[0] / app.WIN_SIZE[1]
        self.position = glm.vec3(0, 10, 15)
        self.up = glm.vec3(0, 1, 0)
        # View matrix
        self.m_view = self.get_view_matrix()
        # Projection matrix
        self.m_proj = self.get_projection_matrix(projection_type)

    def get_view_matrix(self):
        return glm.lookAt(self.position, glm.vec3(0), self.up)

    def get_projection_matrix(self, projection_type=1):
        if projection_type == 1:
            return glm.perspective(glm.radians(FOV), self.aspect_ratio, self.NEAR, self.FAR)
        elif projection_type == 2:
            return glm.ortho(-100, 100, -50, 50, self.NEAR, self.FAR)
