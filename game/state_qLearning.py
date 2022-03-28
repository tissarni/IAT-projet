import pygame
import random
import math
from pygame import mixer
import numpy as np


class State():
	#collision balle : si distance euclienne <= 50
	#collision vaisseau-invaders : if invader_Y[i] >= 450: && delta_x < 80:
	#changeY : 50
	#changeX_invaders ~= 10
	def __init__(self, invaders_init_position, player_init_position, nbInvaders):
		self.invaders_pos = invadars_init_position
		self.nbInvaders = nbInvaders
		self.last_invaders_pos = [[]]
		self.player_pos = player_init_position
		self.invaders_state = [[]]
		self.screen_width = 800
		self.screen_height = 600

	def update_state(self,invaders_delta_xy,player_delta_xy):

		for i in range(nbInvaders):
			next_invaders_pos = [[]]
			next_player_pos = [[]]
			
			self.last_invaders_pos = self.invaders_pos;
			self.player_pos[0] = player_pos[0]+player_delta_xy[0]
			self.player_pos[1] = player_pos[1]+player_delta_xy[1]

			invaders_pos[i][0] = invaders_pos[i][0]+invaders_delta_xy[i][0]:
			invaders_pos[i][1] = invaders_pos[i][1]+invaders_delta_xy[i][1]:

			if (getZone(i,"x")=="veryCloseZone" && (self.player_pos[0]-invaders_pos[i][0]) <0):
				invaders_state[i][0]=1
			if (getZone(i,"x")=="veryCloseZone" && (self.player_pos[0]-invaders_pos[i][0]) >0):
				invaders_state[i][0]=-1

			if (getZone(i,"x")=="midCloseZone" && (self.player_pos[0]-invaders_pos[i][0]) <0):
				invaders_state[i][0]=2
			if (getZone(i,"x")=="midCloseZone" && (self.player_pos[0]-invaders_pos[i][0]) >0):
				invaders_state[i][0]=-2

			if (getZone(i,"x")=="farCloseZone" && (self.player_pos[0]-invaders_pos[i][0]) <0):
				invaders_state[i][0]=3
			if (getZone(i,"x")=="farCloseZone" && (self.player_pos[0]-invaders_pos[i][0]) >0):
				invaders_state[i][0]=-3

			if (getZone(i,"y")=="veryCloseZone"):
				invaders_state[i][1]=1
			if (getZone(i,"y")=="midCloseZone"):
				invaders_state[i][1]=2
			if (getZone(i,"y")=="farCloseZone"):
				invaders_state[i][1]=3

		return invaders_state

	def getZone(i,s):
		if (s=="x"):
			if (math.abs(self.player_pos[0]-invaders_pos[i][0])<120):
				return "veryCloseZone"
			if (math.abs(self.player_pos[0]-invaders_pos[i][0])<200 && math.abs(self.player_pos[0]-invaders_pos[i][0])<120):
				return "midCloseZone"
			return "farCloseZone"

		if (s=="y"):
			if (math.abs(self.player_pos[0]-invaders_pos[i][0])<200):
				return "veryCloseZone"
			if (math.abs(self.player_pos[0]-invaders_pos[i][0])<300 && math.abs(self.player_pos[0]-invaders_pos[i][0])<200):
				return "midCloseZone"
			return "farCloseZone"