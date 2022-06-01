import pygame
from pygame.locals import *
import signal, sys, os

pygame.init()


# code from https://www.geeksforgeeks.org/python-moving-an-object-in-pygame/

win = pygame.display.set_mode((640, 480))
  
pygame.display.set_caption("Undertale 2 Side Mockup")


health = 10

# object current co-ordinates 
x = 150
y = 240
x2 = 475
y2 = 240

# dimensions of the object 
width = 20
height = 20


wall1 = Rect(25,150,250,175)
wall2 = Rect(350,150,250,175)

bone = Rect(50,200,100,10)



  
# velocity / speed of movement
vel = 2.5
  
# Indicates pygame is running
run = True
  
# infinite loop 
while run:  
    pygame.time.delay(10)
      
    for event in pygame.event.get():
          

        if event.type == pygame.QUIT:
              
            run = False
    keys = pygame.key.get_pressed()




    if keys[pygame.K_LEFT] and x>0:
          
        # decrement in x co-ordinate
        x2 -= vel
          

    if keys[pygame.K_RIGHT] and x<500-width:
          
        # increment in x co-ordinate
        x2 += vel
         
   
    if keys[pygame.K_UP] and y>0:
          
        # decrement in y co-ordinate
        y2 -= vel
          
   
    if keys[pygame.K_DOWN] and y<500-height:
        # increment in y co-ordinate
        y2 += vel
        
    
    if keys[pygame.K_a] and x>0:
          
        # decrement in x co-ordinate
        x -= vel
          

    if keys[pygame.K_d] and x<500-width:
          
        # increment in x co-ordinate
        x += vel
         
   
    if keys[pygame.K_w] and y>0:
          
        # decrement in y co-ordinate
        y -= vel
          
   
    if keys[pygame.K_s] and y<500-height:
        # increment in y co-ordinate
        y += vel
              

    win.fill((0, 0, 0))
    
    player_rect = Rect(x, y, width, height)
    player_rect2 = Rect(x2, y2, width, height)
    
    
    pygame.draw.rect(win, (0,255,0), wall1, 10)
    pygame.draw.rect(win, (0,255,0), wall2, 10)
    
    pygame.draw.rect(win, (0,0,255), bone)



    pygame.draw.rect(win, (255, 0, 0), player_rect)
    pygame.draw.rect(win, (255, 0, 0), player_rect2)
    

    if pygame.Rect.colliderect(player_rect, bone):
        os.exit()
    
    if pygame.Rect.colliderect(player_rect2, bone):
        os.exit()
        
    if pygame.Rect.colliderect(player_rect, wall1) == False:
        x = 150
        y = 240
    
    if pygame.Rect.colliderect(player_rect2, wall2) == False:
        x2 = 475
        y2 = 240        
        

    
      
    # it refreshes the window
    pygame.display.update() 
  
pygame.quit()


