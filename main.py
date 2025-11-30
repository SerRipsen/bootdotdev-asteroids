import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from player import Player
from logger import log_state

def main():
    print(f"""Starting Asteroids with pygame version: {pygame.version.ver}
          Screen width: {SCREEN_WIDTH}
          Screen height: {SCREEN_HEIGHT}""")

    # initialise basic info
    pygame.init()
    game_clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # create groups of updatable, drawable
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Player.containers = (updatable, drawable)

    # create player
    player = Player((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2))

    # main game loop
    while True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        # render the screen items
        screen.fill("black")
        updatable.update(dt)
        for _draw in drawable:
            _draw.draw(screen)
            
        
        # set game speed to 60fps and update the clock
        dt = game_clock.tick(60) / 1000

        # refresh the screen
        pygame.display.flip()


if __name__ == "__main__":
    main()
