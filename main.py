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

    a_player = Player(12, "Guerrero")
    a_board = Board(a_player)

    update.message.reply_text("I've created a new game! Please use /show to show the board.")


def draw_board(update, context):
    if a_board == None:
        update.message.reply_text("There is no board created yet. Please use the command /begin to begin a new game. 💘")
    else:
        update.message.reply_text(str(a_board))


def move_up(update, context):
    a_player.move_up()
    draw_board(update, context)


def move_down(update, context):
    a_player.move_down()
    draw_board(update, context)


def move_left(update, context):
    a_player.move_left()
    draw_board(update, context)


def move_right(update, context):
    a_player.move_right()
    draw_board(update, context)


updater.dispatcher.add_handler(CommandHandler('show', draw_board))
updater.dispatcher.add_handler(CommandHandler('begin', begin_game))
updater.dispatcher.add_handler(CommandHandler('move_up', move_up))
updater.dispatcher.add_handler(CommandHandler('move_down', move_down))
updater.dispatcher.add_handler(CommandHandler('move_left', move_left))
updater.dispatcher.add_handler(CommandHandler('move_right', move_right))

updater.start_polling()
updater.idle()

# <3
