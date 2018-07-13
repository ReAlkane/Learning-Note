# -*- coding: utf-8 -*-
# @Time    : 2018/5/6 下午4:47
# @Author  : Alkane
# @FileName: settings.py
# @Software: PyCharm

class Settings():
    """存储Alien Invasion所有设置的类"""

    def __init__(self):
        """初始化游戏的设置"""
        # 屏幕设置
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        # 飞船的设置
        self.ship_speed_factor = 10
        self.ship_limit = 3

        # 子弹的设置
        self.bullet_speed_factor = 40
        self.bullet_width = 10
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullets_allowed = 10  # 限制屏幕上最多能有多少的子弹

        # 外星人的设置
        self.alien_speed_factor = 4
        self.fleet_drop_speed = 100
        self.fleet_direction = 1
