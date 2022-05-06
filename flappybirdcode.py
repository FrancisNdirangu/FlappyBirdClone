#hello this is the file
import pygame

screen = pygame.display.set_mode((600,500))
pygame.display.set_caption('FlappyBirdClone')

running = True

while running:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False