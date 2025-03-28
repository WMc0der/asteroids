import pygame

#Base class for game objects:
class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        # Add this to CircleShape.__init__
        self.rect = pygame.Rect(x - radius, y - radius, radius * 2, radius * 2)
       
       #we will be using this later
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()


        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0 , 0)
        self.radius = radius

    def draw(self, screen):
        #sub-classes must override
        pass

    def update(self, dt):
        self.rect.center = (int(self.position.x), int(self.position.y))

    
    def collision(self, other_shape):
        distance = self.position.distance_to(other_shape.position)
        result = distance <= (self.radius + other_shape.radius)
        if result:
            print(f"Collision detected! Distance: {distance}, Sum of radii: {self.radius + other_shape.radius}")
        return result

