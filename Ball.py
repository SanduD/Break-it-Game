import pygame
from Wall import wall 
from Paddle import paddle
from pygame.locals import *

wall=wall()

paddle=paddle()

Gri=(128,128,128)
Verde=(0,255,0)

class ball():
    def __init__(self,x,y,speed_state,speed_ok,create_wall_ok):
        if(create_wall_ok==True):
            wall.create_wall()
            create_wall_ok=False
        self.reset(x,y,speed_state,speed_ok)
  
    def move(self,special_state,score):
        wall_destroyed=1
        row_count=0
        distance=10
        for row in wall.blocks:
            item_count=0

            for item in row:
                if self.rect.colliderect(item[0]):
     
                    if abs(self.rect.bottom-item[0].top)<distance and self.speed_y>0:
                        self.speed_y*=-1
                        if wall.blocks[row_count][item_count][1]<=1 and wall.blocks[row_count][item_count][1]!=0 and wall.blocks[row_count][item_count][1]!=0.9 :
                            score+=1

                    if abs(self.rect.top-item[0].bottom)<distance and self.speed_y<0:
                        self.speed_y*=-1
                        if wall.blocks[row_count][item_count][1]<=1 and wall.blocks[row_count][item_count][1]!=0 and wall.blocks[row_count][item_count][1]!=0.9:
                            score+=1
                    
                    if abs(self.rect.right-item[0].left)<distance and self.speed_x>0:
                        self.speed_x*=-1
                        if wall.blocks[row_count][item_count][1]<=1 and wall.blocks[row_count][item_count][1]!=0 and wall.blocks[row_count][item_count][1]!=0.9:
                            score+=1

                    if abs(self.rect.left-item[0].right)<distance and self.speed_x<0:
                        self.speed_x*=-1
                        if wall.blocks[row_count][item_count][1]<=1 and wall.blocks[row_count][item_count][1]!=0 and wall.blocks[row_count][item_count][1]!=0.9:
                            score+=1
                   
                    

                    if wall.blocks[row_count][item_count][1]==0.9:
                        special_state+=1
                        score+=1
                        if special_state==1:
                            bigger=False

                        if special_state!=1:
                            smaller=False
                        if special_state>3:
                            special_state=0

                        self.ok=True
                        print(special_state)
                    
                    if special_state==2 and self.ok==True:
    
                        if row_count>=1:
                            if wall.blocks[row_count-1][item_count][1]<3 and wall.blocks[row_count-1][item_count][1]!=0:
                                wall.blocks[row_count-1][item_count][1]=0
                                wall.blocks[row_count-1][item_count][0]=(0,0,0,0)
                                score+=1

                            if item_count<=6 and wall.blocks[row_count-1][item_count+1][1]<3 and wall.blocks[row_count-1][item_count+1][1]!=0:
                                wall.blocks[row_count-1][item_count+1][1]=0
                                wall.blocks[row_count-1][item_count+1][0]=(0,0,0,0)
                                score+=1
                            
                            if item_count>=1 and wall.blocks[row_count-1][item_count-1][1]<3 and wall.blocks[row_count-1][item_count-1][1]!=0 :
                                wall.blocks[row_count-1][item_count-1][1]=0
                                wall.blocks[row_count-1][item_count-1][0]=(0,0,0,0)
                                score+=1
                   
                        if item_count>=1 and wall.blocks[row_count][item_count-1][1]<3 and wall.blocks[row_count][item_count-1][1]!=0:
                            wall.blocks[row_count][item_count-1][1]!=0
                            wall.blocks[row_count][item_count-1][0]=(0,0,0,0)
                            score+=1

                        if item_count<=6 and wall.blocks[row_count][item_count+1][1]<3 and wall.blocks[row_count][item_count+1][1]!=0:
                            wall.blocks[row_count][item_count+1][1]=0
                            wall.blocks[row_count][item_count+1][0]=(0,0,0,0)
                            score+=1
                        
                        if row_count<=4:
                            if wall.blocks[row_count+1][item_count][1]<3 and wall.blocks[row_count+1][item_count][1]!=0:
                                wall.blocks[row_count+1][item_count][1]=0
                                wall.blocks[row_count+1][item_count][0]=(0,0,0,0)
                                score+=1

                            if item_count>=1 and wall.blocks[row_count+1][item_count-1][1]<3 and wall.blocks[row_count+1][item_count-1][1]!=0:
                                wall.blocks[row_count+1][item_count-1][1]=0
                                wall.blocks[row_count+1][item_count-1][0]=(0,0,0,0)
                                score+=1

                            if item_count<=6 and wall.blocks[row_count+1][item_count+1][1]<3 and wall.blocks[row_count+1][item_count+1][1]!=0:
                                wall.blocks[row_count+1][item_count+1][1]=0
                                wall.blocks[row_count+1][item_count+1][0]=(0,0,0,0)
                                score+=1

                    self.ok=False
                    if wall.blocks[row_count][item_count][1]>1:
                        wall.blocks[row_count][item_count][1]-=1
                    else:
                        wall.blocks[row_count][item_count][0]=(0,0,0,0)
                
                if wall.blocks[row_count][item_count][1]<3:
                    wall_destroyed=0
                item_count+=1

            row_count+=1
        if wall_destroyed==1:
            self.game_over=1

        if self.rect.left<0 or self.rect.right>600:
            self.speed_x*=-1
        
        if self.rect.top<0:
            self.speed_y*=-1

        if self.rect.bottom>600:
            self.game_over=-1
        
        global ball_x,ball_y
        ball_y=(self.rect.bottom +self.rect.top)/2
        ball_x=(self.rect.left+self.rect.right)/2

        if self.rect.colliderect(paddle)==True:
            if abs(self.rect.bottom-paddle.rect.top)<distance and self.speed_y>0:
                self.speed_y*=-1
        
        self.rect.x+=self.speed_x
        self.rect.y+=self.speed_y

        return self.game_over

    def draw(self,screen):
        pygame.draw.circle(screen,Verde,(self.rect.x+self.ball_rad,self.rect.y+self.ball_rad),self.ball_rad)
        pygame.draw.circle(screen,Gri,(self.rect.x+self.ball_rad,self.rect.y+self.ball_rad),self.ball_rad,2)  

    def reset(self,x,y,speed_state,speed_ok):
        self.ball_rad=10
        self.x=x-self.ball_rad
        self.y=y

        if speed_ok==False:
            self.speed_x=2
            self.speed_y=-2

        if speed_state==0 and speed_ok==True:
            if self.speed_x>0:
                self.speed_x=2
            else:
                self.speed_x=-2
            if self.speed_y>0:
                self.speed_y=2
            else:
                self.speed_y=-2
            distance=10
        self.rect=Rect(self.x,self.y, self.ball_rad*2, self.ball_rad*2)
        self.game_over=0
        self.ok=False
        if speed_state==1:
            if self.speed_x>0:
                self.speed_x=4
            else:
                self.speed_x=-4
            if self.speed_y>0:
                self.speed_y=4
            else:
                self.speed_y=-4
            distance=15
        elif speed_state==2:
            
            if self.speed_x>0:
                self.speed_x=6
            else:
                self.speed_x=-6
            if self.speed_y>0:
                self.speed_y=6
            else:
                self.speed_y=-6
            distance=20
        