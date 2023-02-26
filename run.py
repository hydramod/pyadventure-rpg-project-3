import cmd
import textwrap
import sys
import os
import time
import random


class player_setup:
    """
    Initial player setup, health points, mana points and status effects
    """

    def __init__(self):
        self.name = ""
        self.health = 0
        self.mana = 0
        self.status = []
        self.location = "home"


player = player_setup()


def title_menu():
    """
    Controls the title menu screen options
    """
    options = {
        "play": start,
        "help": help_menu,
        "quit": sys.exit,
    }

    while True:
        option = input("-> ").lower()
        if option in options:
            options[option]()
        else:
            print("Invalid command!\nEnter a valid command:")


def title_screen():
    """
    Prints title screen
    """
    os.system("clear")
    print("*#" * 21)
    print("*#{:^39}#*".format("WELCOME TO PYADVENTURE RPG"))
    print("*#" * 21)
    print("{:^43}".format("<- Play ->"))
    print("{:^43}".format("<- Help ->"))
    print("{:^43}".format("<- Quit ->"))
    print("{:^43}".format("Copyright 2023 Ali Saeid"))

    title_menu()


def help_menu():
    print("*#" * 21)
    print("*#{:^39}*#".format("HELP"))
    print("*#" * 21)
    print("{:^43}".format("<- Use UP, DOWN, LEFT, RIGHT to move ->"))
    print("{:^43}".format("<-   Type your commands to do them   ->"))
    print("{:^43}".format("<-  Use examine to inspect something ->"))
    print("{:^43}".format("<-      Have fun and good luck       ->"))

    title_menu()


def start():
    """
    Handles game functions
    """

"""
Game Map

+----+----+----+----+----+----+----+----+----+----+----+
| a1 | b1 | c1 | d1 | e1 | f1 | g1 | h1 | i1 | j1 | k1 |
+----+----+----+----+----+----+----+----+----+----+----+
| a2 | b2 | c2 | d2 | e2 | f2 | g2 | h2 | i2 | j2 | k2 |
+----+----+----+----+----+----+----+----+----+----+----+
| a3 | b3 | c3 | d3 | e3 | f3 | g3 | h3 | i3 | j3 | k3 |
+----+----+----+----+----+----+----+----+----+----+----+
| a4 | b4 | c4 | d4 | e4 | f4 | g4 | h4 | i4 | j4 | k4 |
+----+----+----+----+----+----+----+----+----+----+----+
| a5 | b5 | c5 | d5 | e5 | f5 | g5 | h5 | i5 | j5 | k5 |
+----+----+----+----+----+----+----+----+----+----+----+
| a6 | b6 | c6 | d6 | e6 | f6 | g6 | h6 | i6 | j6 | k6 |
+----+----+----+----+----+----+----+----+----+----+----+
| a7 | b7 | c7 | d7 | e7 | f7 | g7 | h7 | i7 | j7 | k7 |
+----+----+----+----+----+----+----+----+----+----+----+
| a8 | b8 | c8 | d8 | e8 | f8 | g8 | h8 | i8 | j8 | k8 |
+----+----+----+----+----+----+----+----+----+----+----+
| a9 | b9 | c9 | d9 | e9 | f9 | g9 | h9 | i9 | j9 | k9 |
+----+----+----+----+----+----+----+----+----+----+----+
|a10 |b10 |c10 |d10 |e10 |f10 |g10 |h10 |i10 |j10 |k10 |
+----+----+----+----+----+----+----+----+----+----+----+
|a11 |b11 |c11 |d11 |e11 |f11 |g11 |h11 |i11 |j11 |k11 |
+----+----+----+----+----+----+----+----+----+----+----+
"""

AREANAME = ""
DESCRIPTION = "description"
INFO = "inspect"
COMPLETE = False
UP = "up", "north"
DOWN = "down", "south"
LEFT = "left", "west"
RIGHT = "right", "east"

completed_areas = {
    "home": {
        "a1" : {"bedroom": False},
        "a2" : {"atrium": False},
        "b2" : {"atrium": False},
        "c2" : {"atrium": False},
        "d2" : {"atrium": False},
        "a3" : {"kitchen": False},
        "b1" : {"bathroom": False},
        "c1" : {"study": False},
        "a3" : {"yard": False},
        "a4" : {"yard": False},
        "a5" : {"yard": False},
        "b3" : {"yard": False},
        "b4" : {"yard": False},
        "b5" : {"yard": False},
        "c3" : {"yard": False},
        "c4" : {"yard": False},
        "c5" : {"yard": False},
        "e3" : {"yard": False},
        "e4" : {"yard": False},
        "e5" : {"yard": False},
        "d3" : {"garden" :False},
        "d4" : {"garden" :False},
        "d5" : {"garden" :False}
    },
    "outside": {
        "a6" : {"road": False},
        "b6" : {"road": False},
        "c6" : {"road": False},
        "d6" : {"road": False},
        "e6" : {"road": False},
        "g6" : {"road": False},
        "e1" : {"rood": False},
        "e2" : {"rood": False},
        "e3" : {"rood": False},
        "e4" : {"rood": False},
        "e5" : {"rood": False},
        "e6" : {"road": False},
        "f6" : {"road": False},
        "f7" : {"rood": False},
        "f8" : {"rood": False},
        "f9" : {"rood": False},
        "f10" : {"rood": False},
        "f11" : {"rood": False},
        "h6" : {"road": False},
        "i6" : {"road": False},
        "j6" : {"road": False},
        "k6" : {"road": False}
    },
    "forest": {
        "c7" : {"forest path": False},
        "c8" : {"forest path": False},
        "c9" : {"forest path": False},
        "c10" : {"forest path": False},
        "c11" : {"forest path": False},
        "a9" : {"river": False},
        "b9" : {"river": False},
        "d9" : {"river": False},
        "e9" : {"river": False},
        "a7" : {"cabin": False},
        "a8" : {"cabin": False},
        "b7" : {"cabin": False},
        "b8" : {"cabin": False},
        "a10" : {"cave": False},
        "a11" : {"cave": False},
        "b10" : {"cave": False},
        "b11" : {"cave": False},
        "d7" : {"outpost": False},
        "d8" : {"outpost": False},
        "e7" : {"outpost": False},
        "e8" : {"outpost": False},
        "d10" : {"meadow": False},
        "d11" : {"meadow": False},
        "e10" : {"meadow": False},
        "e11" : {"meadow": False}
    },
    "castle": {
        "j8" : {"great hall": False},
        "j9" : {"great hall": False},
        "j7" : {"living quarters": False},
        "k9" : {"kitchen": False},
        "d4" : {"guards room": False},
        "k10" : {"dungeons": False},
        "k11" : {"dungeons": False},
        "h7" : {"stables": False},
        "h8" : {"courtyards": False},
        "h10" : {"courtyards": False},
        "h11" : {"courtyards": False},
        "i7" : {"gaurd tower": False},
        "i8" : {"courtyards": False},
        "i9" : {"courtyards": False},
        "i10" : {"courtyards": False},
        "i11" : {"courtyards": False},
        "j10" : {"courtyards": False},
        "j11" : {"tower": False},
        "d9" : {"gatehouse": False},
        "k7" : {"gardens": False},
        "k8" : {"gardens": False}
    }
}

areamap = {}
for area, subareas in completed_areas.items():
    for subarea, is_completed in subareas.items():
        areamap[subarea] = {
            "AREANAME": f"{area}: {list(is_completed.keys())[0]}",
            "DESCRIPTION": "description",
            "INFO": "inspect",
            "COMPLETE": False,
            "UP": ["up", "north"],
            "DOWN": ["down", "south"],
            "LEFT": ["left", "west"],
            "RIGHT": ["right", "east"]
        }
        print(subarea + ':', areamap[subarea])


def main():
    """
    Runs main game functions
    """
    title_screen()
    help_menu()

#main()
