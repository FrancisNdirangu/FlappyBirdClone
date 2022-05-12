#hello this is the file
import pygame
from player import Player
from random import choice
from sprites import Background


class Game:
    def __init__(self):
        #player setup
        player_sprite = Player(45,60,5)
        self.player = pygame.sprite.GroupSingle(player_sprite)
        
        #sprites setup
        Background(self.all_sprites)

        #score setup
        self.score = 0


        #obstacle setup
        self.collision_sprites = pygame.sprite.group()

        #all_sprites group 
        self.all_sprites = pygame.sprite.group()
#in order to get consistent smooth movement use delta time. which Clear Code has a video on

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
        self.player.update()
        self.player.draw(screen)









if __name__ == '__main__':
    pygame.init()
    screen_width = 600
    screen_height = 600
    screen = pygame.display.set_mode((screen_width,screen_height))
    pygame.display.set_caption('FlappyBirdClone')
  
    
    running = True
    clock = pygame.time.Clock()
    game = Game()

    while running:

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                running = False

        screen.fill([0,0,0])


        
        game.run() #when you make the run function in the game class



        pygame.display.flip()
        clock.tick(60)
