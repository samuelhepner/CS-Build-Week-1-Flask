# Implement a class to hold room information. This should have name and
# description attributes.

from store import Store

class Room:
    def __init__(self, name, description, id=0, x=None, y=None, items=[], store=None):
        self.id = id
        self.name = name
        self.description = description
        self.n_to = None
        self.s_to = None
        self.e_to = None
        self.w_to = None
        self.x = x
        self.y = y
        self.items = items
        self.store = store

    def get_exits(self):
        exits = []
        if self.n_to is not None:
            exits.append("n")
        if self.s_to is not None:
            exits.append("s")
        if self.w_to is not None:
            exits.append("w")
        if self.e_to is not None:
            exits.append("e")
        return exits
    
    def get_items(self):
        item_names = []
        for item in self.items:
            item_names.append(item.name)
        return item_names

    def connect_rooms(self, direction, connecting_room):
        if direction == "n":
            self.n_to = connecting_room
            connecting_room.s_to = self
        elif direction == "s":
            self.s_to = connecting_room
            connecting_room.n_to = self
        elif direction == "e":
            self.e_to = connecting_room
            connecting_room.w_to = self
        elif direction == "w":
            self.w_to = connecting_room
            connecting_room.e_to = self
        else:
            print("INVALID ROOM CONNECTION")
            return None

    def get_room_in_direction(self, direction):
        if direction == "n":
            return self.n_to
        elif direction == "s":
            return self.s_to
        elif direction == "e":
            return self.e_to
        elif direction == "w":
            return self.w_to
        else:
            return None

    def get_coords(self):
        return [self.x, self.y]
