import random
import uuid
from items import Item, Food, Weapon

class Player:
    def __init__(self, name, starting_room, password_hash, coin_purse = 5, inventory = [Item('Scroll', 'Just says kek', 1), Weapon('Rusty Sword', "Don't cut yourself", 5, "Short Sword", 2), Food('Apple', "Yummy", 1, "Fruit", 3)]):
        self.username = name
        self.current_room = starting_room
        self.auth_key = Player.__generate_auth_key()
        self.password_hash = password_hash
        self.uuid = uuid.uuid4
        self.coin_purse = coin_purse
        self.inventory = inventory
     
    def __generate_auth_key():
        digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f']
        auth_key_list = []
        for i in range(40):
            auth_key_list.append(random.choice(digits))
        return "".join(auth_key_list)

    def travel(self, direction, show_rooms = False):
        next_room = self.current_room.get_room_in_direction(direction)
        if next_room is not None:
            self.current_room = next_room
            return True
        else:
            print("You cannot move in that direction.")
            return False
