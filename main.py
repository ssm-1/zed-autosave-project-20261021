import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from logger import log_state, log_event
import player
from asteroid import Asteroid
from asteroidfield import AsteroidField
import asteroidfield
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

def main():
    dt = 0.0

    pygame.init()
    print(f"Starting Asteroids with pygame version: {pygame.version}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()

    player.Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    asteroidfield.AsteroidField.containers = (updatable)
    b = asteroidfield.AsteroidField()
    a = player.Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    while True:
        log_state()
        clock = pygame.time.Clock()
        clock.tick(60)


        updatable.update(dt)
        screen.fill("black")
        for event in pygame.event.get():
            a.draw(screen)
            if event.type == pygame.QUIT:
                return


        pygame.display.flip()

        dt = clock.tick(60)/1000





if __name__ == "__main__":
    main()
