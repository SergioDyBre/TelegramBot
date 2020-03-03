#!/usr/bin/env python
# -*- coding: utf-8 -*-

from player import Player
from enemy import Enemy


class Board:
    cells = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

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
