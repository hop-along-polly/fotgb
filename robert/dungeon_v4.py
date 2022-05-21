import os
import time

class Player:
    def __init__(self, name, location):
        self.name = name
        self.location = location


class Region:
    def __init__(self, description):
        self.description = description
    

EastBlue = Region('')
WestBlue = Region(' ')
SouthBlue = Region(' ')
NorthBlue = Region(' ')


print(f'What is your name, adventurer?\n')

Player.name = input('> ').lower().capitalize()

os.system('cls')

print(f'Welcome, {Player.name}!')

time.sleep(3)
os.system('cls')

while True:
    pass
