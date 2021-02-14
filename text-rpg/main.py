import sys, random

# initialize player
class Player:
    def __init__(self):
        self.name = ""
        self.hp = 100
        self.mp = 0
        self.explored = []
        self.location = [2, 2]
        self.status_effects = []

    def move(self, arguments):
        (direction, directions) = arguments
        if direction == "north" and not directions["north"] == "x":
            self.location[1] -= 1
        elif direction == "south" and not directions["south"] == "x":
            self.location[1] += 1
        elif direction == "west" and not directions["west"] == "x":
            self.location[0] -= 1
        elif direction == "east" and not directions["east"] == "x":
            self.location[0] += 1
        else:
            return print(f"You can't move {direction}.")

        print(f"You moved {direction}.")
    
    def kill(self, arguments):
        print("You killed yourself.")
        exit_game()

    def display_stats(self, arguments):
        print(f"HP: {self.hp}")
        print(f"MP: {self.mp}")

player = Player()

def start_game():
    print("Started the game!")
    print("You are a knight in the middle of an open field. Survive for as long as possible!")
    player.display_stats([])

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
def action(name, callback):
    return {
        "name": name,
        "callback": callback
    }

MAP = [
    ['x', 'x', 'x', 'x', 'x', 'x'],
    ['x', 'o', 'o', 'o', 'o', 'x'],
    ['x', 'o', 'o', 'o', 'o', 'x'],
    ['x', 'o', 'o', 'o', 'o', 'x'],
    ['x', 'o', 'o', 'o', 'o', 'x'],
    ['x', 'c', 'o', 'o', 'o', 'x'],
    ['x', 'o', 'o', 'o', 'o', 'x'],
    ['x', 'o', 'o', 'o', 'o', 'x'],
    ['x', 'o', 'o', 'o', 'o', 'x'],
    ['x', 'x', 'x', 'x', 'x', 'x']
]
MAP_CONSTANTS = {
    "x": {
        "name": "a boundary",
        "actions": ["not move here"]
    },
    "o": {
        "name": "open space",
        "actions": [ "move", "suicide" ]
    },
    "c": {
        "name": "city",
        "actions": []
    }
}

# generate map
def print_map():
    (player_x, player_y) = player.location
    sight = 3
    for y in range(len(MAP)):
        row = MAP[y]
        map_row = []
        random_sides = random.randint(1, sight)
        random_tops = random.randint(1, sight)
        for x in range(len(row)):
            tile = row[x]
            tile_coordinates = f"{y}-{x}"
            zone = (x < player_x + random_sides and x > player_x - random_sides) and (y < player_y + random_tops and y > player_y - random_tops)
            explored = tile_coordinates in player.explored
            
            if explored or zone:
                if player_x == x and player_y == y:
                    map_row.append("P")
                else: 
                    map_row.append(tile)

                if not explored:
                    player.explored.append(tile_coordinates)
            else:
                map_row.append("☁")
            

        print(" ".join(map_row))

    directions = {
        "north": MAP[player_y + 1][player_x],
        "south": MAP[player_y - 1][player_x],
        "west": MAP[player_y][player_x - 1],
        "east": MAP[player_y][player_x + 1]
    }

    for key, value in directions.items():
        constant = MAP_CONSTANTS[value]

        actions = constant["actions"]
        print_actions = ', '.join(actions)

        if len(actions) > 1:
            last_action = actions.pop(len(actions) - 1)
            print_actions = ', '.join(actions) + " or " + last_action

        print(f"To the {key}, there is {constant['name']}. You can {print_actions}.")

    return directions

while True:
    directions = print_map()
    actions = {
        "move": (player.move, True),
        "suicide": (player.kill),
        "refresh": (player.display_stats)
    }

    def prompt():
        arguments = input("> ").split()
        action = arguments.pop(0)
        
        if action not in actions:
            print("That's not a valid action.")
            return prompt()
        else:
            (defined_action, required_arg) = actions[action]

            if required_arg and not len(arguments) > 0:
                print("You need to specify an argument for", action)
                return prompt()

            defined_action(arguments + [directions])
        
    prompt()