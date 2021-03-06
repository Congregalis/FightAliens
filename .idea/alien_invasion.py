#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import sys
import pygame
import time

from pygame.sprite import Group
from settings import Settings
from ship import Ship
from alien import Alien
from asuna import Asuna
from game_stats import GameStats
from button import Button
from scoreboard import ScoreBoard
import  game_functions as gf


def run_game():
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height)
    )
    gameIcon = pygame.image.load("images/icon.png")
    pygame.display.set_icon(gameIcon)
    pygame.display.set_caption("打洗外星人")
    # pygame.mixer.init()
    # music_file = 'music/lrh-xjzw.mp3'
    # pygame.mixer.music.load(music_file)
    # pygame.mixer.music.set_volume(0.2)
    # pygame.mixer.music.play(1)
    # time.sleep(10)

    stats = GameStats(ai_settings)
    sb = ScoreBoard(ai_settings, screen, stats)
    play_button = Button(ai_settings, screen, "Play")
    ship = Ship(ai_settings, screen)
    asuna = Asuna(screen)
    bullets = Group()
    aliens = Group()
    gf.create_fleet(ai_settings, screen, ship, aliens)

    while True:
        gf.check_events(ai_settings, screen, stats, sb, play_button, ship, aliens,
                        bullets)

        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings, screen, stats, sb, ship, bullets, aliens)
            gf.update_aliens(ai_settings, stats, sb, screen, ship, aliens, bullets)

        gf.update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets,
                         play_button, asuna)

run_game()