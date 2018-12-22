from helpers import print_text_fancily, print_title_fancily
from Stats import Stats
from Avatar import WarriorAvatar
from Backpack import Backpack, Equipments


class Player:
    def __init__(self, name):
        self.name = name
        self.skill_tree = None
        self.skill_point = 0
        self.stats = Stats(self)
        self.avatar = WarriorAvatar()
        self.backpack = Backpack(self)
        self.equipments = Equipments(self)

    def draw_player_avatar(self):
        print_title_fancily(None, "player avatar")
        self.avatar.show_avatar()

    def draw_player_skill_tree(self):
        self.skill_tree.show()

    def show_player_stats(self):
        self.stats.print_all_stats()
        print()
