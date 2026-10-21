import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from logger import log_state
import player
def main():
    pygame.init()
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    clock = pygame.time.Clock()
    dt = 0.0
    a = player.Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    while True:
        screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        log_state()
        for event in pygame.event.get():
            a.draw(screen)
            if event.type == pygame.QUIT:
                pass

        screen.fill("black")
        pygame.display.flip()
        clock.tick(60)
        dt = clock.tick(60)/1000



if __name__ == "__main__":
    main()
