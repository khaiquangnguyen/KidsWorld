from helpers import print_title_fancily
from pptree import *


STATUS_EFFECTS = ["modify_hp", "modify_defense", "modify_dmg", "modify_evasion",
                  "modify_accuracy", "modify_crit_chance", "modify_crit_mult"]
ACTIVE_EFFECTS = ["deal_dmg", "deal_dmg_ignore_defense",
                  "deal_dmg_ignore_evasion", "deal_dmg_ignore_accuracy", "deal_dmg_crit", "healing"]


class Skill:
    def __init__(self, name, type, effects, description):
        self.name = name
        self.type = type
        # A dictionary of all potential effects of this skill.
        # format is {"modifier_name":(modifer,number_of_turns)}. i.e {"hp":+10,3}
        # For passive skills, the number of turns is -1, implying infinity
        self.effects = effects
        self.description = description

    def get_effects(self):
        return self.effects

    def get_description(self):
        return self.description


class ActiveSkill(Skill):
    def __init__(self, skill_name, effects, description):
        super().__init__(skill_name, "active", effects, description)


class PassiveSkill(Skill):
    def __init__(self, skill_name, effects, description):
        super().__init__(skill_name, "passive", effects, description)



