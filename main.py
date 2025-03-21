import pygame
from constants import *
from player import *
from asteroidfield import *

def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    pygame.init()

    # SETTING THE FRAME RATE
    clock = pygame.time.Clock()
    # dt = delta time
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    running = True
    
    #GROUPS
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    Player.containers = (updatable, drawable, asteroids)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    asteroid_field = AsteroidField()
    player=Player(SCREEN_WIDTH/2 , SCREEN_HEIGHT/2) #since we're importing Player from player.py file we can go ahead and utilize the function created inside of the file.



    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        screen.fill((0, 0, 0))  # Note: This needs a tuple (0, 0, 0), not 0,0,0
        for entity in drawable:
            entity.draw(screen)
        updatable.update(dt)
        pygame.display.flip()
        dt = clock.tick(60)/1000

if __name__ == "__main__":
    main()
