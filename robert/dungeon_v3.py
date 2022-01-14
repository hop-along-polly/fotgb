# OS module for using CMD command to clear terminal for better viewing
import os

# User to store player data and reuse throughout the program.
class Player:
    def __init__(self, name, room_name):
        self.name = name
        self.position = room_name

# Used to create rooms that the player can travel to and from.
class Room:
    def __init__(self, name, pos_x, pos_y, text):
        self.name = name 
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.text = text

# Main program loop
while True:
    os.system('cls')
    title_menu = Room('Title Menu', 0, 0, 'What is your name?\n')
    print(title_menu.text)

    Player.name = input(' > ').lower().capitalize()
    os.system('cls')

    print(f'Welcome, {Player.name}\n')

    # Cave Entrance
    cave_entrance = Room('Cave Entrance', 1, 0, 'Most do not complete or return from this maze. Good luck...\n')

    location = cave_entrance.name
        
    print(f'You are now in: {location}\n')
    print(cave_entrance.text)
    action = input('Which direction do you go?\n > ').lower()

    def first_encounter():

        if 'north' in action:

            cave_entrance = Room('Cave Entrance', 1, 0, 'Most do not complete or return from this maze. Good luck...\n')

        elif 'east' in action:

            inner_room = Room('Inner Room', 2, 0, 'This is the inner room.')
            print('You travel further into the cave.')
            print(inner_room.text)

        elif 'south' in action:

            print('South')

        elif 'west' in action:

            print('West')

        else:

            print('inncorrect response.')

    break
