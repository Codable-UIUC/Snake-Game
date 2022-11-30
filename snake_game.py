# import pygame
# import sys
# import time
# import random

# class Snake_Game():
#     def init_window(self):
#         pygame.init()
#         dis=pygame.display.set_mode((800,600))
        
#         pygame.display.set_caption('Snake Game')
        
#         # blue=(0,0,255)
#         red=(255,0,0)
        
#         game_over=False
#         while not game_over:
#             for event in pygame.event.get():
#                 if event.type==pygame.QUIT:
#                     game_over=True
#             #pos can be randomized
#             inital_pos_size = [200,200,15,15] #x, y, width, height
#             pygame.draw.rect(dis,red,inital_pos_size)
#             pygame.display.update()

# game = Snake_Game()
# game.init_window()

import pygame
import sys
import time
import random

pygame.init()
d_width = 800
d_height = 600
dis=pygame.display.set_mode((d_width,d_height))

pygame.display.update()
pygame.display.set_caption('Snake Game')
# blue=(0,0,255)
red=(255,0,0)
framerate = pygame.time.Clock()
# Initialize Snake Position # 
 #pos can be randomized
x = random.randint(60, 700)
y = random.randint(60, 700)
inital_pos_size = [x,y,15,15] # x position, y position, width, height of snake body
move_x = 0
move_y = 0
game_over=False

def snake():
    global x, y, move_x, move_y, game_over, inital_pos_size
    x = move_x + x
    y = move_y + y
    dis.fill((0, 0, 0))
    
    pygame.draw.rect(dis, (255, 0, 0), [x, y, 15, 15])
    pygame.display.update()
    # pygame.draw.rect(dis, (255, 0, 0), [x, y, 15, 15])
    # pygame.display.update()
    # Close game # 
    if (x == 0 or y == 0 or x == 780 or y == 600): 
            pygame.quit()
            quit()

while not game_over:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            game_over=True
        if (event.type == pygame.KEYDOWN):
            if (event.key == pygame.K_LEFT):
                if (move_x != 15): # If previous move is not the opposite direction
                    move_x = -15
                    move_y = 0
            elif (event.key == pygame.K_RIGHT):
                if (move_x != -15): # If previous move is not the opposite direction
                    move_x = 15
                    move_y = 0
            elif (event.key == pygame.K_UP):
                move_x = 0
                if (move_y != 15): # If previous move is not the opposite direction
                    move_y = -15
            elif (event.key == pygame.K_DOWN):
                move_x = 0
                if (move_y != -15): # If previous move is not the opposite direction
                    move_y = 15
            else:
                continue
            snake()
    
    if x >= d_width or x < 0 or y >= d_height or y < 0:
        game_over = True
    if (not pygame.event.get()):
        snake()
    framerate.tick(10)
