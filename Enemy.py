import pygame
import os

class Enemy(pygame.sprite.Sprite):
    def __init__(self,x,y,name,win):
        pygame.sprite.Sprite.__init__(self)
        self.name = name
        self.animation_List = [] 
        self.frame_index = 0
        self.update_time = pygame.time.get_ticks()
        self.action = 0
        self.flip = True
        self.width = 35
        self.height = 60
        self.win = win
        #Load Run animation
        temp_list = []#temporary list
        for i in range(1,14):#loop through spries and add them to the list
            img = pygame.image.load(os.path.join(f'Assets/{self.name}/2-Run',f'{i}.png'))
            temp_list.append(img)#add images to temporary list
        self.animation_List.append(temp_list)#add the temporary list with images in the animation list
        
        #Load Death animation
        temp_list = []#temporary list
        for i in range(1,6):#loop through spries and add them to the list
            img = pygame.image.load(os.path.join(f'Assets/{self.name}/9-Dead Hit',f'{i}.png'))
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
                self.Run()
        
    def Death(self):
        #set variables to death animation
        self.action = 1
        self.frame_index = 0
        self.update_time = pygame.time.get_ticks()


    def Run(self):
        #set variables to run animation
        self.action = 0
        self.frame_index = 0
        self.update_time = pygame.time.get_ticks()
    
    def move(self):
        dy = 0
        dx = 1
        self.rect.x -= dx
        self.rect.y += dy

    def draw(self):
        self.win.blit(pygame.transform.flip(self.image,True,False),(self.rect.x -25,self.rect.y -2))
        