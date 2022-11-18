import pygame
import sys
import time
import random

class Snake_Game():
    def init_window(self):
        pygame.init()
        dis=pygame.display.set_mode((800,600))
        
        pygame.display.set_caption('Snake Game')
        
        # blue=(0,0,255)
        red=(255,0,0)
        
        game_over=False
        while not game_over:
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    game_over=True
            #pos can be randomized
            inital_pos_size = [200,200,15,15] #x, y, width, height
            pygame.draw.rect(dis,red,inital_pos_size)
            pygame.display.update()

game = Snake_Game()
game.init_window()




def draw_single_block(snake_block,color):
    vertical_position = snake_block[0] * 15
    horizontal_position = snake_block[1] * 15
    pygame.draw.rect(dis, color, (vertical_position, horizontal_position, 15, 15)) 
draw_single_block([x1,y1],(0, 255, 0))
snake_list = [[200,203], [200,202], [200,201], [200,200]]
def draw_snake(snake_list):
    for snake_block in snake_list:
        draw_single_block(snake_block,green)
snake_list.append([x1,y1])
if(len(snake_list)>=4):
	del snake_list[0]