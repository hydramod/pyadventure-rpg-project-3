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


AREANAME = ""
DESCRIPTION = "description"
INFO = "inspect"
SOLVED = False
UP = "up", "north"
DOWN = "down", "south"
LEFT = "left", "west"
RIGHT = "right", "east"

completed_areas = {"home": {"bedroom": False, "atrium": False, "kitchen": False, "bathroom": False, "study": False, "yard": False},
                "outside": {"yard": False, "road": False},
                "forest": {"river": False, "cabin": False, "cave": False},
                "castle": {"great hall": False, "living_quarters": False, "kitchens": False, "gaurds room": False, "dungeons": False,
                           "stables": False, "courtyards": False, "Towers Tall": False, "gatehouse": False, "gardens": False}
                }

areamap = {""}

def main():
    """
    Runs main game functions
    """
    title_screen()
    help_menu()


main()
