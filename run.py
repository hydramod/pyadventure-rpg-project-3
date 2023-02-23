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
COMPLETE = False
UP = "up", "north"
DOWN = "down", "south"
LEFT = "left", "west"
RIGHT = "right", "east"

completed_areas = {"home": {"bedroom": False,
                            "atrium": False,
                            "kitchen": False,
                            "bathroom": False,
                            "study": False},
                   "outside": {"yard": False,
                               "road": False},
                   "forest": {"river": False,
                              "cabin": False,
                              "cave": False},
                   "castle": {"great hall": False,
                              "living_quarters": False,
                              "kitchen": False,
                              "gaurds room": False,
                              "dungeons": False,
                              "stables": False,
                              "courtyards": False,
                              "tower": False,
                              "gatehouse": False,
                              "gardens": False}
                   }

areamap = {completed_areas[home][bedroom]: {ZONENAME: ""
                                            DESCRIPTION = "description"
                                            INFO = "inspect"
                                            COMPLETE = False
                                            UP = "up", "north"
                                            DOWN = "down", "south"
                                            LEFT = "left", "west"
                                            RIGHT = "right", "east"},
           completed_areas[home][atrium]: {ZONENAME: ""
                                           DESCRIPTION = "description"
                                           INFO = "inspect"
                                           COMPLETE = False
                                           UP = "up", "north"
                                           DOWN = "down", "south"
                                           LEFT = "left", "west"
                                           RIGHT = "right", "east"},
           completed_areas[home][kitchen]: {ZONENAME: ""
                                            DESCRIPTION = "description"
                                            INFO = "inspect"
                                            COMPLETE = False
                                            UP = "up", "north"
                                            DOWN = "down", "south"
                                            LEFT = "left", "west"
                                            RIGHT = "right", "east"},
           completed_areas[home][bathroom]: {ZONENAME: ""
                                             DESCRIPTION = "description"
                                             INFO = "inspect"
                                             COMPLETE = False
                                             UP = "up", "north"
                                             DOWN = "down", "south"
                                             LEFT = "left", "west"
                                             RIGHT = "right", "east"},
           completed_areas[home][study]: {ZONENAME: ""
                                          DESCRIPTION = "description"
                                          INFO = "inspect"
                                          COMPLETE = False
                                          UP = "up", "north"
                                          DOWN = "down", "south"
                                          LEFT = "left", "west"
                                          RIGHT = "right", "east"},
           completed_areas[outside][yard]: {ZONENAME: ""
                                            DESCRIPTION = "description"
                                            INFO = "inspect"
                                            COMPLETE = False
                                            UP = "up", "north"
                                            DOWN = "down", "south"
                                            LEFT = "left", "west"
                                            RIGHT = "right", "east"},
           completed_areas[outside][road]: {ZONENAME: ""
                                            DESCRIPTION = "description"
                                            INFO = "inspect"
                                            COMPLETE = False
                                            UP = "up", "north"
                                            DOWN = "down", "south"
                                            LEFT = "left", "west"
                                            RIGHT = "right", "east"},
           completed_areas[forest][river]: {ZONENAME: ""
                                            DESCRIPTION = "description"
                                            INFO = "inspect"
                                            COMPLETE = False
                                            UP = "up", "north"
                                            DOWN = "down", "south"
                                            LEFT = "left", "west"
                                            RIGHT = "right", "east"},
           completed_areas[forest][cabin]: {ZONENAME: ""
                                            DESCRIPTION = "description"
                                            INFO = "inspect"
                                            COMPLETE = False
                                            UP = "up", "north"
                                            DOWN = "down", "south"
                                            LEFT = "left", "west"
                                            RIGHT = "right", "east"},
           completed_areas[forest][cave]: {ZONENAME: ""
                                           DESCRIPTION = "description"
                                           INFO = "inspect"
                                           COMPLETE = False
                                           UP = "up", "north"
                                           DOWN = "down", "south"
                                           LEFT = "left", "west"
                                           RIGHT = "right", "east"},
           completed_areas[castle][great hall]: {ZONENAME: ""
                                                 DESCRIPTION = "description"
                                                 INFO = "inspect"
                                                 COMPLETE = False
                                                 UP = "up", "north"
                                                 DOWN = "down", "south"
                                                 LEFT = "left", "west"
                                                 RIGHT = "right", "east"},
           completed_areas[castle][living quarters]: {ZONENAME: ""
                                                      DESCRIPTION = "description"
                                                      INFO = "inspect"
                                                      COMPLETE = False
                                                      UP = "up", "north"
                                                      DOWN = "down", "south"
                                                      LEFT = "left", "west"
                                                      RIGHT = "right", "east"},
           completed_areas[castle][kitchen]: {ZONENAME: ""
                                              DESCRIPTION = "description"
                                              INFO = "inspect"
                                              COMPLETE = False
                                              UP = "up", "north"
                                              DOWN = "down", "south"
                                              LEFT = "left", "west"
                                              RIGHT = "right", "east"},
           completed_areas[castle][gaurds room]: {ZONENAME: ""
                                                  DESCRIPTION = "description"
                                                  INFO = "inspect"
                                                  COMPLETE = False
                                                  UP = "up", "north"
                                                  DOWN = "down", "south"
                                                  LEFT = "left", "west"
                                                  RIGHT = "right", "east"},
           completed_areas[castle][dungeons]: {ZONENAME: ""
                                               DESCRIPTION = "description"
                                               INFO = "inspect"
                                               COMPLETE = False
                                               UP = "up", "north"
                                               DOWN = "down", "south"
                                               LEFT = "left", "west"
                                               RIGHT = "right", "east"},
           completed_areas[castle][stables]: {ZONENAME: ""
                                              DESCRIPTION = "description"
                                              INFO = "inspect"
                                              COMPLETE = False
                                              UP = "up", "north"
                                              DOWN = "down", "south"
                                              LEFT = "left", "west"
                                              RIGHT = "right", "east"},
           completed_areas[castle][courtyards]: {ZONENAME: ""
                                                 DESCRIPTION = "description"
                                                 INFO = "inspect"
                                                 COMPLETE = False
                                                 UP = "up", "north"
                                                 DOWN = "down", "south"
                                                 LEFT = "left", "west"
                                                 RIGHT = "right", "east"},
           completed_areas[castle][tower]: {ZONENAME: ""
                                            DESCRIPTION = "description"
                                            INFO = "inspect"
                                            COMPLETE = False
                                            UP = "up", "north"
                                            DOWN = "down", "south"
                                            LEFT = "left", "west"
                                            RIGHT = "right", "east"},
           completed_areas[castle][gatehouse]: {ZONENAME: ""
                                                DESCRIPTION = "description"
                                                INFO = "inspect"
                                                COMPLETE = False
                                                UP = "up", "north"
                                                DOWN = "down", "south"
                                                LEFT = "left", "west"
                                                RIGHT = "right", "east"},
           completed_areas[castle][gardens]: {ZONENAME: ""
                                              DESCRIPTION = "description"
                                              INFO = "inspect"
                                              COMPLETE = False
                                              UP = "up", "north"
                                              DOWN = "down", "south"
                                              LEFT = "left", "west"
                                              RIGHT = "right", "east"}
           }


def main():
    """
    Runs main game functions
    """
    title_screen()
    help_menu()


main()
