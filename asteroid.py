import pygame
from circleshape import CircleShape
import random
from constants import ASTEROID_MAX_RADIUS, ASTEROID_MIN_RADIUS


class Asteroid(CircleShape):
    def __init__(self, x, y, radius=None, velocity=None):
        if radius is None:
            radius = ASTEROID_MAX_RADIUS
        super().__init__(x, y, radius)
        
        # If velocity wasn't provided, generate a random one
        if velocity is None:
            speed = random.uniform(50, 100)
            angle = random.uniform(0, 360)
            self.velocity = pygame.Vector2(0, speed).rotate(angle)
        else:
            self.velocity = velocity

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        # Kill the current asteroid
        self.kill()
        
        # If this is already a small asteroid, don't split
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        
        # Calculate new properties for child asteroids
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        split_angle = random.uniform(20, 50)
        
        # Create two new velocity vectors by rotating current velocity
        velocity1 = self.velocity.rotate(split_angle) * 1.2
        velocity2 = self.velocity.rotate(-split_angle) * 1.2
        
        # Spawn two new smaller asteroids
        Asteroid(self.position.x, self.position.y, new_radius, velocity1)
        Asteroid(self.position.x, self.position.y, new_radius, velocity2)
