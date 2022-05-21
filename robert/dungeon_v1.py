# Initial variable setups
rooms = 1
treasure_door_open = False


# Game loop
while True:
    # Main Menu
    while rooms == 1:
        print('Case Dungeon')
        print('What is your name?\n')

        name = input('> ').lower().capitalize()
        directions = ['North', 'East', 'South', 'West']

        print('-------------------------------\n')
        print(f'Welcome, {name}!\n\nTo navigate, type the following commands {directions}.\nGot it memorized?\n')

        response = input('> ').lower()

        if 'y' in response:
            print('-------------------------------\n')
            print("You travel east, entering the cave. The smell of rotting flesh fills your nose... Definitely a goblin's nest...")
            
            rooms = 2

        elif 'n' in response:
            rooms = 1

        else:
            print('Unacceptable answer...')
            print('Try again\n')

    # Cave Entrance
    while rooms == 2:
        print('Choose your direction:\n')

        action = input('> ').lower()

        if 'north' in action:
            print('-------------------------------\n')
            print('Nothing but bloody tattered clothes.')

        elif 'east' in action:
            print('-------------------------------\n')
            print('You begin travling futher into the cave. You find yourself in a large open room.')

            rooms = 3
            break
            
        elif 'south' in action:
            print('-------------------------------\n')
            print('A pole staked in the ground impaling a decapitated head.')

        elif 'west' in action:
            print('-------------------------------\n')
            print('As you start exiting the cave, you are jumped by a man in full knight armor.')
            print('As he plunges his sword through your heart, he says "COWARD!!".\n')
            print('Try again?\n')
            response = input('> ').lower()

            if 'y' in response:
                rooms = 1
                break

            else:
                quit()
        else:
            print('Unknown command')

    # Open room
    while rooms == 3:
        print('Choose your direction:\n')
        action = input('> ').lower()

        if 'north' in action:
            print('-------------------------------\n')
            print('You make your way north and find a set of levers on the wall.')
            print('There are 3 levers lined up horizontally.')
            print('Do you pull one of the levers?\n')

            action = input('> ').lower()

            if 'y' in action:
                print('-------------------------------\n')
                print('Which lever do you pull? Left, middle, right or none?\n')

                action = input('> ').lower()

                if 'left' in action:
                    rooms = 4
                    break

                elif 'middle' in action:
                    rooms = 5
                    break

                elif 'right' in action:
                    print('You hear a clicking sound east of where you are.')
                    treasure_door_open = True

                else:
                    rooms = 3

            elif 'n' in action:
                rooms = 3

            else:
                print("Unknown command")
        
        elif 'east' in action:
            if treasure_door_open == True:
                rooms = 6

            elif treasure_door_open == False:
                print('-------------------------------\n')
                print("There is a massive metal reinforced door. It looks to be locked by a mechanism.")
                print('Look around for a way to open it and come back.')

                rooms = 3

        elif 'south' in action: # ADD CONTENT
            print('-------------------------------\n')
            print('Just a blank rock wall')

            rooms = 3

        elif 'west' in action: # ADD CONTENT
            print('-------------------------------\n')
            print("That's where you came from, you have to find the treasure!")

            rooms = 3

        else:
            print('-------------------------------\n')
            
            rooms = 3
    break

while rooms == 4:
    print('You feel a drop of water hit your forehead.  As you look up')
    print('water begins filling the room and the door shuts behind you.')
    print('\nYou have drowned.\n')

    rooms = 0
    break

while rooms == 5:
    print('You hear rocks crumbling above you and before you can react')
    print('a large boulder falls upon you')
    print('\nYou are now a waffle.\n')

    rooms = 0
    break

while rooms == 6:
    print('As you go to open the door, it has no resistance and opens up.')
    print('Almost blinded by the shimmering light reflecting off the treasure,')
    print('You jump with joy as you haul all you can and leave the cave.')
    print('Just becareful for the goblins that followed you the whole way here...\n')

    print('Thanks for playing!\n')

    quit()


while rooms == 0:
    print('Continue?')

    action = input('> ').lower()

    if 'y' in action:
        rooms = 1
        break

    elif 'n' in action:
        print('Game Over')
        quit()

    break

