import pygame
import os
class Bomb(pygame.sprite.Sprite):
    def __init__(self,x,y,name,win):
        pygame.sprite.Sprite.__init__(self)
        self.name = name
        self.animation_List = [] 
        self.frame_index = 0
        self.update_time = pygame.time.get_ticks()
        self.action = 0
        self.flip = True
        self.width = 35
        self.height = 40
        self.win = win
        #Load Idle animation
        temp_list = []#temporary list
        for i in range(1,2):#loop through spries and add them to the list
            img = pygame.image.load(os.path.join(f'Assets/{self.name}/1-Bomb Off',f'{i}.png'))
            temp_list.append(img)#add images to temporary list
        self.animation_List.append(temp_list)#add the temporary list with images in the animation list
        
        #Load Timer animation
        temp_list = []#temporary list
        for i in range(1,10):#loop through spries and add them to the list
            img = pygame.image.load(os.path.join(f'Assets/{self.name}/2-Bomb On',f'{i}.png'))
            temp_list.append(img)#add images to temporary list
        self.animation_List.append(temp_list)#add the temporary list with images in the animation list

        #Load Explotion animation
        temp_list = []#temporary list
        for i in range(1,9):#loop through spries and add them to the list
            img = pygame.image.load(os.path.join(f'Assets/{self.name}/3-Explotion',f'{i}.png'))
            temp_list.append(img)#add images to temporary list
        self.animation_List.append(temp_list)#add the temporary list with images in the animation list

        self.image = self.animation_List[self.action][self.frame_index]
        self.rect = pygame.Rect(0,0,self.width,self.height)
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
            if self.action == 1:
                self.frame_index = len(self.animation_List[self.action]) - 1
            else:
                self.Idle()
            

    def timer(self):
        #set variables to timer animation
        self.action = 1
        self.frame_index = 0
        self.update_time = pygame.time.get_ticks()

    def Idle(self):
        #set variables to run animation
        self.action = 0
        self.frame_index = 0
        self.update_time = pygame.time.get_ticks()

    def explode(self):
        #set variables to run animation
        self.action = 2
        self.frame_index = 0
        self.update_time = pygame.time.get_ticks()
    def move(self):
        dx = 0
        dx += 10
        self.rect.x += dx

    def draw(self):
        self.win.blit(self.image,(self.rect.x,self.rect.y))
        