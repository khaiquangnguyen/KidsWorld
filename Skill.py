from collections import namedtuple

class Skill:
    def __init__(self, name, desc):
        self.name = name
        self.desc = desc

class Fruit(Skill):
    def __init__(self, name, b_chrg, acc, dmg, sp_effs, desc):
        self.name = name
        self.b_chrg = b_chrg
        self.chrg = self.b_chrg
        self.acc = acc
        self.dmg = dmg
        self.sp_effs = sp_effs
        self.desc = desc

class AdvFruit(Fruit):
    def __init__(self, name, b_chrg, chrg, acc, dmg, sp_effs, desc):
        super().__init__(name,b_chrg, acc,dmg,sp_effs,desc)

class CbtFruit(Fruit):
    def __init__(self, name, b_chrg, acc, dmg, sp_effs, desc):
        super().__init__(name,b_chrg,chrg, acc,dmg,sp_effs,desc)

       
class Flower(Skill):
    def __init__(self, name, stat_effs, sp_effs, desc):
        self.name = name
        self.stat_effs = stat_effs
        self.sp_effs = sp_effs
        self.desc = desc    

class AdvFlower(Flower):
    def __init__(self, name, stat_effs, sp_effs, desc):
        super().__init__(name,stat_effs,sp_effs,desc)

class CbtFlower(Flower):
    def __init__(self, name, stat_effs, sp_effs, desc):
        super().__init__(stat_effs,sp_effs,desc)

class Leaf:
    def __init__(self, name, stat_effs):
        self.name = name
        self.stat_effs = stat_effs

class TreeSoul(Skill):
    def __init__(self, name, description=""):
        super().__init__(name, description)
        self.name = name
        self.description = description
        self.maturity = 0
        self.b_hp = 0
        self.b_dmg = 0
        self.b_defs = 0
        self.b_spd = 0
        self.b_eva = 0
        self.b_acc = 0
        self.b_crt_chc = 0
        self.b_crt_mult = 0
        self.hp_incr = 0
        self.dmg_incr = 0
        self.defs_incr = 0
        self.spd_incr = 0
        self.eva_incr = 0
        self.acc_incr = 0
        self.crt_chc_incr = 0
        self.crt_mult_incr = 0

