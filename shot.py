import pygame
from constants import *
from asteroidfield import *
from circleshape import CircleShape

class Shot(CircleShape):
    def __init__(self, x, y, radius, velocity):
        # Call the parent class constructor correctly
        super().__init__(x, y, radius)
        self.velocity = velocity

    def draw(self, screen):
        # Properly position and draw the shot
        pygame.draw.circle(screen, "white", (int(self.position.x), int(self.position.y)), self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt
        super().update(dt)  # syncs rect center
   
