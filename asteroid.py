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
        a1 = self.velocity.rotate(angle)
        a2 = self.velocity.rotate(-angle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        first_asteroid = Asteroid(self.position.x, self.position.y, new_radius)
        second_asteroid = Asteroid(self.position.x, self.position.y, new_radius)
        first_asteroid.velocity = a1 *1.2
        second_asteroid.velocity = a2 *1.2
