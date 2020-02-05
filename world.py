from room import Room
from player import Player
from store import Store
from items import Item, Weapon, Food
import random
import math
import bcrypt
import pandas as pd


# levels = pd.read_csv('room-info.csv')
# for i in range(len(levels)):
#     print(levels[i]['name'], levels[i]['description'][i])

item_list = [Item('Pile of Gold', 'Contains several coins', 20),
            Item('Ring', 'Size 8', 15), Item('Gem', 'Beautifully polished', 50),
            Item('Crown', 'Used to adorn royalty', 150), Item('Scroll', 'Just says kek', 1),
            Item('Potion', 'Used to increase health', 25), Item('Dice', 'YAHTZEE!', 2),
            Weapon('Silver Sword', "A Witcher's favorite", 20, 'sword', 100),
            Weapon('Wooden Spear', 'Longer than a sword', 25, 'spear', 15),
            Weapon('Wooden Shield', 'Good against arrows', 13, 'shield', 3),
            Weapon('Heavy Book', 'Use the power of knowledge!', 5, 'Book', 1),
            Weapon('Thick rope', 'Very short range weapon', 2, 'rope', 60),
            Weapon('Battle Axe', 'Small stick, big blade', 20, 'axe', 25),
            Food('Apple', 'Red fruit', 2, 'small', 5), Food('Mushroom', 'Probably not poisoned', 1, 'small', 1),
            Food('Root', 'Yum...fiber', 1, 'healthy', 15), Food('Green Leaf', 'You need the nutrients', 1, 'healthy', 15),
            Food('Berries', 'Berries on a stick', 5, 'healthy', 10)]

class World:
    def __init__(self):
        self.starting_room = None
        self.rooms = {}
        self.players = {}
        self.create_world()
        self.password_salt = bcrypt.gensalt()

    def add_player(self, username, password1, password2):
        if password1 != password2:
            return {'error': "Passwords do not match"}
        elif len(username) <= 2:
            return {'error': "Username must be longer than 2 characters"}
        elif len(password1) <= 5:
            return {'error': "Password must be longer than 5 characters"}
        elif self.get_player_by_username(username) is not None:
            return {'error': "Username already exists"}
        password_hash = bcrypt.hashpw(password1.encode(), self.password_salt)
        player = Player(username, self.starting_room, password_hash)
        self.players[player.auth_key] = player
        return {'key': player.auth_key}

    def get_player_by_auth(self, auth_key):
        if auth_key in self.players:
            return self.players[auth_key]
        else:
            return None

    def get_player_by_username(self, username):
        for auth_key in self.players:
            if self.players[auth_key].username == username:
                return self.players[auth_key]
        return None

    def authenticate_user(self, username, password):
        user = self.get_player_by_username(username)
        print('user: ', user)
        if user is None:
            return None
        password_hash = bcrypt.hashpw(password.encode() ,self.password_salt)
        if user.password_hash == password_hash:
            return {'key': user.auth_key}
        return None

    def create_world(self):
        # UPDATE THIS:
        # Should create 100 procuedurally generated rooms
        self.rooms = {
            'outside':  Room("Outside Cave Entrance",
                             "North of you, the cave mount beckons", 1, 1, 1, items=[Item('Torch', 'Lights the way', price=1)]),

            'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
        passages run north and east.""", 2, 1, 2, items=[Item('Torch', 'Lights the way', price=1)], store=Store()),

            'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
        into the darkness. Ahead to the north, a light flickers in
        the distance, but there is no way across the chasm.""", 3, 1, 3),

            'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
        to north. The smell of gold permeates the air.""", 4, 2, 2),

            'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
        chamber! Sadly, it has already been completely emptied by
        earlier adventurers. The only exit is to the south.""", 5, 2, 3),
        }

        # Link rooms together
        self.rooms['outside'].connect_rooms('n', self.rooms['foyer'])
        self.rooms['foyer'].connect_rooms('n', self.rooms['overlook'])
        self.rooms['foyer'].connect_rooms('e', self.rooms['narrow'])
        self.rooms['narrow'].connect_rooms('n', self.rooms['treasure'])

        self.starting_room = self.rooms['outside']


    def print_rooms(self):
        '''
        Print the rooms in room_grid in ascii characters.
        '''
        # Add top border
        str = "# " * ((3 + self.width * 5) // 2) + "\n"
        # The console prints top to bottom but our array is arranged
        # bottom to top.
        #
        # We reverse it so it draws in the right direction.
        reverse_grid = list(self.grid) # make a copy of the list
        reverse_grid.reverse()
        for row in reverse_grid:
            # PRINT NORTH CONNECTION ROW
            str += "#"
            for room in row:
                if room is not None and room.n_to != 0:
                    str += "  |  "
                else:
                    str += "     "
            str += "#\n"
            # PRINT ROOM ROW
            str += "#"
            for room in row:
                if room is not None and room.w_to != 0:
                    str += "-"
                else:
                    str += " "
                if room is not None:
                    str += f"{room.id}".zfill(3)
                else:
                    str += "   "
                if room is not None and room.e_to != 0:
                    str += "-"
                else:
                    str += " "
            str += "#\n"
            # PRINT SOUTH CONNECTION ROW
            str += "#"
            for room in row:
                if room is not None and room.s_to != 0:
                    str += "  |  "
                else:
                    str += "     "
            str += "#\n"
        # Add bottom border
        str += "# " * ((3 + self.width * 5) // 2) + "\n"
        # Print string
        print(str)
