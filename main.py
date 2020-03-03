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

a_board = Board()
an_enemy = Enemy("Ogro")
a_player = Player(12,"Guerrero")

a_board.cells[0][0] = a_player
a_board.cells[9][9] = an_enemy


def draw_board(update, context):
	update.message.reply_text(str(a_board))

updater.dispatcher.add_handler(CommandHandler('show', draw_board))

updater.start_polling()
updater.idle()

#<3