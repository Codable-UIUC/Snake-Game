import pygame
import sys
import time
import random

class Snake_Game():
    def __init__(self) -> None:
        self.x = random.randint(50, 750)
        self.y = random.randint(50, 550)
        self.x_update = 0
        self.y_update = 0

    def init_window(self):
        pygame.init()
        dis=pygame.display.set_mode((800,600))
        
        pygame.display.set_caption('Snake Game')
        
        #white = (255, 255, 255)
        black = (0, 0, 0)
        #red=(255,0,0)
        #blue=(0,0,255)
        green = (0,255, 0)

        game_over = False

        while not game_over:
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    game_over=True
                self.handle_direction(event)    
            
            inital_pos_size = [self.x,self.y,30,30] #x, y, width, height

            self.update_direction()

            if self.is_bound(): 
                game_over = True

            dis.fill(black)
            pygame.draw.rect(dis,green,inital_pos_size)
            pygame.display.update()

    def handle_direction(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT: 
                self.x_update, self.y_update = -3, 0
            elif event.key == pygame.K_RIGHT: 
                self.x_update, self.y_update = 3, 0
            elif event.key == pygame.K_UP: 
                self.x_update, self.y_update = 0, -3
            elif event.key == pygame.K_DOWN: 
                self.x_update, self.y_update = 0, 3

    def update_direction(self):
        self.x += self.x_update
        self.y += self.y_update

    def is_bound(self):
        return self.x < 1 or self.y < 1 or self.x > 770 or self.y > 570

game = Snake_Game()
game.init_window()

