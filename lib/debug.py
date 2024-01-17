#!/usr/bin/env python3
import ipdb

from classes.man_to_many import Player
from classes.man_to_many import Game
from classes.man_to_many import Result

if __name__ == '__main__':
    print("HELLO! :) let's debug :vibing_potato:")

    game = Game("Skribbl.io")
    player = Player("Nick")
    result = Result(player, game, 5000)

    ipdb.set_trace()
