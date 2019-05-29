from room import Room
from player import Player
# Declare all the rooms

# equip = {'skeleton''knife''rope''glasses'}

room = {
    'outside':  Room("Outside Cave Entrance", "North of you, the cave mount beckons", 'rock'),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""",'match'),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""",'key'),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""",'rope'),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it appears to be empty.""",'skeleton'),

    'stairway': Room("Dark Stair Case", """You've found a stair case, 
looks like the only way to go is north!""",'knife'),

    'secretroom': Room("Secret Room", """This room is completely empty, why is it even here?""",'glasses'),

    'realtreasureroom': Room("Secret Treasure Chamber", """You've found the long-lost treasure
chamber! Enough gold to last you 1,000 life times. You're a true explorer!!!""",'torch')
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']
room['treasure'].d_to = room['stairway']
room['stairway'].u_to = room['treasure']
room['stairway'].n_to = room['secretroom']
room['secretroom'].s_to = room['stairway']
room['secretroom'].k_to = room['realtreasureroom']

player = Player(room['outside'])

def direction_successful(direction, current_room):
    attribute = direction + "_to"

    if hasattr(current_room, attribute):
        return getattr(current_room, attribute)
    elif(attribute == "q_to"):
        return
    else:
        print("You can't go that way")
        return current_room

while True:
    print(player.current_room.name)
    print(player.current_room.description)
    print(player.current_room.equipment)

    player_input = input("\n>").lower().split()
    
    if len(player_input) == 1:
        player_input = player_input[0][0]    
        player.current_room = direction_successful(player_input, player.current_room)
        if player_input == "q":
            print("Thanks for playing!!!") 
            break

    elif len(player_input) == 2:
        first_word = player_input[0]
        second_word = player_input[1]




    # if player_input == 'n':
    #     player.current_room = player.current_room.n_to
    # elif player_input == 's':
    #     player.current_room = player.current_room.s_to
    # elif player_input == 'w':
    #     player.current_room = player.current_room.w_to
    # elif player_input == 'e':
    #     player.current_room = player.current_room.e_to
    # else:
    #     print("Not a valid direction")


    # If the user enters a cardinal direction, attempt to move to the room there.
    
    
    # Print an error message if the movement isn't allowed.
    
    
    
    # If the user enters "q", quit the game.
