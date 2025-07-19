import pygame

from constants import *

from player import *
from asteroid import *
from asteroidfield import *
from shot import *

def main():
   
    pygame.init()

    clock = pygame.time.Clock()

    dt = 0
    
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    updatable = pygame.sprite.Group()

    drawable = pygame.sprite.Group()

    asteroids = pygame.sprite.Group()

    shots = pygame.sprite.Group()
    
    Player.containers = (updatable, drawable)

    Asteroid.containers = (updatable, drawable, asteroids)

    AsteroidField.containers = (updatable)

    Shot.containers = (shots, updatable, drawable)
    
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    asteroidfield = AsteroidField()
    
    while True:
        screen.fill((0,0,0))
        updatable.update(dt)
        for asteroid in asteroids:
            if asteroid.collide(player):
                print("Game Over!")
                raise SystemExit
        for asteroid in asteroids:
            for shot in shots:
                if asteroid.collide(shot):
                    asteroid.split()
                    shot.kill()
        for o in drawable:
            o.draw(screen)
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        dt = clock.tick(60) / 1000
        

if __name__ == "__main__":
    main()
