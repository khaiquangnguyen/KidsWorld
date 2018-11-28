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

