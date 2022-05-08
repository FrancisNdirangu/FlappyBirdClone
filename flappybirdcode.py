#hello this is the file
import pygame
from player import Player
from random import choice


class Game:
    def __init__(self):
        #player setup
        player_sprite = Player(45,60,5)
        self.player = pygame.sprite.GroupSingle(player_sprite)
        
        #score setup
        self.score = 0


        #obstacle setup


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


class Background(pygame.sprite.Sprite):
    def __init__(self,image_file,location,screen_width,screen_height):
        #super().__init__()
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(image_file)
        self.image = pygame.transform.scale(self.image,(screen_width,screen_height))
        self.rect = self.image.get_rect()
        self.rect.x,self.rect.y = location
        








if __name__ == '__main__':
    pygame.init()
    screen_width = 600
    screen_height = 600
    screen = pygame.display.set_mode((screen_width,screen_height))
    pygame.display.set_caption('FlappyBirdClone')
    image_file = choice(['C:/Users/franc/Downloads/FlappyBirdClone/flappy-bird-assets-master/sprites/background-day.png'
        ,'C:/Users/franc/Downloads/FlappyBirdClone/flappy-bird-assets-master/sprites/background-night.png'])
    
    background = Background(image_file,[0,0],screen_width,screen_height)    
    
    running = True
    clock = pygame.time.Clock()
    game = Game()

    while running:

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                running = False

        screen.fill([0,0,0])

        screen.blit(background.image,background.rect)
        game.run() #when you make the run function in the game class



        pygame.display.flip()
        clock.tick(60)
