import circleshape

from constants import PLAYER_RADIUS



class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, radius)
        self.radius = radius
        self.x = x
        self.y = y
        self.rotation = 0
