class Stats:
    def __init__(self, dmg, defense, hp, hp_regen, charge_restore_rate, charge_increment_rate = 0, evasion = 0, accuracy = 1, crit_chance = 0.1, crit_mult = 1.5):
        # Primary stats
        # Damage, unit is scalar
        self.dmg = dmg
        # Defense, unit is scalar
        self.defense = defense
        # Hit point, unit is scalar
        self.hp = hp
        # Hit point regen, unit is percentage/s.
        self.hp_regen = hp_regen
        # How much charge should be restored, unit is percentage/hr.
        self.charge_restore_rate = charge_restore_rate


        # Secondary stats
        self.charge_increment_rate = charge_increment_rate
        self.evasion = evasion
        self.accuracy = accuracy
        self.crit_chance = crit_chance
        self.crit_mult = crit_mult
   
    def get_all_stats(self):
        return {
            "dmg": self.dmg,
            "defense":self.defense,
            "hp": self.hp,
            "hp_regen": self.hp_regen,
            "charge_increment_rate": self.charge_increment_rate,
            "charge_restore_rate": self.charge_restore_rate,
            "evasion": self.evasion,
            "accuracy": self.accuracy,
            "crit_chance": self.crit_chance,
            "crit_mult": self.crit_mult
        }
    
    def get_primary_stats(self):
        return {
            "dmg": self.dmg,
            "defense":self.defense,
            "hp": self.hp,
            "hp_regen": self.hp_regen,
            "charge_restore_rate": self.charge_restore_rate,
        }
    
    def get_secondary_stats(self):
                return {
            "charge_increment_rate": self.charge_increment_rate,
            "evasion": self.evasion,
            "accuracy": self.accuracy,
            "crit_chance": self.crit_chance,
            "crit_mult": self.crit_mult
        }
    
    def get_stats_by_names(self,name):
        return getattr(self,name)

    def list_stats(self):
        print (['dmg','defense','hp','hp_regen','charge_increment_rate',' charge_restore_rate', 'evasion','accuracy','crit_chance','crit_mult'])
    
    def __str__(self):
        print ("Showing Stat...")
        print(" - Damage = {}".format(self.dmg))
        print(" - Defense = {}".format(self.defense))
        print(" - HP = {}".format(self.defense))
        print(" - HP Regeneration Rate = {}".format(self.hp_regen))
        print(" - Maximum Charge Increment = {}".format(self.charge_increment_rate))
        print(" - Skill Charge Regenertion Rate = {}".format(self.charge_restore_rate))
        print(" - Evasion = {}".format(self.evasion))
        print(" - Accuracy = {}".format(self.accuracy))
        print(" - Critical Hit Chance = {}".format(self.crit_chance))
        print(" - Critical Hit Damage Multiplier = {}".format(self.crit_mult))
    
    def update_stats(self,stat_type, value):
        setattr(value,stat_type,value)
