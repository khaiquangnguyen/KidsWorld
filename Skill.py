from collections import namedtuple


class Skill:
    def __init__(self, name, type, desc):
        self.name = name
        self.desc = desc


class AdvFruit:
    def __init__(self, name, b_chrg, chrg, acc, dmg, stat_effs, sp_effs, desc):
        self.name = name
        self.b_chrg = b_chrg
        self.chrg = chrg
        self.acc = acc
        self.dmg = dmg
        self.stat_effs = stat_effs
        self.sp_effs = sp_effs
        self.desc = desc


class CbtFruit:
    def __init__(self, name, b_chrg, chrg, acc, dmg, stat_effs, sp_effs, desc):
        self.name = name
        self.b_chrg = b_chrg
        self.chrg = chrg
        self.acc = acc
        self.dmg = dmg
        self.stat_effs = stat_effs
        self.sp_effs = sp_effs
        self.desc = desc


class AdvFlower:
    def __init__(self, name, stat_effs, sp_effs, desc):
        self.name = name
        self.stat_effs = stat_effs
        self.sp_effs = sp_effs
        self.desc = desc


class CbtFlower:
    def __init__(self, name, stat_effs, sp_effs, desc):
        self.name = name
        self.stat_effs = stat_effs
        self.sp_effs = sp_effs
        self.desc = desc


class Leaf:
    def __init__(self, name, stat_effs, desc):
        self.name = name
        self.stat_effs = stat_effs
        self.desc = desc


class ActiveSkill(Skill):
    def __init__(self, skill_name, base_charge, base_accuracy, dmg, status_effects, description):
        super().__init__(skill_name, "active", description)
        self.base_charge = base_charge
        self.base_accuracy = base_accuracy
        self.dmg = dmg
        self.status_effects = status_effects


class ActiveDamageSkill(ActiveSkill):
    def __init__(self, skill_name, base_charge, base_accuracy, dmg, status_effects, description):
        super().__init__(skill_name, base_charge, base_accuracy, dmg, status_effects, description)


class ActiveStatusSkill(ActiveSkill):
    def __init__(self, skill_name, base_charge, base_accuracy, dmg, status_effects, description):
        super().__init__(skill_name, base_charge, base_accuracy, 0, status_effects, description)


class ActiveSpecialSkill(ActiveSkill):
    def __init__(self, skill_name, base_charge, base_accuracy, dmg, status_effects, description):
        super().__init__(skill_name, base_charge, base_accuracy, 0, status_effects, description)


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


# Different types of modifiers
CombatStatsModifier = namedtuple('StatsModifer', 'target modifier value num_turn')
PassiveStatModifer = namedtuple("PassiveStatModifer", 'modifer value')
