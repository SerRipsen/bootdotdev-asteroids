import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from logger import log_state

def main():
    print(f"""Starting Asteroids with pygame version: {pygame.version.ver}
          Screen width: {SCREEN_WIDTH}
          Screen height: {SCREEN_HEIGHT}""")

    pygame.init()
    game_clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    while True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        
        # set game speed to 60fps
        dt = game_clock.tick(60) / 1000

        # refresh the screen
        pygame.display.flip()


if __name__ == "__main__":
    main()
