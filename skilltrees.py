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
