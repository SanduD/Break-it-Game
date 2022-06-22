import pygame
from pygame.locals import *
from Wall import wall 
from Paddle import paddle
import math
pygame.init()

Gri=(128,128,128)
Orange=(255,69,0)
Maro=(139,69,19)
Alb=(255,255,255)
Verde=(0,255,0)
Galben=(255,255,0)
Negru=(0,0,0)

cols=8
rows=6
count=0

score=0

bigger=False
smaller=True

speed_state=0
special_state=0
game_over=0
live_ball=False
ball_x=0
ball_y=0

speed_ok=False

#bullet
bulletImg=pygame.image.load('bullet.png')
bulletX=0
bulletY=575
bulletY_change=5
bullet_state="ready"
nr_bullet=0


#Ball class
class ball():
    def __init__(self,x,y):
        self.reset(x,y)
  
    def move(self):

        wall_destroyed=1
        row_count=0
        distance=10

        for row in wall.blocks:
            item_count=0

            for item in row:

                if self.rect.colliderect(item[0]):
                    
                    global score,bulletY
                    
                    if abs(self.rect.bottom-item[0].top)<distance and self.speed_y>0:
                        self.speed_y*=-1
                        if wall.blocks[row_count][item_count][1]<=1  and wall.blocks[row_count][item_count][1]!=0.9 :
                            score+=1

                    if abs(self.rect.top-item[0].bottom)<distance and self.speed_y<0:
                        self.speed_y*=-1
                        if wall.blocks[row_count][item_count][1]<=1  and wall.blocks[row_count][item_count][1]!=0.9:
                            score+=1
                    
                    if abs(self.rect.right-item[0].left)<distance and self.speed_x>0:
                        self.speed_x*=-1
                        if wall.blocks[row_count][item_count][1]<=1  and wall.blocks[row_count][item_count][1]!=0.9:
                            score+=1

                    if abs(self.rect.left-item[0].right)<distance and self.speed_x<0:
                        self.speed_x*=-1
                        if wall.blocks[row_count][item_count][1]<=1 and wall.blocks[row_count][item_count][1]!=0.9:
                            score+=1
                   
                    global special_state

                    if wall.blocks[row_count][item_count][1]==0.9:
                        special_state+=1
                        score+=1
                       
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

    def draw(self):
        pygame.draw.circle(screen,Verde,(self.rect.x+self.ball_rad,self.rect.y+self.ball_rad),self.ball_rad)
        pygame.draw.circle(screen,Gri,(self.rect.x+self.ball_rad,self.rect.y+self.ball_rad),self.ball_rad,2)  

    def reset(self,x,y):
        self.ball_rad=10
        self.x=x-self.ball_rad
        self.y=y

        global speed_ok

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
                self.speed_x=3
            else:
                self.speed_x=-3

            if self.speed_y>0:
                self.speed_y=3
            else:
                self.speed_y=-3
            distance=15
        elif speed_state==2:
            
            if self.speed_x>0:
                self.speed_x=4
            else:
                self.speed_x=-4

            if self.speed_y>0:
                self.speed_y=4
            else:
                self.speed_y=-4
            distance=20
        

#create wall
wall=wall()
wall.create_wall()

#create paddle
paddle=paddle()

#create ball
ball=ball(paddle.x+(paddle.width//2),paddle.y-paddle.height)

screen=pygame.display.set_mode((600,600))

background=pygame.image.load('background.png')

#title and icon
pygame.display.set_caption("Break-it Game")
icon=pygame.image.load('icon.png')
pygame.display.set_icon(icon)

running=True
#clock=how fast screen updates
clock=pygame.time.Clock()

pause_state=False

def display_text(live_ball):
    if live_ball==False:
        if game_over==0:
            font=pygame.font.Font(None,34)
            text=font.render("Apasa SPACE pentru a incepe jocul.",1,Alb)
            screen.blit(text,(100,300))
        elif game_over==1:
            font=pygame.font.Font(None,34)
            text=font.render("Felicitari! Ai castigat",1,Alb)
            screen.blit(text,(100,300))
            text=font.render("Apasa SPACE pentru a juca din nou!",1,Alb)
            screen.blit(text,(100,350))
        elif game_over==-1:
            font=pygame.font.Font(None,34)
            text=font.render("Ai pierdut...",1,Alb)
            screen.blit(text,(225,300))
            text=font.render("Apasa SPACE pentru a juca din nou!",1,Alb)
            screen.blit(text,(100,350))

def fire_bullet(x,y):
    global bullet_state
    bullet_state="fire"
    screen.blit(bulletImg,(x-16,y))

def isCollision(bulletX,bulletY,wallX,wallY):
    distance=math.sqrt((math.pow((wallX-bulletX),2))+(math.pow((wallY-bulletY),2)))
    
    if distance<30:
        return True
        
while running:
    screen.blit(background,(0,0))
    wall.draw_wall(screen)

    paddle.draw(screen)
   
    ball.draw()

    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_x:
                running=False
            if event.key==pygame.K_p:
                if pause_state==False:
                    pause_state=True
                else:
                    pause_state=False
            if event.key==pygame.K_UP:
                speed_state+=1
                speed_ok=True
            
                ball.reset(ball_x,ball_y)
            if event.key==pygame.K_DOWN and speed_state>=1:
                speed_state-=1
                ball.reset(ball_x,ball_y)
            
            if event.key==pygame.K_f:
                if bullet_state is "ready" and nr_bullet<5 and live_ball==True and (special_state==3 or special_state==1):
                    fire_bullet(bulletX,bulletY)
                    nr_bullet+=1
                

    if pause_state==True and live_ball==True:
        font=pygame.font.Font(None,34)
        text=font.render("Pauza!",1,Alb)
        screen.blit(text,(270,300))
        text=font.render("Apasa P pentru a relua jocul.",1,Alb)
        screen.blit(text,(150,350))
    
    if pause_state==False:
        if live_ball==True:
            bulletX=paddle.move(speed_state,special_state,bullet_state)
            game_over=ball.move()
            if game_over!=0:
                live_ball=False

    display_text(live_ball)


    key=pygame.key.get_pressed()
    
    
    if key[pygame.K_SPACE]==True and live_ball==False :
        live_ball=True
        speed_state=0
        ball.reset(paddle.x+(paddle.width//2),paddle.y-paddle.height)
        paddle.reset()
        wall.create_wall()
        score=0
        special_state=0
        nr_bullet=0
    
    font=pygame.font.Font(None,34)
    text=font.render("Score: "+str(score),1,Alb)
    screen.blit(text,(20,570))

    
    row_count=0
    for row in wall.blocks:
        item_count=0
        for item in row:
            collision=isCollision(bulletX,bulletY,wall.width*item_count,wall.height*row_count)

            if collision==True and wall.blocks[row_count][item_count][0]!=(0,0,0,0):
                bulletY=575
                wall.blocks[row_count][item_count][0]=(0,0,0,0)
                bullet_state="ready"
                score+=1
            item_count+=1
        row_count+=1

    if bullet_state is "fire":
        fire_bullet(bulletX,bulletY)
        bulletY-=bulletY_change

    if(bulletY<=0):
        bullet_state="ready"
        bulletY=575
    
    pygame.display.update()
    clock.tick(200)
pygame.quit()
    