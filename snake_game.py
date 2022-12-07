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

        self.applex = round(random.randint(0, self.d_width - self.snake_block) / 10.0) * 10.0
        self.appley = round(random.randint(0, self.d_height - self.snake_block) / 10.0) * 10.0

        self.font_style = pygame.font.SysFont("bahnschrift", 30)
        self.score_font = pygame.font.SysFont("ariel", 20)

        self.snake_body = []

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

    def draw_snake(self):
        for pos in self.snake_body:
            pygame.draw.rect(self.dis, self.blue, pygame.Rect(pos[0], pos[1], self.snake_block, self.snake_block))

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

            # When game is over, there should messages asking 
            # if the user wants to close the game or restart
            # That's why game_close condition is set to true below instead of game_over
            if self.x >= self.d_width or self.x < 0 or self.y >=self. d_height or self.y < 0:
                self.game_close = True 

            self.x += self.move_x
            self.y += self.move_y
            self.dis.fill(self.black)
            pygame.draw.rect(self.dis, self.red, [self.applex, self.appley, self.snake_block, self.snake_block])

            self.snake_pos = [self.x,self.y]
            self.snake_body.append(self.snake_pos)
            if len(self.snake_body) > self.curr_score+1:
                del self.snake_body[0]
    
            for x in self.snake_body[:-1]:
                if x == self.snake_pos:
                    self.game_close = True

            self.draw_snake()
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
