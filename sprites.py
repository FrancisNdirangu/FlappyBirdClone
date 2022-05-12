import pygame




class Background(pygame.sprite.Sprite):
    def __init__(self,groups):
        super().__init__()
        self.image = pygame.image.load('C:/Users/franc/Downloads/FlappyBirdClone/flappy-bird-assets-master/sprites/background-day.png')
        self.rect = self.image.get_rect(topleft = (0,0))
