#hello this is the file
import pygame,sys,time
from player import Player
from sprites import Background
from settings import *


class Game:
    def __init__(self):
        pygame.init()
        self.display_surface = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT))
        pygame.display.set_caption('Flappy_Bird')
        self.clock = pygame.time.Clock()
        #player setup
        player_sprite = Player(45,60,5)
        self.player = pygame.sprite.GroupSingle(player_sprite)
        


        #sprite groups
        self.collision_sprites = pygame.sprite.Group() 
        self.all_sprites = pygame.sprite.Group()
#in order to get consistent smooth movement use delta time. which Clear Code has a video on
        

        #scale factor
        background_height = pygame.image.load('C:/Users/franc/Downloads/FlappyBirdClone/flappy-bird-assets-master/sprites/background-day.png').get_height()
        self.scale_factor = WINDOW_HEIGHT/ background_height
        

        #sprites setup
        Background(self.all_sprites,self.scale_factor)

    def run(self):


        last_time = time.time()
        while True:
            #delta time
            dt = time.time() -last_time
            last_time = time.time()

            #event loop
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            #game logic
            self.all_sprites.update(dt)
            self.all_sprites.draw(self.display_surface)
            pygame.display.update()
            self.clock.tick(FRAMERATE)









if __name__ == '__main__':
    game = Game()
    game.run()
