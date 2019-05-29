

class Equip:
    def __init__(self, name, description):
        self.name = name
        self.description = description 

    def __repr__(self):
        return f"Your equipment - {self.name}, {self.description}"