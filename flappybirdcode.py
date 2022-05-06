#hello this is the file
import pygame


class Game:
    def __init__(self):
        #player setup


        #obstacle setup


        #audio setup

    #def collision checker

    #def creating obstacles

    #def update if this is needed here

    #def run







if __name__ == '__flappybirdcode__':
    pygame.init()
    screen = pygame.display.set_mode((600,500))
    pygame.display.set_caption('FlappyBirdClone')

    running = True






    while running:

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                running = False

        pygame.display.flip()
