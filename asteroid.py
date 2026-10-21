from circleshape import CircleShape
import pygame
from constants import LINE_WIDTH, PLAYER_RADIUS

class Asteroid(CircleShape):
    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y, radius)


    def draw(self, screen: pygame.Surface) -> None:
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)
        pass
    def update(self, dt: float) -> None:
        # must override
        pass
