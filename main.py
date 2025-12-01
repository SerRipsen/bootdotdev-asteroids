import pygame
import sys
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from player import Player
from logger import log_state, log_event
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

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
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (updatable, drawable, shots)


    # create objects
    player = Player((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2))
    asteroidfield = AsteroidField()

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

        # check for player x asteroid collisions
        for _asteroid in asteroids:
            if _asteroid.collides_with(player):
                log_event("player_hit")
                print("Game over!")
                sys.exit()
            
        # check for shot x asteroid collisions
        for _asteroid in asteroids:
            for _shot in shots:
                if _asteroid.collides_with(_shot):
                    log_event("asteroid_shot")
                    _asteroid.kill()
                    _shot.kill()
        
        # set game speed to 60fps and update the clock
        dt = game_clock.tick(60) / 1000

        # refresh the screen
        pygame.display.flip()


if __name__ == "__main__":
    main()
