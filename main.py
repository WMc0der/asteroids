import pygame
from constants import *
from player import *
from asteroidfield import *
import sys

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
    shots = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable,)
    Shot.containers = (shots, updatable, drawable)
    #Add splitting asteroids to group?
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
        
        # Handle collisions between shots and asteroids
        #collisions = pygame.sprite.groupcollide(asteroids, shots, dokilla=False, dokillb=True)
        to_kill_asteroids = []
        to_kill_shots = []
            
        for asteroid in asteroids:
            if asteroid.collision(player):
                print("Game over!")
                sys.exit()

            for shot in shots:
                if asteroid.collision(shot):  # Assuming you defined a `collision` method
                    if asteroid not in to_kill_asteroids:
                        to_kill_asteroids.append(asteroid)
                    if shot not in to_kill_shots:
                        to_kill_shots.append(shot)


                        #asteroid.split()  # Split the asteroid into smaller ones if needed

# Remove asteroids and shots after the loop
        for asteroid in to_kill_asteroids:
            asteroid.split()

        for shot in to_kill_shots:
            shot.kill()
        
        pygame.display.flip()
        dt = clock.tick(60)/1000

if __name__ == "__main__":
    main()
