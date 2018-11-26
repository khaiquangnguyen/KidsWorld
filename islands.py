from enum import Enum
islands = ["MathParadise", "HistoryField"]

# class BuildingType(Enum):

class Stats:
    def __init__(self, dmg, defense, hp, hp_regen, max_charge, charge_restore_rate, evasion, accuracy, crit_chance, crit_mult):
        self.dmg = dmg
        self.defense = defense
        self.hp = hp
        self.hp_regen = hp_regen
        self.max_charge = max_charge
        self.charge_restore_rate = charge_restore_rate
        self.evasion = evasion
        self.accuracy = accuracy
        self.crit_chance = crit_chance
        self.crit_mult = crit_mult

            
    def get_stats(self):
        return (self.dmg, self.defense, self.hp, self.hp_regen, self.max_charge, self.charge_restore_rate, self.evasion, self.accuracy, self.crit_chance, self.crit_mult)
    
    def list_stats(self):
        print (['dmg','defense','hp','hp_regen','max_charge',' charge_restore_rate', 'evasion','accuracy','crit_chance','crit_mult'])
    
    def __str__(self):
        print ("Showing Stat...")
        print(" - Damage = {}".format(self.dmg))
        print(" - Defense = {}".format(self.defense))
        print(" - HP = {}".format(self.defense))
        print(" - HP Regeneration Rate = {}".format(self.hp_regen))
        print(" - Maximum Skill Charge = {}".format(self.max_charge))
        print(" - Skill Charge Regenertion Rate = {}".format(self.charge_restore_rate))
        print(" - Evasion = {}".format(self.evasion))
        print(" - Accuracy = {}".format(self.accuracy))
        print(" - Critical Hit Chance = {}".format(self.crit_chance))
        print(" - Critical Hit Damage Multiplier = {}".format(self.crit_mult))
    
    def update_stats(self):
        pass




class Island:
    def __init__(self,name):
        self.name = name
        self.buildings = []

class Building:
    def __init__(self,type):
        self.type = type

class Marketplace (Building):
    def __init__(self, parent_island = None):
        super().__init__("marketplace")
        self.parent_island = parent_island
        self.vendors = []

class Vendor:
    def __init__(self,name, items = []):
        self.name = name
        self.items = items

class Item:
    def __init__(self,name,type,attributes = None):
        self.name = name
        self.type = type
        self.attributes = attributes