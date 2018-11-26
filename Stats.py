from helpers import *


class Stats:
    def __init__(self, dmg, defense, hp, hp_regen, charge_restore_rate, charge_increment_rate=0, evasion=0, accuracy=1, crit_chance=0.1, crit_mult=1.5):

        # base stats, which is the inherent stats of character.

        # Primary stats
        self.primary_stats = ['dmg', 'defense',
                              'hp', 'hp_regen', ' charge_restore_rate']
        self.base_dmg = dmg
        # Defense, unit is scalar
        self.base_defense = defense
        # Hit point, unit is scalar
        self.base_hp = hp
        # Hit point regen, unit is percentage/s. . i.e 0.1 = 10%/s
        self.base_hp_regen = hp_regen
        # How much charge should be restored, unit is percentage/hr. i.e 0.1 = 10%/hr
        self.base_charge_restore_rate = charge_restore_rate

        # Secondary stats
        self.secondary_stats = ['charge_increment_rate',
                                'evasion', 'accuracy', 'crit_chance', 'crit_mult']
        # Increase the maximum number of charge rate per skill, unit is percentage. Default is 1
        # i.e 0.1 = 10%
        self.base_charge_increment_rate = charge_increment_rate
        # Evasion. Unit is percentage. Default is 0. 0.1 = 10%
        self.base_evasion = evasion
        # Base accuracy. Unit is percentage. Default is 1. 1 = 100%
        self.base_accuracy = accuracy
        # Critical hit chance. Unit is percentage. Default is 0.1, which is 10%
        self.base_crit_chance = crit_chance
        # Critical hit damage multipler. Unit is percentage. Default is 1.5, which is damage * 1.5
        self.base_crit_mult = crit_mult

        # Actual stats, which is the stats after modification from items and everything
        self.dmg = dmg
        self.defense = defense
        self.hp = hp
        self.hp_regen = hp_regen
        self.charge_restore_rate = charge_restore_rate
        self.charge_increment_rate = charge_increment_rate
        self.evasion = evasion
        self.accuracy = accuracy
        self.crit_chance = crit_chance
        self.crit_mult = crit_mult

    def update_passive_skill_modifiers(self, skill_tree):
        # tranverse the tree and get all passives
        pass

    def update_active_skill_modifier(self, effects):
        # get effects and update
        pass

    def get_all_stats(self):
        stats = {}
        for i in (self.primary_stats + self.secondary_stats):
            stats.update(i, getattr(self, i))
        return stats

    def get_primary_stats(self):
        stats = {}
        for i in self.primary_stats:
            stats.update(i, getattr(self, i))
        return stats

    def get_secondary_stats(self):
        stats = {}
        for i in self.secondary_stats:
            stats.update(i, getattr(self, i))
        return stats

    def get_stats_by_names(self, name):
        return getattr(self, name)

    def list_stats(self):
        print(self.primary_stats + self.secondary_stats)

    def list_primary_stats(self):
        print(self.primary_stats)

    def list_secondary_stats(self):
        print(self.secondary_stats)

    def print_primary_stats(self):
        print_text_fancily("Showing Primary Stats ...")
        for i in self.primary_stats:
            s = (' - %s = %d' % (i, getattr(self, i)))
            print_text_fancily(s)

    def print_secondary_stats(self):
        print_text_fancily("Showing Secondary Stat ...")
        for i in self.secondary_stats:
            s = (' - %s = %d' % (i, getattr(self, i)))
            print_text_fancily(s)

    def print_all_stats(self):
        print_text_fancily("Showing Stats ...")
        for i in (self.primary_stats + self.secondary_stats):
            s = (' - %s = %d' % (i, getattr(self, i)))
            print_text_fancily(s)

    def update_stats(self, stat_type, value):
        setattr(value, stat_type, value)
