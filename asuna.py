#!/usr/bin/env python 
# -*- coding:utf-8 -*-

import pygame

class Asuna():
    def __init__(self, screen):
        self.screen = screen

        self.image = pygame.image.load('images/asuna.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        self.rect.centerx = self.screen_rect.centerx
        self.rect.top = self.screen_rect.top
    def blitme(self):
        self.screen.blit(self.image, self.rect)


