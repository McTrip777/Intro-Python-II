# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self, current_room):
        self.current_room = current_room
        self.equipment = []

    def addEquipment(self, item):
        self.equipment.append(item)

    def __repr__(self):
        return f"Player is in {self.current_room}"

    def set_current_room(self, new_room):
        self.current_room = new_room