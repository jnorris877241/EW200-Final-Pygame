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
duck_pic = r"duck_outline_target_white.png"
duck_pic_img = pygame.image.load(duck_pic)
duck_pic_img = pygame.transform.rotozoom(duck_pic_img, 20, 1.65)
bg_main = pygame.Surface(SIZE)
for x in range(0, WIDTH):
    for y in range(0, HEIGHT):
        bg_main.blit(wood_img, (x*TS, y*TS))


#load fonts
font = pygame.font.Font('Cinzel-ExtraBold.ttf', size = 120)
font2 = pygame.font.Font('Cinzel-ExtraBold.ttf', size = 45)
font3 = pygame.font.Font('Cinzel-ExtraBold.ttf', size = 25)
font4 = pygame.font.Font('Cinzel-ExtraBold.ttf', size = 80)
#make the main screen text
title_surface = font.render('Duck Hunt!',1, baltic_blue)
title_rect = title_surface.get_rect()
title_rect.center = (WIDTH/2, HEIGHT/2-70)
subtitle_surface = font2.render('press SPACEBAR to play', 1, hunter_green)
subtitle_rect = subtitle_surface.get_rect()
subtitle_rect.center = (WIDTH/2, HEIGHT/2+30)
directions_surface = font3.render('DIRECTIONS: \nshoot the ducks in all three levels. \npay attention to how many shots you have per round. \nuse the arrow keys to move the gun and mousepad to shoot. \nbest of luck!', 1, icy_blue)
directions_rect = directions_surface.get_rect()
directions_rect.center = (WIDTH/2, HEIGHT/2+180)
#level one text
level_one = font.render('LEVEL ONE', 1, icy_blue)
level1_rect = level_one.get_rect()
level1_rect.center = (WIDTH/2, HEIGHT/2-40)
level1_shots = font2.render('10 shots to kill 6 ducks', 1, pale_sky)
level1_shots_rect = level1_shots.get_rect()
level1_shots_rect.center = (WIDTH/2, HEIGHT/2+40)
#level two text
level_two = font.render('LEVEL TWO', 1, icy_blue)
level2_rect = level_two.get_rect()
level2_rect.center = (WIDTH/2, HEIGHT/2-40)
level2_shots = font2.render('14 shots to kill 10 ducks', 1, pale_sky)
level2_shots_rect = level2_shots.get_rect()
level2_shots_rect.center = (WIDTH/2, HEIGHT/2+40)
#level three text
level_three = font.render('LEVEL THREE', 1, icy_blue)
level3_rect = level_three.get_rect()
level3_rect.center = (WIDTH/2, HEIGHT/2-40)
level3_shots = font2.render('18 shots to kill 15 ducks', 1, pale_sky)
level3_shots_rect = level3_shots.get_rect()
level3_shots_rect.center = (WIDTH/2, HEIGHT/2+40)
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
theme_music.set_volume(0.6)
lose = pygame.mixer.Sound('lose.mp3')
lose.set_volume(0.8)

#main game background
bg = make_bg(SIZE, TS)
#ammo sprite group
ammo = pygame.sprite.Group()
#ammo left to append to to print on screen
ammo_shot = 0
#make the gun
gun = Gun(ammo)
#ducks in game
ducks1 = pygame.sprite.Group()
ducks2 = pygame.sprite.Group()
ducks3 = pygame.sprite.Group()
#load dead duck images
dead_duck = r"duck_outline_back.png"
dead_duck_img = pygame.image.load(dead_duck)
dead_duck_img = pygame.transform.scale_by(dead_duck_img, 0.8)
#dead ducks list to append to to blit the ducks
dead_ducks = []
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
    #play theme music repeating
    theme_music.play(-1)
    while running:
        screen.blit(bg_main, (0,0))
        screen.blit(duck_pic_img, (115, 25))
        #blit the title to the screen
        screen.blit(title_surface,title_rect)
        screen.blit(subtitle_surface,subtitle_rect)
        screen.blit(directions_surface, directions_rect)
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
        #level one intro screen displayed for 3 seconds
        while pygame.time.get_ticks() - start1 <= 3000:
            screen.fill(hunter_green)
            screen.blit(level_one, level1_rect)
            screen.blit(level1_shots, level1_shots_rect)
            pygame.display.flip()
        #level one runs for 63 seconds, making the level 60 seconds
        while pygame.time.get_ticks() - game_clock1 <= 63000 and running==1:
            clock.tick(60)
            screen.blit(bg, (0,0))
            events = pygame.event.get()
            for e in events:
                if e.type == pygame.QUIT:
                        running = 0
                        leave = 0
                        break
                ammo1 = len(ammo)
                gun.update(e)
                #check ammo after gun.update to count bullets
                if len(ammo) > ammo1:
                    ammo_shot += 1
            #kill both duck and ammo when collide
            hit = pygame.sprite.groupcollide(ducks1, ammo, True, True)
            if hit:
                quack.play()
                for duck in hit:
                    #append the dead ducks position to the empty list
                    dead_ducks.append(duck.rect.copy())
            for position in dead_ducks:
                screen.blit(dead_duck_img, position)
                position.y += 5
            ducks1.update(screen)
            ammo.update(screen_rect)
            ammo.draw(screen)
            gun.draw(screen)
            #keeping track of ammo
            if ammo_shot >= 11:
                running = 0
                theme_music.stop()
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
            if len(ducks1) == 0:
                running = 0
                game_clock1 -= 60000
            time -= 1/60
            time_surface = font4.render(f"{time:0.0f}", 1, (hunter_green))
            screen.blit(time_surface, (int(TS*9.5), 60))
            ammo_surface = font4.render(f"{ammo_shot}", 1, dark_blue)
            screen.blit(ammo_surface, (int(TS*0.5), 60))
            if time <= 0.0:
                running = 0
                theme_music.stop()
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
    #make sure dead ducks list is empty from level 1
    dead_ducks.clear()
    #reset ammo count to 0
    ammo_shot = 0
    time2 = 45
    while running:
        #level two intro screen running for 3 seconds
        while pygame.time.get_ticks() - start2 <= 3000:
            screen.fill(hunter_green)
            screen.blit(level_two, level2_rect)
            screen.blit(level2_shots, level2_shots_rect)
            pygame.display.flip()
        #level two runs for 48 seconds, making the level 45 seconds long
        while pygame.time.get_ticks() - game_clock2 <= 48000 and running==1:
            clock.tick(60)
            screen.blit(bg, (0,0))
            events = pygame.event.get()
            for e in events:
                if e.type == pygame.QUIT:
                    running = 0
                    leave = 0
                    break
                ammo1 = len(ammo)
                gun.update(e)
                #check ammo after gun.update to count bullets
                if len(ammo) > ammo1:
                    ammo_shot += 1
            #kill both duck and ammo when collide
            hit = pygame.sprite.groupcollide(ducks2, ammo, True, True)
            if hit:
                quack.play()
                for duck in hit:
                    #append the dead ducks position to the empty list
                    dead_ducks.append(duck.rect.copy())
            for position in dead_ducks:
                screen.blit(dead_duck_img, position)
                position.y += 5
            ducks2.update(screen)
            ammo.update(screen_rect)
            ammo.draw(screen)
            gun.draw(screen)
            #counting ammo
            if ammo_shot >= 15:
                running = 0
                theme_music.stop()
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
            if len(ducks2) == 0:
                running = 0
                game_clock2 -=45000
            time2 -= 1/60
            time2_surface = font4.render(f"{time2:0.0f}", 1, (hunter_green))
            screen.blit(time2_surface, (int(TS*9.5), 60))
            ammo_surface = font4.render(f"{ammo_shot}", 1, dark_blue)
            screen.blit(ammo_surface, (int(TS*0.5), 60))
            if time2 <= 0.0:
                running = 0
                theme_music.stop()
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
    #make sure dead ducks list is empty from level 2
    dead_ducks.clear()
    running = 1
    #reset ammo count
    ammo_shot = 0
    time3 = 30
    while running:
        clock.tick(60)
        #level three intro screen for 3 seconds
        while pygame.time.get_ticks() - start3 <= 3000:
            screen.fill(hunter_green)
            screen.blit(level_three, level3_rect)
            screen.blit(level3_shots, level3_shots_rect)
            pygame.display.flip()
        #level three level runs for 33 seconds, so play level for 30s
        while pygame.time.get_ticks() - game_clock3 <= 33000 and running==1:
            clock.tick(60)
            screen.blit(bg, (0,0))
            events = pygame.event.get()
            for e in events:
                if e.type == pygame.QUIT:
                    running = 0
                    leave = 0
                    break
                ammo1 = len(ammo)
                gun.update(e)
                #check ammo after gun.update to count bullets
                if len(ammo) > ammo1:
                    ammo_shot += 1
            #kill both duck and ammo when collide
            hit = pygame.sprite.groupcollide(ducks3, ammo, True, True)
            if hit:
                quack.play()
                for duck in hit:
                    #append the dead ducks position to the empty list
                    dead_ducks.append(duck.rect.copy())
            for position in dead_ducks:
                screen.blit(dead_duck_img, position)
                position.y += 5
            ducks3.update(screen)
            ammo.update(screen_rect)
            ammo.draw(screen)
            gun.draw(screen)
            #tracking ammo
            if ammo_shot >= 19:
                running = 0
                theme_music.stop()
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
            if len(ducks3) == 0:
               running = 0
               game_clock3 -= 30000
            time3 -= 1/60
            time3_surface = font4.render(f"{time3:0.0f}", 1, (hunter_green))
            screen.blit(time3_surface, (int(TS*9.5), 60))
            ammo_surface = font4.render(f"{ammo_shot}", 1, dark_blue)
            screen.blit(ammo_surface, (int(TS*0.5), 60))
            if time3 <= 0.0:
                running = 0
                theme_music.stop()
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
