import pygame
from shoot import Shoot
from math import cos, sin, pi, atan2

class Gun:
    def __init__(self, ammo, x=450, y=650, speed = 6):
        self.ammo = ammo
        self.x = x
        self.y = y
        self.vx = 0
        self.vy = 0
        self.speed = speed
        self.gun = pygame.image.load('rifle.png')
        self.gun = pygame.transform.scale_by(self.gun, 0.5)
        self.rect = self.gun.get_rect(center=(self.x, self.y))
        self.theta = 0
    
    def draw(self, surface):
        self.rect.center = (self.x, self.y)
        #determines if gun goes off screen ornot
        if not surface.get_rect().contains(self.rect):
            self.contain(surface.get_rect())
        surface.blit(self.gun,self.rect)
        
    def contain(self, screen_rect):
        #moves self.rect back to screen edge if it goes off
        self.rect.clamp_ip(screen_rect)
        self.x, self.y = self.rect.center
        
    
    def update(self,e):
        if e.type == pygame.KEYDOWN:
            #check for keydown
            if e.key == pygame.K_UP:
                self.y -= self.speed
                self.vy = -self.speed
            elif e.key == pygame.K_DOWN:
                self.y += self.speed
                self.vy = self.speed
            elif e.key == pygame.K_RIGHT:
                self.x += self.speed
                self.vx = self.speed
            elif e.key == pygame.K_LEFT:
                self.x -= self.speed
                self.vx = -self.speed
        #reset velocity of bullet after shoots to zero
        elif e.type == pygame.KEYUP:
            if e.key == pygame.K_UP or pygame.K_DOWN:
                self.vy = 0
            elif e.key == pygame.K_RIGHT or pygame.K_LEFT:
                self.vx = 0
        #mouse to shoot
        elif e.type == pygame.MOUSEBUTTONDOWN:
            if len(self.ammo) < 5:
                gun = pygame.mixer.Sound('gun.mp3')
                gun.set_volume(1)
                gun.play()
                spawn_x = self.x - 56.8
                spawn_y = self.y - 128
                bullet = Shoot(spawn_x, spawn_y, self.vy, self.vx)
                self.ammo.add(bullet)
        
    
        
    
    