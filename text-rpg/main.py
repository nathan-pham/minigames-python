import os
import sys
import cmd
import time
import random
import textwrap

screen_width = 100

# Initialize player
class Player:
    def __init__(self):
        self.name = ""
        self.hp = 0
        self.mp = 0
        self.status_effects = []

user = Player()

def start_game():
    print("start game")

def help_menu():
    print("Interact with the world using simple commands like up, down, right, left, and look.")
    print("Good luck and have fun!")
    title_screen()

def exit_game():
    sys.exit()

def title_screen():
    print("Welcome to the Text RPG!")
    print("        - play -        ")
    print("        - help -        ")
    print("        - exit -        ")
    title_options()

def title_options():
    options = {
        "play": start_game,
        "help": help_menu,
        "exit": exit_game
    }
    option = input("> ").lower()
    while option not in options:
        print(f"Enter a valid option: { ', '.join(list(options)) }.")
        option = input("> ").lower()
    options[option]()


