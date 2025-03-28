from circleshape import CircleShape
from constants import *
import pygame
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        # Call the parent class constructor
        super().__init__(x, y, radius)
        
    def draw(self, screen):
        # The parameters for pygame.draw.circle are:
        # surface, color, position, radius, width(optional)
        pygame.draw.circle(screen, "white", (int(self.position.x), int(self.position.y)), self.radius, 2)
        
    def update(self, dt):
        self.position += self.velocity * dt
        super().update(dt)

    def split(self):
        self.kill()
        print(f"Splitting asteroid at {self.position} with radius {self.radius}")
        

        if self.radius <= ASTEROID_MIN_RADIUS:
            return

        random_angle = random.uniform(20, 50)

        a = self.velocity.rotate(random_angle)
        b = self.velocity.rotate(-random_angle)

        new_radius = self.radius - ASTEROID_MIN_RADIUS
    
        # Create first asteroid
        asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid1.velocity = a * 1.2
    
        # Create second asteroid
        asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid2.velocity = b * 1.2

        asteroid1.add(*self.containers)
        asteroid2.add(*self.containers)

        
        

