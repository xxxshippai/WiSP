import glm
import pygame as pg

FOV = 50
SPEED = 0.01
SENSITIVITY = 0.1

class Camera:
    def __init__(self, app, projection_type=1, NEAR=0.1, FAR=100, position=(0, 0, 4), yaw=-90, pitch=0):
        self.app = app
        self.NEAR = NEAR
        self.FAR = FAR
        self.aspect_ratio = app.WIN_SIZE[0] / app.WIN_SIZE[1]
        # Camera origin position
        self.position = glm.vec3(position)
        # Movement vectors
        self.up = glm.vec3(0, 1, 0)
        self.right = glm.vec3(1, 0, 0)
        self.forward = glm.vec3(0, 0, -1)
        # Euler rotation angles
        self.yaw = yaw
        self.pitch = pitch
        # View matrix
        self.m_view = self.get_view_matrix()
        # Projection matrix
        self.m_proj = self.get_projection_matrix(projection_type)

    def update(self):
        self.move()
        self.rotate()
        self.update_camera_vectors()
        self.m_view = self.get_view_matrix()

    def rotate(self):
        rel_x, rel_y = pg.mouse.get_rel()
        self.yaw += rel_x * SENSITIVITY
        self.pitch -= rel_y * SENSITIVITY
        self.pitch = max(-89, min(89, self.pitch))

    def update_camera_vectors(self):
        yaw, pitch = glm.radians(self.yaw), glm.radians(self.pitch)
        self.forward.x = glm.cos(yaw) * glm.cos(pitch)
        self.forward.y = glm.sin(pitch)
        self.forward.z = glm.sin(yaw) * glm.cos(pitch)

        self.forward = glm.normalize(self.forward)
        self.right = glm.normalize(glm.cross(self.forward, glm.vec3(0, 1, 0)))
        self.up = glm.normalize((glm.cross(self.right, self.forward)))

    def move(self):
        velocity = SPEED * self.app.delta_time
        keys = pg.key.get_pressed()
        if keys[pg.K_w]:
            self.position += self.forward * velocity
        if keys[pg.K_s]:
            self.position -= self.forward * velocity
        if keys[pg.K_d]:
            self.position += self.right * velocity
        if keys[pg.K_a]:
            self.position -= self.right * velocity
        if keys[pg.K_q]:
            self.position += self.up * velocity
        if keys[pg.K_e]:
            self.position -= self.up * velocity

    def get_view_matrix(self):
        return glm.lookAt(self.position, self.position + self.forward, self.up)

    def get_projection_matrix(self, projection_type=1):
        if projection_type == 1:
            return glm.perspective(glm.radians(FOV), self.aspect_ratio, self.NEAR, self.FAR)
        elif projection_type == 2:
            return glm.ortho(-100, 100, -50, 50, self.NEAR, self.FAR)
