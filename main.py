import pygame

from constants import *

from player import *

def main():
   
    pygame.init()

    clock = pygame.time.Clock()

    dt = 0
    
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    updatable = pygame.sprite.Group()

    drawable = pygame.sprite.Group()
    
    Player.containers = (updatable, drawable)
    
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    
    while True:
        screen.fill((0,0,0))
        updatable.update(dt)
        for o in drawable:
            o.draw(screen)
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        dt = clock.tick(60) / 1000
        

if __name__ == "__main__":
    main()
