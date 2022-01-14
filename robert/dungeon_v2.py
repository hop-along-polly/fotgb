


# Initiates game loop
while True:
    treasure_room_unlocked = False
    # Cave Entrance Room
    def cave_entrance():
        print('\nLOCATION: Cave Entrance\n')
        print(f'Which direction do you go, {name}?')
        
        action = input('> ').lower() # Action is an action by the player

        if 'north' in action:
            print('\nJust a blank cave wall.\n')
            cave_entrance()
        elif 'east' in action:
            print('\nYou begin on a trail heading deeper into the cave.\n')
            inner_room()
        elif 'south' in action:
            print('\nYou find bloody tattered clothes.\n')
            cave_entrance()
        elif 'west' in action:
            print('\nAs you turn around to exit the cave, you stomach feels cold')
            print('When you look down, you see a blade plunged through you.')
            print('A whisper in your ear says "coward..."\n')
            try_again()
        else:
            print("That's not a correct response.")
            cave_entrance()

    # Try Again
    def try_again():
        print('\nTry Again?\n')

        response = input('> ').lower() # Reponse is a yes or no by the player

        if 'y' in response:
            cave_entrance()
        else:
            quit()

    # Lever Area
    def lever_area():
        print('\nYou see a series of levers.')
        print('3 levers to be exact.')
        print('Do you wish to pull a lever?\n')

        response = input('> ').lower() # Reponse is a yes or no by the player

        if 'y' in response:
            print('\nWhich lever do you pull?')
            print('Left, middle, or right?\n')

            action = input('> ').lower() # Action is an action by the player

            if 'left' in action:
                print('\nA small boulder shoots out, replacing your head...')
                try_again()
            elif 'middle' in action:
                print('\nThe floor beneath you drops...')
                try_again()
            elif 'right' in action:
                print('\nYou hear a clicking sound east of your direction.')
                inner_room()
                return treasure_room_unlocked == True
            else:
                print("That's not a correct response.")
                inner_room()
        else:
            inner_room()
    
    # Treasure Room
    def treasure_room():
        if treasure_room_unlocked == False:
            print('\nThe gate seems to be locked.')
            print('Maybe look around for a lever?\n')
            inner_room()
        elif treasure_room_unlocked == True:
            print('\nYou found the treasure!\n')
            try_again()    

    # Inner Room 
    def inner_room():
        print('\nLOCATION: Inner Room\n')
        
        action = input('> ').lower() # Action is an action by the player

        if 'north' in action:
            lever_area()
        elif 'east' in action:
            print('\nYou see a massive gate.')
            print('Do you try to open it?\n')

            response = input('> ').lower()

            if 'y' in response:
                treasure_room()
            elif 'n' in response:
                inner_room()
            else:
                print("That's not a correct response.")
                inner_room()
        elif 'south' in action:
            print('\nNothin but a blank cave wall here.\n')
            inner_room()
        elif 'west' in action:
            print('\nAs you turn around to exit the cave, you stomach feels cold')
            print('When you look down, you see a blade plunged through you.')
            print('A whisper in your ear says "coward..."\n')
        else:
            print("That's not a correct reponse.")
            inner_room()

    #print('####################')
    print('\nWelcome to Case Dungeon!\n')
    print('What is your name?\n')

    name = input('> ').lower().capitalize()

    print(f'\nHello, {name}!\n')
    print('Enter the commands, "North", "East", "South", or "West" to navigate!\n')

    print('As you enter the cave, you smell the stench of rotting flesh...')

    cave_entrance()

    break
