#!/usr/bin/env python 
# -*- coding:utf-8 -*-

import pygame
from pygame.sprite import Sprite

class Ship(Sprite):
    def __init__(self,ai_settings, screen):
        super(Ship, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        self.rect.centerx = self.screen_rect.centerx  #飞船中心的x坐标
        self.rect.centery = self.screen_rect.centery
        self.rect.bottom = self.screen_rect.bottom    #飞船下边缘的y坐标

        self.centerfx = float(self.rect.centerx)
        self.centerfy = float(self.rect.centery)

        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.centerfx += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left > self.screen_rect.left:
            self.centerfx -= self.ai_settings.ship_speed_factor
        if self.moving_up and self.rect.top > self.screen_rect.top:
            self.centerfy -= self.ai_settings.ship_speed_factor
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.centerfy += self.ai_settings.ship_speed_factor
        self.rect.centerx = self.centerfx
        self.rect.centery = self.centerfy

    def center_ship(self):
        self.centerfx = self.screen_rect.centerx
        self.centerfy = self.screen_rect.bottom - self.rect.height / 2

    def blitme(self):
        self.screen.blit(self.image, self.rect)
