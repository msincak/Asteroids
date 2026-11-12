from circleshape import CircleShape
from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS
from logger import log_event
import random
import pygame

class Asteroid(CircleShape):
    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y, radius)

    def draw(self, screen: pygame.Surface) -> None:
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt:float) -> None:
        self.position+=self.velocity *dt

    def split(self) ->None:
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            log_event("asteroid_split")
            angle = random.uniform(20, 50)
            new_vector= self.velocity.rotate(angle)
            another_vector=self.velocity.rotate(-angle)
            new_radius= self.radius - ASTEROID_MIN_RADIUS
            
            asteroid_new1=Asteroid(self.position.x, self.position.y, new_radius)
            asteroid_new1.velocity=new_vector*1.2

            asteroid_new2=Asteroid(self.position.x, self.position.y, new_radius)
            asteroid_new2.velocity=another_vector*1.2
            


