import pygame
from random import choice
#properties of the player:
#player should move diagonally forward by clicking. both x and y movement at a constant speed
#player image should change based on the click. player should start on the midflap and then the upflap then the bottomflap then the upflap and so on.
#player should have collisions with the obstacles
#player is not destroyed by the colliding with the obstacle but should instead fall off the screen and then there should be a 'you lose' on the screen
#player should have a sound that plays during each click
#there should be a score that increases as time passes when the player is alive
class Player(pygame.sprite.Sprite):
    def __init__(self,speed_x,speed_y,gravity):
        super().__init__()
        player_image = choice(['C:/Users/franc/Downloads/FlappyBirdClone/flappy-bird-assets-master/sprites/redbird-midflap.png',
        'C:/Users/franc/Downloads/FlappyBirdClone/flappy-bird-assets-master/sprites/yellowbird-midflap.png'])
        self.image = pygame.image.load(player_image)
        self.rect = self.image.get_rect(topleft = (60,300)) #should be somewhere in the middle of the screen
        self.speed_x = speed_x
        self.speed_y = speed_y
        self.gravity = gravity
        self.ready = True
        self.jump_time = 0
        self.jump_cooldown = 200

    def get_keyboard_input(self):
        key = pygame.key.get_pressed()

        if key[pygame.K_SPACE] and self.ready:
            self.rect.x += self.speed_x
            self.rect.y -= self.speed_y
            self.ready = False
            self.jump_time = pygame.time.get_ticks()
            #also replace the image with that of the upflap as long as the y is moving up
            if self.rect.y > 0:
                self.image = pygame.image.load('C:/Users/franc/Downloads/FlappyBirdClone/flappy-bird-assets-master/sprites/redbird-upflap.png') #this is not changing the image
                #another issue is that we are only using the red bird upflap and we have to find a way to use both for the upflap, we can do that by finding the index we used in the choice
                sound_up = pygame.mixer.Sound('C:/Users/franc/Downloads/FlappyBirdClone/flappy-bird-assets-master/audio/wing.wav')
                sound_up.set_volume(0.2)
                sound_up.play()

    def player_gravity(self):
        self.rect.y += self.gravity
        if self.rect.y < 0:
            self.image = pygame.image.load('C:/Users/franc/Downloads/FlappyBirdClone/flappy-bird-assets-master/sprites/redbird-downflap.png')

    def jump_delay(self):
        if not self.ready:
            current_time = pygame.time.get_ticks()
            if current_time - self.jump_time >= self.jump_cooldown:
                self.ready = True

    def player_jump_path(self): #we need to use reverse kinematics to smoothen the path that the player sprite undergoes
        pass


    def update(self):
        self.get_keyboard_input()
        self.player_gravity()
        self.jump_delay()
        #self.image =  #this is for updating the self.image when we do jump



        

    
