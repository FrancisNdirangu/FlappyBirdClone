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
        
        #sprites setup
        Background(self.all_sprites)

        #sprite groups
        self.collision_sprites = pygame.sprite.group() 
        self.all_sprites = pygame.sprite.group()
#in order to get consistent smooth movement use delta time. which Clear Code has a video on

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
            pygame.display.update()
            self.clock.tick(FRAMERATE)









if __name__ == '__main__':
    game = Game()
    game.run()
