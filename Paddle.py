import pygame
from pygame.locals import *

Gri=(128,128,128)
Verde=(0,255,0)
class paddle():
    def __init__(self):
        self.reset()
    
    def move(self,speed_state,special_state,bullet_state):
        self.direction=0
        #global speed_state

        if speed_state==1:
            self.speed=5
        if speed_state==2:
            self.speed=7
        
        global bulletX
        if bullet_state is "ready":
            bulletX=(self.rect.left+self.rect.right)/2


        if special_state==1 and self.bigger==False:
            self.width=200
            self.rect=Rect(self.x,self.y,self.width,self.height)
            self.bigger=True
        
        if special_state>=2 and self.smaller==False:
            self.width=100
            self.rect=Rect(self.x,self.y,self.width,self.height)
            self.smaller=True
        
        
        key=pygame.key.get_pressed()
        
        if key[pygame.K_LEFT] and self.rect.left>0:
            self.rect.x-=self.speed
            

        if key[pygame.K_RIGHT] and self.rect.right<600:
            self.rect.x+=self.speed
            
        return bulletX

    def draw(self,screen):
        pygame.draw.rect(screen,Verde,self.rect)   
        pygame.draw.rect(screen,Gri,self.rect,3)
    
    def reset(self):
        self.height=20
        self.width=100
        self.bigger=False
        self.smaller=False
        self.x=290
        self.y=575
        self.speed=3
        self.rect=Rect(self.x,self.y,self.width,self.height)