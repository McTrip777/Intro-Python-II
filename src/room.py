# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    def __init__(self, name, description, equipment):
        self.name = name
        self.description = description 
        self.equipment = equipment 

    def __repr__(self):
        return f"{self.name}, {self.description}"