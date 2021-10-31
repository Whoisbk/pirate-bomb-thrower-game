import pygame
from pygame import mixer
import os
import random
import player
import Enemy
import projectiles
pygame.init()
pygame.font.init()
mixer.init()


SCREEN_WIDTH = 600
SCREEN_HEIGHT = 400

WIN = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
pygame.display.set_caption("Bomb Thrower")

FPS = 60
#SOUND
pygame.mixer.music.load(os.path.join("Assets","Fluffing-a-Duck.mp3"))
pygame.mixer.music.set_volume(0.6)
pygame.mixer.music.play(-1,0.0)
hit_sfx = pygame.mixer.Sound(os.path.join("Assets","88499787.mp3"))
hit_sfx.set_volume(0.2)
#IMAGES
bg_image = pygame.image.load(os.path.join("Assets","War.png"))

#COLORS
WHITE = (255,255,255)
BLACK = (0,0,0)

#GAME VARIABLES
MAX_ENEMIES = 3 #NUMBER OF ENEMIES ON SCREEN
game_over = False
fade_counter = 0
score = 0 

#FONTS
font = pygame.font.SysFont("Lucida Sans",60)
font_small = pygame.font.SysFont("comicsans",35)

def draw_win():
    WIN.blit(bg_image,(0,0))
    

def draw_text(message,x,y,font,color):
    message_text = font.render(message,True,color)
    WIN.blit(message_text,(x,y))

#INSTANCES
pirate = player.Pirate(100,300,"player",WIN)

enemies = []
bombs = []

#MAIN GAME LOOP
run = True
clock = pygame.time.Clock()
while run:

    clock.tick(FPS)
    if game_over != True:
        #DRAW WINDOW
        draw_win()

        #DRAW PLAYER
        pirate.update()
        pirate.move()
        pirate.draw()
        #CREATE ENEMY
        if len(enemies) < 3:#IF ENEMIES LENGTH IS SMALLER THEN 3 THEN CREATE ENEMY
            e_x =random.randint(SCREEN_WIDTH,900)
            e_y = random.randint(100,300)
            enemy = Enemy.Enemy(e_x,e_y,f'2-Enemy-Big Guy',WIN)
            enemies.append(enemy)

        #DRAW ENEMY
        for enemy in enemies:
            enemy.update()
            enemy.move()
            enemy.draw()
            #CHECK GAME OVER
            if enemy.rect.x < 50:
                game_over = True
            if enemy.rect.colliderect(pirate.rect):
                pirate.Death()
                game_over = True
        
        #CREATE BOMBS
        key_pressed = pygame.key.get_pressed()
        if key_pressed[pygame.K_LCTRL] and len(bombs) == 0:#IF bombs LENGTH IS SMALLER THEN 1 THEN CREATE BOMB
            bomb = projectiles.Bomb(pirate.rect.centerx + 35,pirate.rect.centery + 10,f'1-BOMB',WIN)
            bombs.append(bomb)

        #DRAW BOMB 
        for bomb in bombs:
            bomb.move()
            bomb.update()
            bomb.draw()

            if bomb.rect.x > SCREEN_WIDTH :
                bombs.remove(bomb)

            if enemy.rect.colliderect(bomb.rect):
                    score +=1
                    hit_sfx.play()
                    bombs.remove(bomb)  
                    enemies.remove(enemy)
        draw_text(f'score: {score}',SCREEN_WIDTH//2 - 20,10,font_small,WHITE)

    else:
        #FADE EFFECT
        if fade_counter < SCREEN_WIDTH:
            fade_counter += 5
            pygame.draw.rect(WIN,BLACK,(0,0,fade_counter,SCREEN_HEIGHT//2))
            pygame.draw.rect(WIN,BLACK,(SCREEN_WIDTH - fade_counter,SCREEN_HEIGHT//2,fade_counter,SCREEN_HEIGHT//2))
        else:
            draw_text(f"GAME OVER!",SCREEN_WIDTH//2-175,SCREEN_HEIGHT//2 -60,font,WHITE)
            draw_text(f"SCORE: {score} ",SCREEN_WIDTH//2-60,SCREEN_HEIGHT//2+ 50,font_small,WHITE)
            draw_text('PRESS ENTER TO PLAY AGAIN',SCREEN_WIDTH//2 - 180,SCREEN_HEIGHT-90,font_small,WHITE)
            key_pressed = pygame.key.get_pressed()
            #RESET GAME VARIABLES
            if key_pressed[pygame.K_SPACE]:
                game_over = False
                fade_counter = 0
                enemy.rect.x -= 3
                score = 0
                #RESET PLAYER
                pirate = player.Pirate(100,300,"player",WIN)
                #EMPTY ENEMY LIST
                enemies.clear()
                #RESET ENEMY POSITION
                enemy = Enemy.Enemy(600,300,f'2-Enemy-Big Guy',WIN)
                enemies.append(enemy)

    #EVENT HANDLER
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()

pygame.quit()

