#hello this is the file
import pygame
from player import Player
from random import choice


class Game:
    def __init__(self):
        pass
        #player setup

        #obstacle setup


        #audio setup

    #def collision checker

    #def creating obstacles

    #def run

def obstacle_creater(self):
    pass

def create_multiple_obstacles(self):
    pass

def collision_checker(self):
    pass

def display_level(self):
    pass

def display_score(self):
    pass

def victory_message(self):
    pass

def run(self):
    pass


class Background(pygame.sprite.Sprite):
    def __init__(self,image_file,location):
        super().__init__()
        image_file = choice(['C:/Users/franc/Downloads/FlappyBirdClone/flappy-bird-assets-master/sprites/background-day.png'
        ,'C:/Users/franc/Downloads/FlappyBirdClone/flappy-bird-assets-master/sprites/background-night.png'])
        self.image = pygame.image.load(image_file)
        self.rect = self.image.get_rect()
        self.rect.x,self.rect.y = location








if __name__ == '__flappybirdcode__':
    pygame.init()
    screen = pygame.display.set_mode((600,500))
    pygame.display.set_caption('FlappyBirdClone')
    image_file = choice(['C:/Users/franc/Downloads/FlappyBirdClone/flappy-bird-assets-master/sprites/background-day.png'
        ,'C:/Users/franc/Downloads/FlappyBirdClone/flappy-bird-assets-master/sprites/background-night.png'])
    
    #game = Game()
    running = True
    clock = pygame.time.Clock()








    while running:

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                running = False

        screen.fill((0,0,0))
        #game.run() when you make the run function in the game class
        Background(image_file,[0,0])


        pygame.display.flip()
        clock.tick(60)
