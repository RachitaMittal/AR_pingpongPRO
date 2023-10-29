import argparse
import os
import time
import sys

import cv2
import numpy as np
import matplotlib.pyplot as plt
import pygame
from pygame.locals import *

import aruco
from aruco import ArucoDetector
from aruco import CalibrationArucoBoard

class PingPongARGame:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption('Ping Pong AR PRO')

        self.background = pygame.image.load("images/background.png").convert()
        self.background = pygame.transform.scale(self.background, (800, 600))

        self.ball = pygame.image.load("images/ball.png").convert_alpha()
        self.ball_rect = self.ball.get_rect()

        self.player = pygame.image.load("images/player.png").convert_alpha()
        self.player_rect = self.player.get_rect()

        self.player_speed = 0
        self.ball_speed_x = 0
        self.ball_speed_y = 0

    def game_loop(self):
        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == KEYDOWN:
                    if event.key == K_UP:
                        self.player_speed = -10
                    elif event.key == K_DOWN:
                        self.player_speed = 10
                elif event.type == KEYUP:
                    if event.key == K_UP or event.key == K_DOWN:
                        self.player_speed = 0

            self.screen.blit(self.background, (0, 0))

            self.player_rect.centery += self.player_speed

            if self.player_rect.top <= 0:
                self.player_rect