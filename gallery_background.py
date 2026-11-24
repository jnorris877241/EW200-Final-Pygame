import pygame

icy_blue = (189,224,254)

def make_bg(SIZE, TS):
    bg = pygame.Surface(SIZE)
    bg.fill(icy_blue)
    
    wood = pygame.image.load('bg_wood.png')
    #put wood on the bg
    for x in range(11):
        for y in range(8):
            bg.blit(wood, (x*TS,y*TS))
    #put grass
    grass = pygame.image.load('grass1.png')
    grass_y = 4*TS
    for x in range(0,11*TS, int(1.65*TS)):
            bg.blit(grass, (x, grass_y))
    #add trees
    oak = pygame.image.load('tree_oak.png')
    bg.blit(oak, (2*TS, int(2.5*TS)))
    pine = pygame.image.load('tree_pine.png')
    bg.blit(pine, (7*TS, int(2.5*TS)))
    #put water
    water1 = pygame.image.load('water1.png')
    water_y1 = 5*TS
    for x in range(0,11*TS, int(1.65*TS)):
            bg.blit(water1, (x, water_y1))
    water2 = pygame.image.load('water2.png')
    water_y2 = 6*TS
    for x in range(0,11*TS, int(1.65*TS)):
            bg.blit(water2, (x, water_y2))
    #put side curtains
    curtains = pygame.image.load('curtain.png')
    curtains = pygame.transform.scale_by(curtains, 1.2)
    R_curtain = curtains
    R_curtain = pygame.transform.flip(R_curtain, 1, 0)
    bg.blit(curtains,(0,0))
    bg.blit(R_curtain, (int(9.05*TS), 0*TS))
    #add main curtain
    curtain = pygame.image.load('curtain_straight.png')
    for x in range(0,11*TS, int(3.2*TS)):
        bg.blit(curtain, (x,0))
    
            
    return bg