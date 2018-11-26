from helpers import print_title_fancily


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
    def __init__(self, skill_name, base_charge, base_accuracy, effects, description):
        super().__init__(skill_name, "active", effects, description)
        self.base_charge = base_charge
        self.base_accuracy = base_accuracy


class PassiveSkill(Skill):
    def __init__(self, skill_name, effects, description):
        super().__init__(skill_name, "passive", effects, description)


class TreeSoul():
    def __init__(self, name, maturity):
        self.name = name
        self.maturity = maturity

# -------  A LIST OF SKILLS -------------#


MathSoul = TreeSoul("The Essence Of Mathematics", 1)
Geometry = TreeSoul("The Beauty of Geometry", 1)
Integral = ActiveSkill("Integral", 5, 90, {"deal_dmg": (3, 0)},
                       "Overwhelm the opponent with a difficult integral, dealing fatal damage.")
Addition = ActiveSkill("Addition", 20, 90, {"deal_dmg": (1, 0)},
                       "Force opponent to do mental addition, dealing minor damage.")


def create_math_skill_tree():
    soul = SkillTreeNode("Math Soul", "soul", "Math")
    hp_branch = SkillTreeNode("Geometry", "Soul", "Boost", soul)
    hp_max_leaf = SkillTreeNode("Max HP++", "Passive", 0, hp_branch)
    hp_regen_leaf = SkillTreeNode("HP regen++", "Passive", 0, hp_branch)
    second_leaf = SkillTreeNode("Dmg ++", "Passive", 4, soul)
    third_leaf = SkillTreeNode("Crit Chance++", "Passive", "10%", soul)
    fourth_leaf = SkillTreeNode("Crit Dmg++", "Passive", "50%", soul)
    active_one = SkillTreeNode("Tackle", "Active",
                               "Dmg: 10 | Charges: 20 | Accuracy: 100", soul)
    active_two = SkillTreeNode("Integral", "Active",
                               "Dmg: 30 | Charges: 5 | Accuracy: 90", soul)
    empty_slot = Node("[   ]", soul)
    empty_slot = Node("[   ]", hp_branch)
    return soul


create_math_skill_tree()
