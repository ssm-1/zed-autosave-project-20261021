from circleshape import CircleShape
import pygame
from constants import LINE_WIDTH, PLAYER_RADIUS, ASTEROID_MIN_RADIUS
from logger import log_event
import random

class Asteroid(CircleShape):
    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y, radius)


    def draw(self, screen: pygame.Surface) -> None:
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)
        pass

    def update(self, dt: float) -> None:
        # must override
        self.position += (self.velocity * dt)
    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return



        log_event("asteroid_split")
        angle = random.uniform(20,50)
        unit_vector = pygame.Vector2(0, 1)
        rotated_first_asteroid = unit_vector.rotate(angle)
        rotated_second_asteroid = unit_vector.rotate(-angle)
