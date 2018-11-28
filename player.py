from helpers import print_text_fancily, print_title_fancily
from Stats import Stats
from avatars import SoldierAvatar

class Equipments:
    def __init__(self, owner):
        """ Modelled after heroes 3
        """
        self.owner = owner
        self.left_hand = None
        self.right_hand = None
        self.feet = None
        self.head = None
        self.cape = None
        self.belt = None
        self.accesories_1 = None
        self.accesories_2 = None
        self.accesories_3 = None
        self.accesories_4 = None
        self.accesories_5 = None
    
    def equip(self,slot,item):
        if getattr(self,slot) is None:
            setattr(self,slot, item)
            return 1
        else:
            return -1

    def unequip(self,slot):
        # if backpack is full, return error
        if self.owner.backpack.is_full():
            return -1
        item = getattr(self,slot)
        setattr(self,slot,None)
        # add the item to the backpack
        self.owner.backpack.add_item(item)
        return item
    
    def swap(self,slot, backpack_slot):
        item = self.unequip(slot)
        backpack_item = self.owner.backpack.get_item_by_slot(backpack_slot)
        # check if we can equip the new item 
        if self.equip(slot,item) == 1:
            # add return the item to backpack
            self.owner.backpack.add_item(item)
            return 1
        else:
            # something goes wrong. Return the item to backpack
            self.owner.backpack.add_item(backpack_item)
            self.equip(item)
            return -1
        




class Player:
    def __init__(self, name):
        self.name = name
        self.skill_tree = None
        self.skill_point = 0
        self.stats = Stats(self, 1, 1, 10, 0.1, 0.5)
        self.avatar = SoldierAvatar()
        # A list of effects and modifiers that the player is currently affected with during combat
        # Format is {(modifier_name, modifer_effect,number_of_turns)}. i.e {modify_hp,10,3}
        self.affected_combat_modifiers = []
        self.gold_coins = 0
        self.backpack = Backpack(self)
        self.equipments = Equipments(self)

    def __str__(self):
        return (self.draw_player_avatar())

    def draw_player_avatar(self):
        print_title_fancily(None, "player avatar")
        self.avatar.show_avatar()

    def draw_player_skill_tree(self):
        self.skill_tree.show()

    def show_player_stats(self):
        print_title_fancily(None, "player stats")
        self.stats.print_all_stats()
        print()
