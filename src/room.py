# Implement a class to hold room information. This should have name and
# description attributes.
from items import Item



class Room:
    def __init__(self, name, description, item=[]):
        self.name = name
        self.description = description
        self.item = [
            Item("hammer", "This can be used as a weapon"),
            Item("knife", "A multi purpose tool"),
            Item("rope", "This will be useful"),
            Item("bone", "Not sure how sturdy this is")
        ]
        self.w_to = None
        self.s_to = None
        self.d_to = None
        self.a_to = None

    def __str__(self):
        return f"\n------------------\n\n{self.name}\n\n  {self.description} \n [{self.getRoomExitStr()}]"

    def getRoomInDirection(self, direction):
        if direction == "w":
            return self.w_to
        elif direction == "s":
            return self.s_to
        elif direction == "d":
            return self.d_to
        elif direction == "a":
            return self.a_to

    def getRoomExitStr(self):
        exits = []
        if self.w_to is not None:
            exits.append('w')
        if self.s_to is not None:
            exits.append('s')
        if self.d_to is not None:
            exits.append('d')
        if self.a_to is not None:
            exits.append('a')
        return ", ".join(exits)