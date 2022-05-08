import pygame
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
        self.image = pygame.image.load('C:/Users/franc/Downloads/FlappyBirdClone/flappy-bird-assets-master/sprites/redbird-midflap.png')
        self.rect = self.image.get_rect(topleft = (60,300)) #should be somewhere in the middle of the screen
        self.speed_x = speed_x
        self.speed_y = speed_y
        self.gravity = gravity

    def get_keyboard_input(self):
        key = pygame.key.get_pressed()

        if key[pygame.K_SPACE]:
            self.rect.x += self.speed_x
            self.rect.y -= self.speed_y
            #also replace the image with that of the upflap as long as the y is moving up
            if self.rect.y > 0:
                self.image = pygame.image.load('C:/Users/franc/Downloads/FlappyBirdClone/flappy-bird-assets-master/sprites/redbird-upflap.png')
                sound_up = pygame.mixer.Sound('C:/Users/franc/Downloads/FlappyBirdClone/flappy-bird-assets-master/audio/swoosh.wav')
                sound_up.set_volume(0.2)
                sound_up.play(0.2)

    def player_gravity(self):
        self.rect.y += self.gravity
        if self.rect.y < 0:
            self.image = pygame.image.load('C:/Users/franc/Downloads/FlappyBirdClone/flappy-bird-assets-master/sprites/redbird-downflap.png')


    def update(self):
        self.get_keyboard_input()
        self.player_gravity()



        

    
