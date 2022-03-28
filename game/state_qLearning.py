import imp
import pygame
import random
from pygame import mixer
import numpy as np
from copy import deepcopy

class State():
	#collision balle : si distance euclienne <= 50
	#collision vaisseau-invaders : if invader_Y[i] >= 450: && delta_x < 80:
	#changeY : 50
	#changeX_invaders ~= 10
	def __init__(self, player_init_position, nbInvaders):
		self.nbInvaders = nbInvaders
		self.player_x = player_init_position[0]
		self.player_y = player_init_position[1]
		self.current_state = [[0,0] for _ in range(nbInvaders)]
		self.last_state = [[0,0] for _ in range(nbInvaders)]
		self.screen_width = 800
		self.screen_height = 600

	def update_state(self, invaders_x, invaders_y, player_x):

		for i in range(self.nbInvaders):
			self.last_state = deepcopy(self.current_state)

			zone_x = self.getZone("x", player_x, (invaders_x[i], invaders_y[i]))
			zone_y = self.getZone("y", player_x, (invaders_x[i], invaders_y[i]))

			if (zone_x=="veryCloseZone" and (player_x-invaders_x[i]) <0):
				self.current_state[i][0]=1
			if (zone_x=="veryCloseZone" and (player_x-invaders_x[i]) >0):
				self.current_state[i][0]=-1

			if (zone_x=="midCloseZone" and (player_x-invaders_x[i]) <0):
				self.current_state[i][0]=2
			if (zone_x=="midCloseZone" and (player_x-invaders_x[i]) >0):
				self.current_state[i][0]=-2

			if (zone_x=="farCloseZone" and (player_x-invaders_x[i]) <0):
				self.current_state[i][0]=3
			if (zone_x=="farCloseZone" and (player_x-invaders_x[i]) >0):
				self.current_state[i][0]=-3

			if (zone_y=="veryCloseZone"):
				self.current_state[i][1]=1
			if (zone_y=="midCloseZone"):
				self.current_state[i][1]=2
			if (zone_y=="farCloseZone"):
				self.current_state[i][1]=3

	def getData(self):
		return (self.last_state, self.current_state)

	def getZone(self, s, player_x, invaders_i):
		if (s=="x"):
			if (abs(player_x-invaders_i[0])<120):
				return "veryCloseZone"
			if (abs(player_x-invaders_i[0])<200 and abs(self.player_x-invaders_i[0])>120):
				return "midCloseZone"
			return "farCloseZone"

		if (s=="y"):
			if (abs(self.player_y-invaders_i[1])<150):
				return "veryCloseZone"
			if (abs(self.player_y-invaders_i[1])<300 and abs(self.player_y-invaders_i[1])>150):
				return "midCloseZone"
			return "farCloseZone"