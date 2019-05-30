# Write a class to hold player information, e.g. what room they are in
# currently.
from items import Item

class Player:
    def __init__(self, name, starting_room, inventory=[]):
        self.name = name
        self.current_room = starting_room
        self.inventory = [
            Item("match", 'You only have one')
        ]

    def travel(self, direction):
        nextRoom = self.current_room.getRoomInDirection(direction)
        if nextRoom is not None:
            self.current_room = nextRoom
            print(self.current_room)
        else:
            print("You can not move in that direction")