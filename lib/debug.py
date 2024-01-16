#!/usr/bin/env python3
import ipdb

from classes.player import Player
from classes.game import Game
from classes.result import Result

if __name__ == '__main__':
    print("HELLO! :) let's debug :vibing_potato:")

    game = Game("Skribbl.io")
    player = Player("Nick")
    result = Result(player, game, 5000)

    ipdb.set_trace()
