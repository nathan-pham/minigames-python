import os
import sys
import cmd
import time
import random
import textwrap

screen_width = 100

# initialize player
class Player:
    def __init__(self):
        self.name = ""
        self.hp = 0
        self.mp = 0
        self.explored = []
        self.location = [1, 1]
        self.status_effects = []

player = Player()

def start_game():
    print("start game")

def help_menu():
    print("Interact with the world using simple commands like up, down, right, left, and look.")
    print("Good luck and have fun!")
    title_screen()

def exit_game():
    sys.exit()

def title_screen():
    print("\nWelcome to the Text RPG!")
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

title_screen()

# map
MAP = [
    ['x', 'x', 'x', 'x', 'x', 'x'],
    ['x', 'o', 'o', 'o', 'o', 'x'],
    ['x', 'o', 'o', 'o', 'o', 'x'],
    ['x', 'o', 'o', 'o', 'o', 'x'],
    ['x', 'o', 'o', 'o', 'o', 'x'],
    ['x', 'o', 'o', 'o', 'o', 'x'],
    ['x', 'o', 'o', 'o', 'o', 'x'],
    ['x', 'o', 'o', 'o', 'o', 'x'],
    ['x', 'o', 'o', 'o', 'o', 'x'],
    ['x', 'x', 'x', 'x', 'x', 'x']
]
MAP_CONSTANTS = {
    "x": "boundary",
    "o": "open_space"
}

# constant commands
# DESCRIPTION = "description"
# EXAMINE = "examine"
# SOLVED = False
# UP = "up", "north"
# DOWN = "down", "south"
# LEFT = "left", "west"
# RIGHT = "right", "east"

# generate map
def print_map():
    (player_x, player_y) = player.location
    sight = 3
    for y in range(len(MAP)):
        row = MAP[y]
        map_row = []
        for x in range(len(row)):
            tile = row[x]
            tile_coordinates = f"{y}-{x}"
            zone = (x < player_x + sight and x > player_x - sight) and (y < player_y + sight and y > player_y - sight)
            explored = tile_coordinates in player.explored

            if explored or zone:
                map_row.append(tile)
                if not explored:
                    player.explored.append(tile_coordinates)
            else:
                map_row.append("-")
            

        print(" ".join(map_row))

    print("===========")

print_map()
player.location = [3, 2]
print_map()