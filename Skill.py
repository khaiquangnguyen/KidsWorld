from helpers import print_title_fancily
from pptree import print_tree
from collections import namedtuple



# -------------------------------
# 
#     S K I L L - C L A S S 
# 
# -------------------------------
class Skill:
    def __init__(self, name, type, description):
        self.name = name
        self.type = type
        # A dictionary of all potential effects of this skill.
        # format is {"modifier_name":(modifer,number_of_turns)}. i.e {"hp":+10,3}
        # For passive skills, the number of turns is -1, implying infinity
        self.description = description

    def get_description(self):
        return self.description


class ActiveSkill(Skill):
    def __init__(self, skill_name, base_charge, base_accuracy, dmg, status_effects, description):
        super().__init__(skill_name, "active", description)
        self.base_charge = base_charge
        self.base_accuracy = base_accuracy
        self.dmg = dmg
        self.status_effects = status_effects

class ActiveDamageSkill(ActiveSkill):
    def __init__(self, skill_name, base_charge, base_accuracy, dmg, status_effects, description):
        super().__init__(skill_name,base_charge,base_accuracy,dmg,status_effects,description)


class ActiveStatusSkill(ActiveSkill):
    def __init__(self, skill_name, base_charge, base_accuracy, dmg, status_effects, description):
        super().__init__(skill_name,base_charge,base_accuracy,0,status_effects,description)

class ActiveSpecialSkill(ActiveSkill):
    def __init__(self, skill_name, base_charge, base_accuracy, dmg, status_effects, description):
        super().__init__(skill_name,base_charge,base_accuracy,0,status_effects,description)

class PassiveSkill(Skill):
    def __init__(self, skill_name, effects, description):
        super().__init__(skill_name, "passive", description)
        self.effects = effects

class PassiveStatsSkill(PassiveSkill):
    def __init__(self, skill_name, effects, description):
        super().__init__(skill_name, "passive", description)
        self.effects = effects

class PassiveAutoActivateSkill(PassiveSkill):
    def __init__(self, skill_name, effects, description):
        super().__init__(skill_name, "passive", description)
        self.effects = effects


# -------------------------------
# 
#     S K I L L - T R E E 
# 
# -------------------------------
class TreeSoul(Skill):
    def __init__(self, name, maturity, description=""):
        super().__init__(name, "soul", description)
        self.name = name
        self.maturity = maturity
        self.description = description


class SkillTreeNode:
    def __init__(self, skill, head=None):
        self.skill = skill
        self.children = []
        if head:
            head.children.append(self)

    def is_empty_node(self):
        return self.skill == "[]"

    def __str__(self):
        if self.is_empty_node():
            return "[      ]"
        else:
            return_string = '{}  [{}]: {}'.format(
                self.skill.type.upper(), self.skill.name, self.skill.description)
            return return_string


# Different types of modifiers
CombatStatsModifier = namedtuple('StatsModifer', 'target modifier value num_turn')
PassiveStatModifer = namedtuple("PassiveStatModifer", 'modifer value')


