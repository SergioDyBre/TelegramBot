#!/usr/bin/env python
# -*- coding: utf-8 -*-
from random import randint

from player import Player
from enemy import Enemy


class Board:

    def __init__(self, player):
        """ Randomly initializes a board with a player. """
        self.cells = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
        new_player_x = randint(0, 9)
        new_player_y = randint(0, 9)
        self.cells[new_player_y][new_player_x] = player

        number_of_enemies = randint(1, 3)
        for i in range(0, number_of_enemies):
            new_enemy_x = randint(0, 9)
            new_enemy_y = randint(0, 9)
            while(self.cells[new_enemy_y][new_enemy_x] != 0):
                new_enemy_x = randint(0, 9)
                new_enemy_y = randint(0, 9)
            self.cells[new_enemy_y][new_enemy_x] = Enemy("Enemy {}".format(i))

    def __str__(self):
        """ Beatifully prints the current board with c00l emoji """
        floor_emoji = "⬜"
        player_emoji = "🇪🇸"
        enemy_emoji = "💀"
        error_emoji = "❌"

        board_render = ""

        for row in self.cells:
            for tile in row:
                if tile == 0:
                    board_render += floor_emoji
                elif isinstance(tile, Player):
                    board_render += player_emoji
                elif isinstance(tile, Enemy):
                    board_render += enemy_emoji
                else:
                    board_render += error_emoji
            board_render += "\n"

        return board_render
