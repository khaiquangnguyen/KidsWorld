from helpers import print_title_fancily
from pptree import print_tree
from collections import namedtuple


class Skill:
    def __init__(self, name, type, description):
        self.name = name
        self.type = type
        # A dictionary of all potential effects of this skill.
        # format is {"modifier_name":(modifer,number_of_turns)}. i.e {"hp":+10,3}
        # For passive skills, the number of turns is -1, implying infinity
        self.description = description

    def get_effects(self):
        return self.effects

    def get_description(self):
        return self.description


class ActiveSkill(Skill):
    def __init__(self, skill_name, base_charge, base_accuracy, dmg, status_effects, description):
        super().__init__(skill_name, "active", description)
        self.base_charge = base_charge
        self.base_accuracy = base_accuracy
        self.dmg = dmg
        self.status_effects = status_effects


class PassiveSkill(Skill):
    def __init__(self, skill_name, effects, description):
        super().__init__(skill_name, "passive", description)
        self.effects = effects


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


class SkillTree:
    def __init__(self, head):
        self.head = head

    def get_all_skills(self):
        if not self.head.is_empty_node() and self.head.children == []:
            return []
        else:
            skills = [self.head.skill]
            for child in self.head.children:
                skills.extend(child.get_all_skills())
            return skills

    def get_all_passive_skills(self):
        if self.head.children == []:
            return []
        else:
            skills = []
            if not self.head.is_empty_node() and self.head.skill.type == "passive":
                skills.extend([self.head.skill])
            for child in self.head.children:
                skills.extend(child.get_all_skills())
            return skills

    def get_all_active_skills(self):
        if self.head.children == []:
            return []
        else:
            skills = []
            if self.head.skill.type == "active":
                skills.extend([self.head.skill])
            for child in self.head.children:
                skills.extend(child.get_all_skills())
            return skills

    def show(self):
        print_title_fancily(None, "Skill Tree")
        print_tree(self.head)
        print()


StatsModifier = namedtuple('StatsModifer', 'target modifier value num_turn')
PassiveStatModifer = namedtuple("PassiveStatModifer", 'modifer value')

# -------  A LIST OF SKILLS -------------#

MathSoul = TreeSoul("The Essence Of Mathematics", 1)
Geometry = TreeSoul("The Beauty of Geometry", 1)
Integral = ActiveSkill("Integral", 5, 90, 3, [],
                       "Overwhelm the opponent with a difficult integral, dealing fatal damage.")
Addition = ActiveSkill("Addition", 20, 90, 1, [StatsModifier("self", '+defense', 1, 5)],
                       "Force opponent to do mental addition, dealing minor damage.")
Think = ActiveSkill("Think", 5, 100, 0, [()],
                    "It's always useful to use your brain!")

QuickCalculation = PassiveSkill("Quick Calculation", [PassiveStatModifer("+dmg", 1)],
                                "Your ability to quickly calculate provides you an edge in battle!")

Imagination = PassiveSkill("Imagination", [PassiveStatModifer("+crit_chance", 0.1)],
                           "Imagination helps you doing unimaginable things!")
DrawingSkill = PassiveSkill("DrawingSkill", [PassiveStatModifer("+crit_mult", 0.2)],
                            "Good drawing skill allows to hit the right spot of a geometry problem easier!")

Meditation = PassiveSkill("Meditation", [PassiveStatModifer("+hp_regen", 0.1)],
                          "Meditation allows you to heal faster outside of battle!")


HistorySoul = TreeSoul("The Worth of History", 1)
Battles = TreeSoul("Knowledge of Battles", 1)
Short_Term_Memory = PassiveSkill("Short_Term_Memory", [PassiveStatModifer("+defense", 1)],
                                 " Short term memory of opponent's actions allows you to divise effective defense measures")
Long_Term_Memory = PassiveSkill("Long_Term_Memory", [PassiveStatModifer("+evasion", 0.1)],
                                " Memory of past battles allows you to predict the future.")

# ------ CREATE THE SKILL TREES --------- #

math_root = SkillTreeNode(MathSoul)
geometry_branch = SkillTreeNode(Geometry, math_root)
integral_leaf = SkillTreeNode(Integral, math_root)
addition_leaf = SkillTreeNode(Addition, math_root)
quick_calculation_leaf = SkillTreeNode(QuickCalculation, math_root)
imagination_leaf = SkillTreeNode(Imagination, geometry_branch)
drawing_leaf = SkillTreeNode(DrawingSkill, geometry_branch)
meditation_leaf = SkillTreeNode(Meditation, math_root)
empty_1_leaf = SkillTreeNode("[]", math_root)
empty_2_leaf = SkillTreeNode("[]", geometry_branch)
Math_Tree = SkillTree(math_root)
