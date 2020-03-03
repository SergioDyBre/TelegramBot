#!/usr/bin/env python
# -*- coding: utf-8 -*-
import logging
from telegram.ext import Updater, CommandHandler
from board import Board
from enemy import Enemy
from player import Player

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

updater = Updater('1142606683:AAFHEBgNIDbqZZ6RizWYRLFmqRpr-8KRBEg', use_context=True)

# Game data
a_board = None
an_enemy = None
a_player = None


def begin_game(update, context):
    global a_board
    global an_enemy
    global a_player

    a_board = Board()
    an_enemy = Enemy("Ogro")
    a_player = Player(12, "Guerrero")
    a_board.cells[0][0] = a_player
    a_board.cells[9][9] = an_enemy

    update.message.reply_text("I've created a new game! Please use /show to show the board.")


def draw_board(update, context):
    if a_board == None:
        update.message.reply_text("There is no board created yet. Please use the command /begin to begin a new game. 💘")
    else:
        update.message.reply_text(str(a_board))


updater.dispatcher.add_handler(CommandHandler('show', draw_board))
updater.dispatcher.add_handler(CommandHandler('begin', begin_game))

updater.start_polling()
updater.idle()

# <3
