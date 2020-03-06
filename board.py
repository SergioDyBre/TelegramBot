#!/usr/bin/env python
# -*- coding: utf-8 -*-
from random import randint
from obstacle import Obstacle
from player import Player
from enemy import Enemy


class Board:

    def __init__(self, player):
        """ Randomly initializes a board with a player. """
        self.cells = []
        self.size_x = randint(5, 14)
        self.size_y = randint(5, 14)
        self.list_enemies = []

        self.create_random_board()
        self.create_obstacles()
        self.create_player(player)
        self.create_enemies()

    def __str__(self):
        """ Beatifully prints the current board with c00l emoji """
        floor_emoji = "⬜"
        player_emoji = "🇪🇸"
        enemy_emoji = "💀"
        error_emoji = "❌"
        obstacle_emoji = "⬛️"

        board_render = ""

        for row in self.cells:
            for tile in row:
                if tile == 0:
                    board_render += floor_emoji
                elif isinstance(tile, Player):
                    board_render += player_emoji
                elif isinstance(tile, Enemy):
                    board_render += enemy_emoji
                elif isinstance(tile, Obstacle):
                    board_render += obstacle_emoji  
                else:
                    board_render += error_emoji
            board_render += "\n"

        return board_render

    def make_enemies_move(self):
        for enemy in self.list_enemies:
            enemy.make_move()

    def create_random_board(self):
        for y in range(0, self.size_y):
            row = []
            for x in range(0, self.size_x):
                row.append(0)
            self.cells.append(row)

    def create_player(self, player):
        new_player_x = randint(0, self.size_x - 1)
        new_player_y = randint(0, self.size_y - 1)
        self.cells[new_player_y][new_player_x] = player
        player.set_coordinates(new_player_x, new_player_y)
        player.set_board(self)

    def create_enemies(self):
        number_of_enemies = randint(1, 3)
        for i in range(0, number_of_enemies):
            new_enemy_x = randint(0, self.size_x - 1)
            new_enemy_y = randint(0, self.size_y - 1)
            while(self.cells[new_enemy_y][new_enemy_x] != 0):
                new_enemy_x = randint(0, self.size_x)
                new_enemy_y = randint(0, self.size_y)

            enemy = Enemy("Enemy {}".format(i))
            self.cells[new_enemy_y][new_enemy_x] = enemy
            self.list_enemies.append(enemy)
            enemy.set_coordinates(new_enemy_x, new_enemy_y)
            enemy.set_board(self)

    def create_obstacles(self):
        num_obstacles = randint(1,3)
       

        for i in range(0, num_obstacles):
            obstacle_size = randint(1,2)
            x = randint(0, self.size_x - 1)
            y = randint(0, self.size_y - 1)
            self.cells[y][x] = Obstacle()
            for i in range(0, obstacle_size - 1):
                move = randint(0, 3)
                if move == 0:
                    y = y - 1
                elif move == 1:
                    x = x + 1
                elif move == 2:
                    y = y + 1
                elif move == 3:
                    x = x - 1
                if 0 <= x < self.size_x and 0 <= y < self.size_y:
                    self.cells[y][x] = Obstacle()    