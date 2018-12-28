
class Item:
    def __init__(self, name, cost, desc=None, stat_effs=None, sp_effs=None):
        self.name = name
        self.desc = desc
        self.cost = cost
        self.stat_effs = stat_effs
        self.sp_effs = sp_effs


class EquipItem(Item):
    def __init__(self, name, cost, desc, stat_effs, sp_effs, equipment_slot, life_time=20):
        super().__init__(name, cost, desc, stat_effs, sp_effs)
        self.equipment_slot = equipment_slot
        self.life_time = life_time

    def show_item(self):
        print(" - {} - ".format(self.name))
        print("   Description:{}".format(self.desc))
        print("   Equipment Slot:{}".format(self.equipment_slot))
        print("   Cost:{}".format(self.cost))
        print("   Life time:{}".format(self.life_time))
        print("   Stat Effects:{}".format(self.stat_effs))
        print("   Special Effects:{}".format(self.sp_effs))


class ConsummableItem(Item):
    def __init__(self, name, description, cost, stat_effs, sp_effs):
        super().__init__(name, cost, description, stat_effs, sp_effs)

    def show_item(self):
        print(" - {} - ".format(self.name))
        print("   Description:{}".format(self.desc))
        print("   Cost:{}".format(self.cost))
        print("   Stat Effects:{}".format(self.stat_effs))
        print("   Special Effects:{}".format(self.sp_effs))


# ------------ ITEM LIST ------------- #

Pencil = EquipItem("pencil", "hands", "the basic tool of students",
                   "1", [("dmg", 1)])

Notebook = EquipItem("notebook", "hands", "The basic tool of students",
                     "1", [("defs", 1)])

Eraser = EquipItem("eraser", "hands", "The basic tool of students",
                   "1", [("dmg", 1.5)])

Laptop = EquipItem("laptop", "accesories", "The advanced productivity tool of students", "1",
                   [("dmg", "130%"),
                    ("crit_mult", 0.5),
                       ("crt_chc", 0.2)])

Calculator = EquipItem("calculator", "accesories",
                       "The best friend of math students", "1", [("dmg", "110%")])

RunningShoes = EquipItem("running shoes", "foot", "Everyone needs a pair of running shoes", "1",
                         [("hp", 2)])
