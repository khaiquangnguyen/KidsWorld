from helpers import *
from pptree import *


class Player:
    def __init__(self, name):
        self.name = name
        self.skill_tree = None
        self.skill_point = 0
        self.stats = {
            'dmg': 2,
            'defense': 1,
            'hp': 10,
            'evasion': 0.1,
            'accuracy': 100,
        }
        self.shape = (r"""
 _   _   _   _+       |
/_`-'_`-'_`-'_|  \+/  |
\_`M'_`D'_`C'_| _<=>_ |
  `-' `-' `-' 0/ \ / o=o
              \/\ ^ /`0
              | /_^_\
              | || ||
            __|_d|_|b__

                """)

    def __str__(self):
        return (self.draw_player_avatar())

    def draw_player_avatar(self):
        print("-" * 30)
        print()
        print('#--- P L A Y E R - A V A T A R ---#')
        print()
        shape_by_line = self.shape.split('\n')
        for a_line in shape_by_line:
            print_text_fancily(a_line, 0.005, False)
        return self.shape

    def draw_player_skill_tree(self):
        self.skill_tree.show()

    def show_player_stats(self):
        print("-" * 30)
        print()
        print('#--- P L A Y E R - S T A T S ---#')
        print()
        print("-- Damage: {}".format(self.stats['dmg']))
        print("-- Defense: {}".format(self.stats['defense']))
        print("-- HP: {}".format(self.stats['hp']))
        print("-- Evasion: {}".format(self.stats['evasion']))
        print("-- Accuracy: {}".format(self.stats['accuracy']))
        print()
