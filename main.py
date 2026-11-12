import pygame
import sys

from constants import SCREEN_WIDTH,SCREEN_HEIGHT
from logger import log_state, log_event
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH }")
    print(f"Screen height: {SCREEN_HEIGHT}")
    pygame.init()
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Shot.containers=(shots, drawable, updatable)
    AsteroidField.containers = (updatable)
    Asteroid.containers =(asteroids, updatable, drawable)
    Player.containers = (updatable, drawable)
    clock = pygame.time.Clock()
    asteroidfield = AsteroidField()
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    dt = 0.0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    while True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        updatable.update(dt)
        for asteroid in asteroids:
            for shot in shots:
                shot_check=shot.collides_with(asteroid)
                if shot_check:
                    log_event("asteroid_shot")
                    shot.kill()
                    asteroid.split()
        for asteroid in asteroids:
            collision_check = player.collides_with(asteroid)
            if collision_check:
                log_event("player_hit")
                print("Game Over!")
                sys.exit()
        screen.fill("black")
        for group in drawable:
            group.draw(screen)
        pygame.display.flip()
        dt=(clock.tick(60)/1000)




if __name__ == "__main__":
    main()
