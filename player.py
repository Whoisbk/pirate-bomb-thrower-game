import pygame
import os

class Pirate():

    def __init__(self,x,y,name,win):
        self.name = name
        self.animation_List = [] 
        self.frame_index = 0
        self.update_time = pygame.time.get_ticks()
        self.action = 0
        self.win = win
        #Load Idle animation
        temp_list = []#temporary list
        for i in range(1,27):#loop through spries and add them to the list
            img = pygame.image.load(os.path.join(f'Assets/{self.name}/1-Idle',f'{i}.png'))
            temp_list.append(img)#add images to temporary list
        self.animation_List.append(temp_list)#add the temporary list with images in the animation list

        #Load Run animation
        temp_list = []#temporary list
        for i in range(8,15):#loop through spries and add them to the list
            img = pygame.image.load(os.path.join(f'Assets/{self.name}/2-Run',f'{i}.png'))
            temp_list.append(img)#add images to temporary list
        self.animation_List.append(temp_list)#add the temporary list with images in the animation list
        
        #Load Death animation
        temp_list = []#temporary list
        for i in range(1,7):#loop through spries and add them to the list
            img = pygame.image.load(os.path.join(f'Assets/{self.name}/8-Dead Hit',f'{i}.png'))
            temp_list.append(img)#add images to temporary list
        self.animation_List.append(temp_list)#add the temporary list with images in the animation list

        self.image = self.animation_List[self.action][self.frame_index]
        self.rect = self.image.get_rect()
        self.rect.center = (x,y)

    def update(self):
        animation_cooldown = 100
        #update image
        self.image = self.animation_List[self.action][self.frame_index]
        #if he current and the last time an image loaded is bigger then 100 the load next animation
        if pygame.time.get_ticks() - self.update_time > animation_cooldown:
            self.update_time = pygame.time.get_ticks()
            self.frame_index += 1#update the index to the next image
        #if the animation has run out the restet
        if self.frame_index >= len(self.animation_List[self.action]):
            if self.action == 2:
                self.frame_index = len(self.animation_List[self.action]) - 1
            else:
                self.Idle()


    def Idle(self):
        #set variables to idle animation
        self.action = 0
        self.frame_index = 0
        self.update_time = pygame.time.get_ticks()
    
    def Death(self):
        #set variables to death animation
        self.action = 2
        self.frame_index = 0
        self.update_time = pygame.time.get_ticks()

    def Run(self):
        #set variables to run animation
        self.action = 1
        self.frame_index = 0
        self.update_time = pygame.time.get_ticks()
    
    def move(self):
        dy = 0
        dx = 0

        key_pressed = pygame.key.get_pressed()
        if key_pressed[pygame.K_UP]:
            dy -= 2
            self.Run()
        if key_pressed[pygame.K_DOWN]:
            dy += 2
            self.Run()
        
        #COLLISION WITH GROUND
        if self.rect.bottom + dy > 340:
            dy = 0

        #COLLISION WITH SKY
        if self.rect.top + dy < 100:
            dy = 0

        self.rect.x += dx
        self.rect.y += dy

    def draw(self):
        self.win.blit(self.image,self.rect)