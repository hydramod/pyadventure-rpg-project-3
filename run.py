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

+----+----+----+----+----+----+----+----+----+----+
| a1 | b1 | c1 | d1 | e1 | f1 | g1 | h1 | i1 | j1 |
+----+----+----+----+----+----+----+----+----+----+
| a2 | b2 | c2 | d2 | e2 | f2 | g2 | h2 | i2 | j2 |
+----+----+----+----+----+----+----+----+----+----+
| a3 | b3 | c3 | d3 | e3 | f3 | g3 | h3 | i3 | j3 |
+----+----+----+----+----+----+----+----+----+----+
| a4 | b4 | c4 | d4 | e4 | f4 | g4 | h4 | i4 | j4 |
+----+----+----+----+----+----+----+----+----+----+
| a5 | b5 | c5 | d5 | e5 | f5 | g5 | h5 | i5 | j5 |
+----+----+----+----+----+----+----+----+----+----+
| a6 | b6 | c6 | d6 | e6 | f6 | g6 | h6 | i6 | j6 |
+----+----+----+----+----+----+----+----+----+----+
| a7 | b7 | c7 | d7 | e7 | f7 | g7 | h7 | i7 | j7 |
+----+----+----+----+----+----+----+----+----+----+
| a8 | b8 | c8 | d8 | e8 | f8 | g8 | h8 | i8 | j8 |
+----+----+----+----+----+----+----+----+----+----+
| a9 | b9 | c9 | d9 | e9 | f9 | g9 | h9 | i9 | j9 |
+----+----+----+----+----+----+----+----+----+----+
|a10 |b10 |c10 |d10 |e10 |f10 |g10 |h10 |i10 |j10 |
+----+----+----+----+----+----+----+----+----+----+

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
        "a3" : {"kitchen": False},
        "a4" : {"bathroom": False},
        "a5" : {"study": False},
        "a6" : {"yard": False},
        "a7" : {"garden" :False}
        },
    "outside": {
        "b2" : {"road": False},
        "b3" : {"crossroad": False}
    },
    "forest": {
        "c1" : {"river": False},
        "c2" : {"cabin": False},
        "c3" : {"cave": False}
    },
    "castle": {
        "d1" : {"great hall": False},
        "d2" : {"living quarters": False},
        "d3" : {"kitchen": False},
        "d4" : {"guards room": False},
        "d5" : {"dungeons": False},
        "d6" : {"stables": False},
        "d7" : {"courtyards": False},
        "d8" : {"tower": False},
        "d9" : {"gatehouse": False},
        "d10" : {"gardens": False}
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
