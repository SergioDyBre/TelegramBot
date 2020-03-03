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
        self.list_enemies = []              
        new_player_x = randint(0, 9)
        new_player_y = randint(0, 9)
        self.cells[new_player_y][new_player_x] = player
        player.set_coordinates(new_player_x, new_player_y)
        player.set_board(self)

        number_of_enemies = randint(1, 3)
        for i in range(0, number_of_enemies):
            new_enemy_x = randint(0, 9)
            new_enemy_y = randint(0, 9)
            while(self.cells[new_enemy_y][new_enemy_x] != 0):
                new_enemy_x = randint(0, 9)
                new_enemy_y = randint(0, 9)

            enemy =  Enemy("Enemy {}".format(i))
            self.cells[new_enemy_y][new_enemy_x] = enemy
            self.list_enemies.append(enemy)
            enemy.set_coordinates(new_enemy_x, new_enemy_y)
            enemy.set_board(self)

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

    def make_enemies_move(self):
        for enemy in self.list_enemies:
            enemy.make_move()   
