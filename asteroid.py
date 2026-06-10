from circleshape import CircleShape
import pygame
from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS
from logger import log_event
import random

class Asteroid (CircleShape):
    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y, radius)

    # draw asteroid
    def draw(self, screen:pygame.Surface):
        pygame.draw.circle(screen, "white",self.position, self.radius, LINE_WIDTH)
        
    def update(self, dt: float)-> None:
        self.position += self.velocity * dt
    
    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            log_event("asteroid_split")
            angle = random.uniform(20, 50)
            asteroid_1_vector =self.velocity.rotate(angle)
            asteroid_2_vector = self.velocity.rotate(-angle)
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            asteroid_1 = Asteroid(self.position.x, self.position.y, new_radius)
            asteroid_2 = Asteroid(self.position.x,self.position.y, new_radius)
            asteroid_1.velocity = asteroid_1_vector * 1.2
            asteroid_2.velocity = asteroid_2_vector * 1.2