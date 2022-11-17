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