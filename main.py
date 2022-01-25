import pygame
import sys
import time
from pygame.locals import *

SIZE = 40

class Snake:
    
    def __init__(self, surface, length):
        self.length = length
        self.parent_screen = surface
        self.block = pygame.image.load("resources/block.jpg").convert()
        self.x = [SIZE]*length
        self.y = [SIZE]*length
        self.direction = "down"
        
    
    def move_left(self):
        self.direction = "left"
        
    def move_right(self):
        self.direction = "right"
        
    def move_down(self):
        self.direction = "up"
        
    def move_up(self):
        self.direction = "down"  
        
    
    def draw(self):
        self.parent_screen.fill((100, 110, 5))
        for i in range(self.length):
            self.parent_screen.blit(self.block,(self.x[i], self.y[i]))
        pygame.display.flip()  
        
        
    def walk(self):
        
        for i in range(self.length-1,0, -1):
            self.x[i] = self.x[i-1]
            self.y[i] = self.y[i-1]        
            if self.direction == "left":
                self.x[0] -= 10
            if self.direction == "right":
                self.x[0] += 10
            if self.direction == "up":
                self.y[0] += 10
            if self.direction == "down":
                self.y[0] -= 10
                
        self.draw()
            
            
        

class Game:
    
    def __init__(self):
        pygame.init()
        self.surface = pygame.display.set_mode((1200, 800))
        self.surface.fill((100, 110, 5))
        self.snake = Snake(self.surface, 2)
        self.snake.draw()
        
        
        
    def run(self):
        
        while True:
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        sys.exit()
                        
                    if event.key == K_UP:
                        self.snake.move_up()
                        
                    if event.key == K_DOWN:
                        self.snake.move_down()
                        
                    if event.key == K_LEFT:
                        self.snake.move_left()
                        
                    if event.key == K_RIGHT:
                        self.snake.move_right()
                        
                elif event.type == pygame.QUIT:
                    sys.exit()
                    
            self.snake.walk()
            time.sleep(0.2)
  


if __name__ == '__main__':
    game = Game()
    game.run()
    
    
    
    
    
   