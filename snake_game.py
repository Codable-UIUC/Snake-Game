import pygame
import sys
import time
import random

class SnakeGame():

    def __init__(self, max_score) -> None:
        pygame.init()

        self.d_width = 600
        self.d_height = 400
        self.snake_block = 10

        self.dis = pygame.display.set_mode((self.d_width, self.d_height))
        pygame.display.set_caption('Snake Game')
        # blue=(0,0,255)
        self.blue = (0, 0, 255)
        self.red = (255, 0, 0)
        self.black = (0, 0, 0)
        self.green = (0, 255, 0)
        self.white = (255, 255, 255)
        self.framerate = pygame.time.Clock()

        # main game loop
        self.game_over = False
        self.game_close = False

        self.x = self.d_width / 2
        self.y = self.d_height / 2

        self.move_x = 0
        self.move_y = 0

        self.applex = round(random.randrange(0, self.d_width - self.snake_block) / 10.0) * 10.0
        self.appley = round(random.randrange(0, self.d_width - self.snake_block) / 10.0) * 10.0

        self.font_style = pygame.font.SysFont("bahnschrift", 30)
        self.score_font = pygame.font.SysFont("comicsansms", 20)

        self.max_score = max_score
        self.curr_score = 0

    def display_score(self, score, higest_score):
        self.highest_value = self.score_font.render("Highest Score: " + str(higest_score), True, self.white)
        self.curr_value = self.score_font.render("Current Score: " + str(score), True, self.white)
        self.dis.blit(self.highest_value, [10, 0])
        self.dis.blit(self.curr_value, [10, 20])

    def display_msg(self, msg, color):
        mesg = self.font_style.render(msg, True, color)
        self.dis.blit(mesg, [150, 180])

    def set_higest_score(self, max_score, curr_score):
        self.max_score = max(max_score, curr_score)

    def main_game(self):
        while not self.game_over:
            while self.game_close == True:
                self.dis.fill(self.black)
                self.display_msg("Press R to Restart or Q to Quit", self.red)
                self.display_score(self.curr_score, self.max_score)
                pygame.display.update()
    
                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_q:
                            self.game_over = True
                            self.game_close = False
                        if event.key == pygame.K_r:
                            self.set_higest_score(self.max_score, self.curr_score)
                            self.__init__(max_score=self.max_score)
    
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.game_over = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        self.move_x = -self.snake_block
                        self.move_y = 0
                    elif event.key == pygame.K_RIGHT:
                        self.move_x = self.snake_block
                        self.move_y = 0
                    elif event.key == pygame.K_UP:
                        self.move_y = -self.snake_block
                        self.move_x = 0
                    elif event.key == pygame.K_DOWN:
                        self.move_y = self.snake_block
                        self.move_x = 0
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.game_over = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        self.move_x = -self.snake_block
                        self.move_y = 0
                    elif event.key == pygame.K_RIGHT:
                        self.move_x = self.snake_block
                        self.move_y = 0
                    elif event.key == pygame.K_UP:
                        self.move_y = -self.snake_block
                        self.move_x = 0
                    elif event.key == pygame.K_DOWN:
                        self.move_y = self.snake_block
                        self.move_x = 0
            
            if self.x >= self.d_width or self.x < 0 or self.y >= self.d_height or self.y < 0:
                self.game_close = True

            #body growing
            self.snake_pos = [self.x,self.y]
            self.snake_body = [[self.x-10, self.y],[self.x-20,self.y],[self.x-30,self.y],[self.x-40,self.y]]
            self.apple_pos = [self.applex, self.appley]
            self.apple_spawn = True

            self.snake_body.insert(0, list(self.snake_pos))
            if self.snake_pos[0] == self.apple_pos[0] and self.snake_pos[1] == self.apple_pos[1]:
                score += 10
                self.apple_spawn = False
            else:
                self.snake_body.pop()
                    
            if not self.apple_spawn:
                self.apple_pos = [random.randrange(1, (self.d_width - self.snake_block) / 10.0) * 10,
                                    random.randrange(1, (self.d_width - self.snake_block) / 10.0) * 10]
                    
            self.apple_spawn = True
            self.dis.fill(self.black)
        
            for pos in self.snake_body:
                pygame.draw.rect(self.dis, self.green, pygame.Rect(
                pos[0], pos[1], 10, 10))
            
            pygame.draw.rect(self.dis, self.white, pygame.Rect(
            self.apple_pos[0], self.apple_pos[1], 10, 10))

            # When game is over, there should messages asking 
            # if the user wants to close the game or restart
            # That's why game_close condition is set to true below instead of game_over
            if self.x >= self.d_width or self.x < 0 or self.y >=self. d_height or self.y < 0:
                self.game_close = True 

            self.x += self.move_x
            self.y += self.move_y

            self.dis.fill(self.black)
            
            pygame.draw.rect(self.dis, (140, 60, 60), [self.applex, self.appley, self.snake_block, self.snake_block])
            pygame.draw.rect(self.dis, (68, 78, 200), [self.x, self.y, self.snake_block, self.snake_block])
            self.display_score(self.curr_score,self.max_score)
            pygame.display.update()   

            if self.x == self.applex and self.y == self.appley:
                self.applex = round(random.randrange(0, self.d_width - self.snake_block) / 10.0) * 10.0
                self.appley = round(random.randrange(0, self.d_height - self.snake_block) / 10.0) * 10.0
                self.curr_score += 1

            self.framerate.tick(10)
        self.max_score = max(self.curr_score, self.max_score)
        pygame.quit()
        quit()

game = SnakeGame(0)
game.main_game()
=======
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
green = (0, 255, 0)
white = (255, 255, 255)
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
         
        pygame.draw.rect(dis, white, pygame.Rect(
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
