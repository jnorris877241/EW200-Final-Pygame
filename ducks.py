import pygame
from shoot import Shoot
from random import randint

class Ducks(pygame.sprite.Sprite):
    def __init__(self, TS, vx, vy):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('duck_outline_target_brown.png')
        self.image = pygame.transform.scale_by(self.image, 0.8)
        self.x = randint(100, 10*TS)
        self.y = randint(2*TS, 6*TS)
        self.vx = vx
        self.vy = vy
        self.rect = self.image.get_rect(center = (self.x, self.y))
        
    def update(self, surface):
        self.x += self.vx
        self.y += self.vy
        if self.x < 100 or self.x> 800:
            self.vx = -self.vx
        if self. y < 160 or self.y> 480:
            self.vy = -self.vy
        self.rect.center = (self.x, self.y)
        surface.blit(self.image,self.rect)
        
    #def check_bullet(self, ammo):
        #collided_ducks = pygame.sprite.spritecollide(self, ammo, True)
        #if collided_ducks:
            #self.kill()
    
        