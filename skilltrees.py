from helpers import print_title_fancily
from pptree import *


class SkillTreeNode:
    def __init__(self, skill, head=None):
        self.skill = skill
        self.type = type
        self.children = []
        if head:
            head.children.append(self)

    def __str__(self):
        return_string = '{}  [{}]: {}'.format(
            self.skill.type.upper(), self.skill.name, self.skill.description)
        return return_string


class SkillTree:
    def __init__(self, head):
        self.head = head

    def get_all_skills(self):
        if self.head.children == []:
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
            if self.head.skill.type == "passive":
                skills.extend([root.skill])
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
