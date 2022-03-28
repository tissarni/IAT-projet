import pygame
import random
import math
from pygame import mixer
import numpy as np

#encodes action as integer : 
#0 : gauche
#1 : droite
#2 : shoot
#3 : pass

#encodes state as np.array(np.array(pixels))

def Space_invaders():

    def __init__(self):
        print("bla");
        pygame.init()

        # creating screen
        self.screen_width = 800
        self.screen_height = 600
        self.screen = pygame.display.set_mode((screen_width, screen_height))

        # caption and icon
        self.pygame.display.set_caption("Welcome to Space Invaders Game by:- styles")

        # Score
        self.score_val = 0
        self.scoreX = 5
        self.scoreY = 5
        self.font = pygame.font.Font('freesansbold.ttf', 20)

        #Image
        self.playerImage = pygame.image.load('data/spaceship.png')
        self.current_state_ = pygame.surfarray.array3d(screen)

        # Game Over
        game_over_font = pygame.font.Font('freesansbold.ttf', 64)
    
    def Step(Action action):
        next_state = [[]]
        #updates next state
        #sleep(npFrame)
        returns next_state

    def Reset():
        #updates image

    def Render():
        #screen.blit(..)


