import pygame
from circleshape import *
from constants import *
from shot import *

class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS) #calls the parent CircleShape
        self.rotation = 0 #stores the rotation as an instance variable
        self.timer = 0

    def triangle(self):
        forward = pygame.Vector2(0,1).rotate(self.rotation)
        right = pygame.Vector2(0,1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def draw(self, screen):
        #Look up the draw command in PYCHARM to get inputs
        pygame.draw.polygon(screen, "white", self.triangle(), 2)

    def rotate(self, dt):
        self.rotation += PLAYER_TURNED_SPEED * dt
        self.timer -= dt

    def update(self, dt):
        keys = pygame.key.get_pressed()
        
        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-dt)
        if keys[pygame.K_SPACE] and self.timer <= 0:
            self.shoot(dt)
            self.timer = PLAYER_SHOOT_COOLDOWN

    def move(self, dt):
        forward = pygame.Vector2(0,1).rotate(self.rotation) #draw a vector from Pygame and utilize the rotation within the movement.
        self.position += forward * PLAYER_SPEED * dt

    def shoot(self, dt):
        # Start the shot at the player's position
        shot_position = self.position.copy()

        # Calculate the velocity of the shot
        shot_velocity = pygame.Vector2(0, 1).rotate(self.rotation) * PLAYER_SHOT_SPEED

        # Create a new Shot object and add it to the containers
        shot = Shot(shot_position.x, shot_position.y, SHOT_RADIUS, shot_velocity)
        shot.add(Shot.containers)
        


