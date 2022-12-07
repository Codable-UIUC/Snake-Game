import pygame
import sys
import time
import random

pygame.init()

d_width = 600
d_height = 400
snake_block = 10

dis = pygame.display.set_mode((d_width, d_height))
pygame.display.set_caption('Snake Game')
# blue=(0,0,255)
blue = (0, 0, 255)
red = (255, 0, 0)
black = (0, 0, 0)
framerate = pygame.time.Clock()

# main game loop
game_over = False

x = d_width / 2
y = d_height / 2

move_x = 0
move_y = 0

applex = round(random.randrange(0, d_width - snake_block) / 10.0) * 10.0
appley = round(random.randrange(0, d_width - snake_block) / 10.0) * 10.0



def main_game():
    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    move_x = -snake_block
                    move_y = 0
                elif event.key == pygame.K_RIGHT:
                    move_x = snake_block
                    move_y = 0
                elif event.key == pygame.K_UP:
                    move_y = -snake_block
                    move_x = 0
                elif event.key == pygame.K_DOWN:
                    move_y = snake_block
                    move_x = 0
        
        #body growing
        snake_pos = [x,y]
        snake_body = [[x-10, y],[x-20,y],[x-30,y],[x-40,y]]
        apple_pos = [applex, appley]
        apple_spawn = True

        snake_body.insert(0, list(snake_pos))
        if snake_pos[0] == apple_pos[0] and snake_pos[1] == apple_pos[1]:
            score += 10
            apple_spawn = False
        else:
            snake_body.pop()
                
        if not apple_spawn:
            apple_pos = [random.randrange(1, (d_width - snake_block) / 10.0) * 10,
                                random.randrange(1, (d_width - snake_block) / 10.0) * 10]
                
        apple_spawn = True
        dis.fill(black)
     
        for pos in snake_body:
            pygame.draw.rect(dis, green, pygame.Rect(
            pos[0], pos[1], 10, 10))
         
        pygame.draw.rect(game_window, white, pygame.Rect(
        apple_pos[0], apple_pos[1], 10, 10))

        # When game is over, there should messages asking 
        # if the user wants to close the game or restart
        # That's why game_close condition is set to true below instead of game_over
        if x >= d_width or x < 0 or y >= d_height or y < 0:
            game_close = True 

        x += move_x
        y += move_y

        dis.fill(black)
        
        pygame.draw.rect(dis, (140, 60, 60), [applex, appley, snake_block, snake_block])
        pygame.draw.rect(dis, (68, 78, 200), [x, y, snake_block, snake_block])
        pygame.display.update()   

        if x == applex and y == appley:
            applex = round(random.randrange(0, d_width - snake_block) / 10.0) * 10.0
            appley = round(random.randrange(0, d_height - snake_block) / 10.0) * 10.0

        framerate.tick(10)
    pygame.quit()
    quit()

main_game()