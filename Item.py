
class Item:
    def __init__(self, name, cost, desc = None, stat_effs = None, sp_effs = None):
        self.name = name
        self.desc = desc
        self.cost = cost
        self.stat_effs = stat_effs
        self.sp_effs = sp_effs

class EquipItem(Item):
    def __init__(self, name, cost, desc, stat_effs, sp_effs, equipment_slot, life_time = 20):
        super().__init__(name, cost, desc, stat_effs, sp_effs)
        self.equipment_slot = equipment_slot
        self.life_time = life_time
    
    def show_item(self):
        print("Name:{}".format(self.name))
        print("Description:{}".format(self.description))
        print("Equipment Slot:{}".format(self.equipment_slot))
        print("Cost:{}".format(self.cost))
        print("life time:{}".format(self.life_time))
        print("Effects:{}".format(self.effects))

def ConsummableItem(Item):
    def __init__(self, name, description, cost, stat_effs, sp_effs):
        super().__init__(name, cost, description, stat_effs, sp_effs)
    
        

# # ------------ ITEM LIST ------------- #
#
# Pencil = Item("pencil", "hands", "the basic tool of students",
#               "1", [PassiveStatModifer("+dmg", 1)])
#
# Notebook = Item("notebook", "hands", "The basic tool of students",
#                 "1", [PassiveStatModifer("+defense", 1)])
#
# Eraser = Item("eraser", "hands", "The basic tool of students", "1",
#               [PassiveStatModifer("+dmg", 1.5)])
#
# Laptop = Item("laptop", "accesories", "The advanced productivity tool of students", "1",
#               [PassiveStatModifer("*dmg", 1.3),
#                PassiveStatModifer("+crit_mult", 0.5),
#                PassiveStatModifer("+crit_chance", 0.2)])
#
# Calculator = Item("calculator", "accesories", "The best friend of math students", "1",
#                   [PassiveStatModifer("*dmg", 1.1)])
#
# RunningShoes = Item("running shoes", "foot", "Everyone needs a pair of running shoes", "1",
#                     [PassiveStatModifer("+hp", 2)])
