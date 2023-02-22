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


player = player_setup()


def title_menu():
    """
    Controls the title menu screen options
    """
    options = {
        "play": start,
        "help": help,
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
    print("*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#")
    print("*#   WELCOME TO PYADVENTURE RPG   #*")
    print("*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#")
    print("             <- Play ->             ")
    print("             <- Help ->             ")
    print("             <- Quit ->             ")
    print("      Copyright 2023 Ali Saeid      ")
    title_menu()


def help_menu():
    print("*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*")
    print("*#     WELCOME TO PYADVENTURE RPG    #*")
    print("*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*")
    print("<- Use UP, DOWN, LEFT, RIGHT to move ->")
    print("<-   Type your commands to do them   ->")
    print("<-  Use examine to inspect something ->")
    print("<-      Have fun and good luck       ->")
    title_menu()


def main():
    """
    Runs game functions
    """
    title_screen()
