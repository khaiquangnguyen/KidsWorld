from pptree import *


class Skill:
    def __init__(self, skill_name, type, value, head=None):
        self.skill_name = skill_name
        self.type = type
        self.description = value
        self.children = []
        if head:
            head.children.append(self)

    def __str__(self):
        return_string = '{}  [{}]: {}'.format(
            self.skill_name.upper(), self.type, self.description)
        return return_string

    def show(self):
        print("-" * 30)
        print()
        print("#--- S K I L L - T R E E ---#")
        print()
        print_tree(self)
        print()


def create_math_skill_tree():
    soul = Skill("Math Soul", "soul", "Math")
    hp_branch = Skill("Geometry", "Soul", "Boost", soul)
    hp_max_leaf = Skill("Max HP++", "Passive", 0, hp_branch)
    hp_regen_leaf = Skill("HP regen++", "Passive", 0, hp_branch)
    second_leaf = Skill("Dmg ++", "Passive", 4, soul)
    third_leaf = Skill("Crit Chance++", "Passive", "10%", soul)
    fourth_leaf = Skill("Crit Dmg++", "Passive", "50%", soul)
    active_one = Skill("Tackle", "Active",
                       "Dmg: 10 | Charges: 20 | Accuracy: 100", soul)
    active_two = Skill("Integral", "Active",
                       "Dmg: 30 | Charges: 5 | Accuracy: 90", soul)
    empty_slot = Node("[   ]", soul)
    empty_slot = Node("[   ]", hp_branch)
    return soul


create_math_skill_tree()
