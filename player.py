from helpers import print_text_fancily, print_title_fancily
from Stats import Stats
from avatars import SoldierAvatar


class Player:
    def __init__(self, name):
        self.name = name
        self.skill_tree = None
        self.skill_point = 0
        self.stats = Stats(1, 1, 10, 0.1, 0.5)
        self.avatar = SoldierAvatar()
        # A list of effects and modifiers that the player is currently affected with during combat
        # Format is {(modifier_name, modifer_effect,number_of_turns)}. i.e {modify_hp,10,3}
        self.affected_combat_modifiers = []
        self.gold_coins = 0
        self.equipments = {
            "left_hand": None,
            "right_hand": None,
            "foot": None,
            "cape": None,
            "head": None,
            "neck": None,
            "accesories_1": None,
            "accesories_2": None,
            "accesories_3": None,
            "accesories_4": None,
        }

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
