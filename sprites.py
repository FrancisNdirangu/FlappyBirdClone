import pygame
from settings import *




class Background(pygame.sprite.Sprite):
    def __init__(self,groups,scale_factor):
        super().__init__(groups)
        background_image = pygame.image.load('C:/Users/franc/Downloads/FlappyBirdClone/flappy-bird-assets-master/sprites/background-day.png')

        FULL_HEIGHT = background_image.get_height() * scale_factor 
        FULL_WIDTH = background_image.get_width() * scale_factor

        self.image = pygame.transform.scale(background_image,(int(FULL_WIDTH),int(FULL_HEIGHT)))
        self.rect = self.image.get_rect(topleft = (0,0))
