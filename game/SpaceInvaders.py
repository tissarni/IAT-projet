import math
import os
import random

import pygame


def getURL(filename):
    return os.path.dirname(__file__) + "/" + filename


# encodes action as integer :
# 0 : gauche
# 1 : droite
# 2 : shoot
# 3 : pass

# encodes state as np.array(np.array(pixels))

class SpaceInvaders():
    NO_INVADERS = 10  # Nombre d'aliens

    def __init__(self, sampling : int, display: bool = False):
        # player
        self.display = display

        # nombre d'actions (left, right, fire, no_action)
        self.na = 4

        # initializing pygame
        pygame.init()

        # creating screen
        self.screen_width = 800
        self.screen_height = 600
        if self.display:
            self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        else:
            self.screen = pygame.display.set_mode((self.screen_width, self.screen_height), flags=pygame.HIDDEN)

        # caption and icon
        pygame.display.set_caption("Welcome to Space Invaders Game by:- styles")

        # Score
        self.scoreX = 5
        self.scoreY = 5
        self.font = pygame.font.Font('freesansbold.ttf', 20)
        self.score_val = 0

        # Game Over
        self.game_over_font = pygame.font.Font('freesansbold.ttf', 64)

        self.playerImage = pygame.image.load(getURL('data/spaceship.png'))

        self.sampling = sampling


    def get_player_X(self) -> int:
        return self.player_X

    def get_player_Y(self) -> int:
        return self.player_Y

    def get_indavers_X(self) -> 'List[int]':
        return self.invader_X

    def get_indavers_Y(self) -> 'List[int]':
        return self.invader_Y

    def get_bullet_X(self) -> int:
        return self.bullet_X

    def get_bullet_Y(self) -> int:
        return self.bullet_Y

    def get_bullet_state(self) -> str:
        """Projectile
        - rest = bullet is not moving
        - fire = bullet is moving
        """
        return self.bullet_state

    def full_image(self):
        return pygame.surfarray.array3d(self.screen)

    def get_state(self):
        player_x = self.get_player_X()
        player_y = self.get_player_Y()
        invaders_x = self.get_indavers_X()
        invaders_y = self.get_indavers_Y()


        if invaders_y[self.getLowerInvader()] > self.screen_height:
            invaders_y[self.getLowerInvader()] = self.screen_height - 1


        if invaders_x[self.getLowerInvader()] > self.screen_width:
            invaders_x[self.getLowerInvader()] = self.screen_width - 1
        
        distance_x = int((player_x - invaders_x[self.getLowerInvader()]) / self.sampling)
        distance_y = int((player_y - invaders_y[self.getLowerInvader()]) / self.sampling)
        shooting = int(self.get_bullet_state == "fire")
        state = (distance_x, distance_y, shooting)
        return state

    def reset(self):
        """Reset the game at the initial state.
        """
        self.score_val = 0

        self.player_X = 370
        self.player_Y = 523
        self.player_Xchange = 0

        # Invader
        self.invaderImage = []
        self.invader_X = []
        self.invader_Y = []
        self.invader_Xchange = []
        self.invader_Ychange = []
        for _ in range(SpaceInvaders.NO_INVADERS):
            self.invaderImage.append(pygame.image.load(getURL('data/alien.png')))
            self.invader_X.append(random.randint(64, 737))
            self.invader_Y.append(random.randint(30, 180))
            self.invader_Xchange.append(1.2)
            self.invader_Ychange.append(50)

        # Bullet
        # rest - bullet is not moving
        # fire - bullet is moving
        self.bulletImage = pygame.image.load(getURL('data/bullet.png'))
        self.bullet_X = 0
        self.bullet_Y = 500
        self.bullet_Xchange = 0
        self.bullet_Ychange = 3
        self.bullet_state = "rest"

        if self.display:
            self.render()

        return self.get_state()

    def step(self, action):
        """Execute une action et renvoir l'état suivant, la récompense perçue
        et un booléen indiquant si la partie est terminée ou non.
        """
        is_done = False
        reward = 0

        # RGB
        self.screen.fill((0, 0, 0))
        # Controling the player movement from the arrow keys
        if action == 0:  # GO LEFT
            self.player_Xchange = -1.7
        if action == 1:  # GO RIGHT
            self.player_Xchange = 1.7
        if action == 2:  # FIRE
            self.player_Xchange = 0
            # Fixing the change of direction of bullet
            if self.bullet_state == "rest":
                self.bullet_X = self.player_X
                self.move_bullet(self.bullet_X, self.bullet_Y)
        if action == 3:  # NO ACTION
            self.player_Xchange = 0

        # adding the change in the player position
        self.player_X += self.player_Xchange
        for i in range(SpaceInvaders.NO_INVADERS):
            self.invader_X[i] += self.invader_Xchange[i]

        # bullet movement
        if self.bullet_Y <= 0:
            self.bullet_Y = 600
            self.bullet_state = "rest"
        if self.bullet_state == "fire":
            self.move_bullet(self.bullet_X, self.bullet_Y)
            self.bullet_Y -= self.bullet_Ychange

        # movement of the invader
        for i in range(SpaceInvaders.NO_INVADERS):

            if self.invader_Y[i] >= 450:
                if abs(self.player_X - self.invader_X[i]) < 80:
                    for j in range(SpaceInvaders.NO_INVADERS):
                        self.invader_Y[j] = 2000
                    is_done = True
                    break

            if self.invader_X[i] >= 735 or self.invader_X[i] <= 0:
                self.invader_Xchange[i] *= -1
                self.invader_Y[i] += self.invader_Ychange[i]
            # Collision
            collision = self.isCollision(self.bullet_X, self.invader_X[i], self.bullet_Y, self.invader_Y[i])
            if collision:
                reward = 1
                self.score_val += 1
                self.bullet_Y = 600
                self.bullet_state = "rest"
                self.invader_X[i] = random.randint(64, 736)
                self.invader_Y[i] = random.randint(30, 200)
                self.invader_Xchange[i] *= -1

            self.move_invader(self.invader_X[i], self.invader_Y[i], i)

        # restricting the spaceship so that it doesn't go out of screen
        if self.player_X <= 16:
            self.player_X = 16
        elif self.player_X >= 750:
            self.player_X = 750

        self.move_player(self.player_X, self.player_Y)

        if self.display:
            self.render()

        return self.get_state(), reward, is_done

    def render(self):
        self.show_score(self.scoreX, self.scoreY)
        pygame.display.update()

    def move_player(self, x, y):
        self.screen.blit(self.playerImage, (x - 16, y + 10))

    def move_invader(self, x, y, i):
        self.screen.blit(self.invaderImage[i], (x, y))

    def move_bullet(self, x, y):
        self.screen.blit(self.bulletImage, (x, y))
        self.bullet_state = "fire"

    def show_score(self, x, y):
        score = self.font.render("Points: " + str(self.score_val), True, (255, 255, 255))
        self.screen.blit(score, (x, y))

    def game_over(self):
        game_over_text = self.game_over_font.render("GAME OVER", True, (255, 255, 255))
        self.screen.blit(game_over_text, (190, 250))

    # Collision Concept
    def isCollision(self, x1, x2, y1, y2):
        distance = math.sqrt((math.pow(x1 - x2, 2)) + (math.pow(y1 - y2, 2)))
        return (distance <= 50)


    def getScore(self):
        return self.score_val

    def getLowerInvader(self):
        max_value = max(self.get_indavers_Y())
        return self.get_indavers_Y().index(max_value)
