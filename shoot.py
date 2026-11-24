import pygame
from math import sin, cos, pi

class Shoot(pygame.sprite.Sprite):
    def __init__(self, x, y, gun_vy, gun_vx):
        super().__init__()
        self.x = x
        self.y = y
        y_speed = -12.5
        self.gravity = 0.2
        height_reduction = abs(gun_vx) * 0.5
        self.vy = y_speed + height_reduction + gun_vy
        self.vx = gun_vx
        self.og_image = pygame.image.load('shot_yellow_small.png')
        self.image = pygame.transform.rotozoom(self.og_image, -90, 0.85)
        self.rect = self.image.get_rect(center=(self.x, self.y))
    
    def update (self, screen_rect):
        self.vy += self.gravity
        self.y += self.vy
        self.x += self.vx
        #self.image=pygame.transform.rotate(self.og_image,self.theta)
        self.rect.center = (self.x, self.y)
        #kill bullet when not in screen
        if not screen_rect.contains(self.rect):
            self.kill()