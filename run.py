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
    option = input("-> ")
    
