from circleshape import CircleShape
from constants import *
import pygame

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        # Call the parent class constructor
        CircleShape.__init__(self, x, y, radius)
        
    def draw(self, screen):
        # The parameters for pygame.draw.circle are:
        # surface, color, position, radius, width(optional)
        pygame.draw.circle(screen, "white", (int(self.position.x), int(self.position.y)), self.radius, 2)
        
    def update(self, dt):
        self.position += self.velocity * dt
