import pygame

Gri=(128,128,128)
Orange=(255,69,0)
Maro=(139,69,19)
Alb=(255,255,255)
Verde=(0,255,0)
Galben=(255,255,0)
Negru=(0,0,0)

cols=8
rows=6

class wall():
    def __init__(self):
        self.width=600/cols
        self.height=40
    
    def create_wall(self):
        self.blocks=[]
        
        block_individual=[]
        for row in range(rows):
            block_row=[]
            for col in range(cols):
                
                block_x=col*self.width
                block_y=row*self.height
                rect=pygame.Rect(block_x,block_y,self.width,self.height)
                
                if row==0:
                    strenght=999
                if row==1 and col<4:
                    strenght=1
                elif row==1 and col>=4:
                    strenght=2
                
                if row==2 and col<4:
                    strenght=2
                elif row==2 and col>=4:
                    strenght=1
                
                if row==3:
                    strenght=2
                if row==4:
                    strenght=1

                if row==5 and col<4:
                    strenght=2
                elif row==5 and col>=4:
                    strenght=1

                if (col==2 and row==3) or (col==6 and row==5) or( col==6 and row==3) or (col==4 and row==4) or (col==1 and row==4):
                    strenght=999
                
                if(col==3 and row==5) or (col==7 and row==5)  or (row ==5 and col==1) or (row ==3 and col==3) or (row ==2 and col==4) or (row ==3 and col==1) or (row ==3 and col==7):
                    strenght=0.9

                
                block_individual=[rect,strenght]
                block_row.append(block_individual)
            
            self.blocks.append(block_row)
    
    def draw_wall(self,screen):
        for row in self.blocks:
            for block in row:
                
                if block[1]>3:
                    block_color=Gri
                elif block[1]==2:
                    block_color=Maro
                elif block[1]==1:
                    block_color=Orange
                elif block[1]==0.9:
                    block_color=Verde
                pygame.draw.rect(screen,block_color,block[0])
                pygame.draw.rect(screen,Negru,(block[0]),5)
