#!/usr/bin/env python 
# -*- coding:utf-8 -*-
class GameStats():
    def __init__(self, ai_setting):
        self.ai_setting = ai_setting
        self.game_active = False
        self.reset_stats()

        self.high_score = self.read_high_score()

    def reset_stats(self):
        self.ships_left = self.ai_setting.ship_limit
        self.score = 0
        self.level = 1

    # 读取最高分
    def read_high_score(self):
        file_handle = open('high_score.txt', 'r')
        high_score = int(file_handle.read())
        file_handle.close()
        return high_score