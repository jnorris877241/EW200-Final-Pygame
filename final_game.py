import pygame
from gallery_background import make_bg
from gun_shoot import Gun
from ducks import Ducks
from shoot import Shoot
#import other classes here

pygame.init()
clock = pygame.time.Clock()

TS = 80
WIDTH = TS * 11
HEIGHT = TS * 9
SIZE = (WIDTH, HEIGHT)
speed = 0.5

#colors
icy_blue = (189,224,254)
orange = (255, 174, 3)
baltic_blue = (0,53,107)
hunter_green = (51, 103, 59)
pale_sky = (206, 229, 242)
dark_blue = (11, 0, 51)

#make screen
screen = pygame.display.set_mode(SIZE)
screen_rect=screen.get_rect()

#make main screen bg
wood = r"bg_wood.png"
wood_img = pygame.image.load(wood)
bg_main = pygame.Surface(SIZE)
for x in range(0, WIDTH):
    for y in range(0, HEIGHT):
        bg_main.blit(wood_img, (x*TS, y*TS))


#load fonts
font = pygame.font.Font('Cinzel-ExtraBold.ttf', size = 120)
font2 = pygame.font.Font('Cinzel-ExtraBold.ttf', size = 40)
#make the main screen text
title_surface = font.render('Duck Hunt!',1, baltic_blue)
title_rect = title_surface.get_rect()
title_rect.center = (WIDTH/2, HEIGHT/2-70)
subtitle_surface = font2.render('press SPACEBAR to play', 1, hunter_green)
subtitle_rect = subtitle_surface.get_rect()
subtitle_rect.center = (WIDTH/2, HEIGHT/2+30)
#level one text
level_one = font.render('LEVEL ONE', 1, icy_blue)
level1_rect = level_one.get_rect()
level1_rect.center = (WIDTH/2, HEIGHT/2)
#level two text
level_two = font.render('LEVEL TWO', 1, icy_blue)
level2_rect = level_two.get_rect()
level2_rect.center = (WIDTH/2, HEIGHT/2)
#level three text
level_three = font.render('LEVEL THREE', 1, icy_blue)
level3_rect = level_three.get_rect()
level3_rect.center = (WIDTH/2, HEIGHT/2)
#make end screen text 
end_surface = font.render('YOU WON!', 1, orange)
end_rect = end_surface.get_rect()
end_rect.center = (WIDTH/2, HEIGHT/2-30)
end_subtitle_surface = font2.render('press SPACEBAR to end', 1, hunter_green)
end_subtitle_rect = end_subtitle_surface.get_rect()
end_subtitle_rect.center = (WIDTH/2, HEIGHT/2+40)
#you lost text
lost_surface = font.render('YOU LOST!', 1, orange)
lost_rect = lost_surface.get_rect()
lost_rect.center = (WIDTH/2, HEIGHT/2-30)
#load sound
pygame.mixer.init()
quack = pygame.mixer.Sound('quack.mp3')
quack.set_volume(1)
theme_music = pygame.mixer.Sound('duck_background.mp3')
theme_music.set_volume(0.2)
lose = pygame.mixer.Sound('lose.mp3')
lose.set_volume(0.8)

#main game background
bg = make_bg(SIZE, TS)
#ammo sprite group
ammo = pygame.sprite.Group()
#make the gun
gun = Gun(ammo)
#ducks in game
ducks1 = pygame.sprite.Group()
ducks2 = pygame.sprite.Group()
ducks3 = pygame.sprite.Group()
#add 5 ducks
for i in range(6):
    ducks1.add(Ducks(TS, 0.75, 0.75))
    
for i in range(10):
    ducks2.add(Ducks(TS, 1.25, 1))

for i in range(15):
    ducks3.add(Ducks(TS, 2, 1.25))
time = 60
#repeat the key
pygame.key.set_repeat(20)
#INTRO SCREEN LOOP
leave = 1
running = 1
while leave:
    clock.tick(60)
    while running:
        screen.blit(bg_main, (0,0))
        theme_music.play()
        #blit the title to the screen
        screen.blit(title_surface,title_rect)
        screen.blit(subtitle_surface,subtitle_rect)
        pygame.display.flip()
        events = pygame.event.get()
        for e in events:
            if e.type == pygame.QUIT:
                running = 0
                leave = 0
                break
            if e.type == pygame.KEYDOWN:
                running = 0
    #MAIN GAME LOOP
    start1 = pygame.time.get_ticks()
    game_clock1 = pygame.time.get_ticks()
    if leave == 0:
        break
    running = 1
    #level one
    while running:
        #working on setting times for each screen to pass the levels
        while pygame.time.get_ticks() - start1 <= 3000:
            screen.fill(hunter_green)
            screen.blit(level_one, level1_rect)
            pygame.display.flip()
        #stop music
        theme_music.stop()
        while pygame.time.get_ticks() - game_clock1 <= 63000 and running==1:
            clock.tick(60)
            screen.blit(bg, (0,0))
            events = pygame.event.get()
            for e in events:
                if e.type == pygame.QUIT:
                        running = 0
                        leave = 0
                        break
                gun.update(e)
            #kill both duck and ammo when collide
            hit = pygame.sprite.groupcollide(ducks1, ammo, True, True)
            if hit:
                quack.play()
            ducks1.update(screen)
            ammo.update(screen_rect)
            ammo.draw(screen)
            gun.draw(screen)
            if len(ducks1) == 0:
                running = 0
                game_clock1 -= 60000
            time -= 1/60
            time_surface = font.render(f"{time:0.0f}", 1, (hunter_green))
            screen.blit(time_surface, (int(TS*8.75), 30))
            if time <= 0.0:
                running = 0
                lose.play()
                game_over = True
                while game_over:
                    screen.fill(dark_blue)
                    screen.blit(lost_surface, lost_rect)
                    screen.blit(end_subtitle_surface, end_subtitle_rect)
                    pygame.display.flip()
                    for e in pygame.event.get():
                        if e.type == pygame.QUIT or (e.type == pygame.KEYDOWN and e.key == pygame.K_SPACE):
                            running = 0
                            leave = 0
                            game_over = False
                            break
            pygame.display.flip()
    start2 = pygame.time.get_ticks()
    game_clock2 = pygame.time.get_ticks()
    if leave == 0:
        break
    #level two
    running = 1
    time2 = 45
    while running:
        while pygame.time.get_ticks() - start2 <= 3000:
            theme_music.play()
            screen.fill(hunter_green)
            screen.blit(level_two, level2_rect)
            pygame.display.flip()
        #stop music
        theme_music.stop()
        while pygame.time.get_ticks() - game_clock2 <= 48000 and running==1:
            clock.tick(60)
            screen.blit(bg, (0,0))
            events = pygame.event.get()
            for e in events:
                if e.type == pygame.QUIT:
                    running = 0
                    leave = 0
                    break
                gun.update(e)
            #kill both duck and ammo when collide
            hit = pygame.sprite.groupcollide(ducks2, ammo, True, True)
            if hit:
                quack.play()
            ducks2.update(screen)
            ammo.update(screen_rect)
            ammo.draw(screen)
            gun.draw(screen)
            if len(ducks2) == 0:
                running = 0
                game_clock2 -=45000
            time2 -= 1/60
            time2_surface = font.render(f"{time2:0.0f}", 1, (hunter_green))
            screen.blit(time2_surface, (int(TS*8.75), 30))
            if time2 <= 0.0:
                running = 0
                lose.play()
                game_over = True
                while game_over:
                    screen.fill(dark_blue)
                    screen.blit(lost_surface, lost_rect)
                    screen.blit(end_subtitle_surface, end_subtitle_rect)
                    pygame.display.flip()
                    for e in pygame.event.get():
                        if e.type == pygame.QUIT or (e.type == pygame.KEYDOWN and e.key == pygame.K_SPACE):
                            running = 0
                            leave = 0
                            game_over = False
                            break
            pygame.display.flip()
    start3 = pygame.time.get_ticks()
    game_clock3 = pygame.time.get_ticks()
    if leave == 0:
        break
    #level three
    running = 1
    time3 = 30
    while running:
        clock.tick(60)
        while pygame.time.get_ticks() - start3 <= 3000:
            theme_music.play()
            screen.fill(hunter_green)
            screen.blit(level_three, level3_rect)
            pygame.display.flip()
        #stop music
        theme_music.stop()
        while pygame.time.get_ticks() - game_clock3 <= 33000 and running==1:
            clock.tick(60)
            screen.blit(bg, (0,0))
            events = pygame.event.get()
            for e in events:
                if e.type == pygame.QUIT:
                    running = 0
                    leave = 0
                    break
                gun.update(e)
            #kill both duck and ammo when collide
            hit = pygame.sprite.groupcollide(ducks3, ammo, True, True)
            if hit:
                quack.play()
            ducks3.update(screen)
            ammo.update(screen_rect)
            ammo.draw(screen)
            gun.draw(screen)
            if len(ducks3) == 0:
               running = 0
               game_clock3 -= 30000
            time3 -= 1/60
            time3_surface = font.render(f"{time3:0.0f}", 1, (hunter_green))
            screen.blit(time3_surface, (int(TS*8.75), 30))
            if time3 <= 0.0:
                running = 0
                lose.play()
                game_over = True
                while game_over:
                    screen.fill(dark_blue)
                    screen.blit(lost_surface, lost_rect)
                    screen.blit(end_subtitle_surface, end_subtitle_rect)
                    pygame.display.flip()
                    for e in pygame.event.get():
                        if e.type == pygame.QUIT or (e.type == pygame.KEYDOWN and e.key == pygame.K_SPACE):
                            running = 0
                            leave = 0
                            game_over = False
                            break
            pygame.display.flip()
    if leave == 0:
        break
    running = 1
    while running:
        screen.blit(bg_main, (0,0))
        theme_music.play()
        screen.blit(end_surface, end_rect)
        screen.blit(end_subtitle_surface, end_subtitle_rect)
        pygame.display.flip()
                
        events = pygame.event.get()
        for e in events:
            if e.type == pygame.QUIT:
                running = 0
                leave = 0
            elif e.type == pygame.KEYDOWN:
                if e.key == pygame.K_SPACE:
                    running = 0
                    leave = 0
pygame.quit()
