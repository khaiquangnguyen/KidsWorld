from helpers import print_text_fancily, print_title_fancily, calc_mod_value
import unittest
class Stats:
    """
    The stat class. Each player has a stat object to manage their stats.
    There are three types of stats:

     - Combat permanent stats: Permanent stats used in combat
        + hp (hit point)
        + dmg (damage)
        + defs (defense)
        + spd (speed)
        + eva (evasion)
        + acc (accuracy)
        + crt_chc (crit chance)
        + crt_mult (crit multiplier)

     - Adventure permanent stats: Permanent stats used during adventure.
        + hp_reg (hit point regen rate)
        + chrg_rstr (charge restore rate)
        + chrg_incr (charge increment rate)
        + luck
    """
    def __init__(self, character):
        # The owner of these stats
        self.character = character
        # Combat permanent stats
        self.combat_perm_stats = ['hp','dmg','defs','spd','eva','acc','crt_chc','crt_mult']
        self.b_hp = 91
        self.b_dmg = 134
        self.b_defs = 95
        self.b_spd = 80
        self.b_eva = 0.1
        self.b_acc = 1
        self.b_crt_chc = .1
        self.b_crt_mult = 1.5
        # adventure permanent stats
        self.adv_perm_stats = ['hp_reg','chrg_rstr','chrg_incr','luck']
        self.b_hp_reg = 1
        self.b_chrg_rstr = 0
        self.b_chrg_incr = 0
        self.b_luck = 0

        # current_stats, after modification
        self.hp = 0
        self.dmg = 0
        self.defs = 0
        self.spd = 0
        self.eva = 0
        self.acc = 1
        self.crt_chc = 0
        self.crt_mult = 0
        self.hp_reg = 0
        self.chrg_rstr = 0
        self.chrg_incr = 0
        self.luck = 0

        # the most important stat of all
        self.curr_hp = 0

    def get_all_stats(self):
        stats = {}
        for i in (self.combat_perm_stats + self.adv_perm_stats):
            stats.update(i, getattr(self, i))
        return stats

    def get_all_combat_stats(self):
        stats = {}
        for i in self.combat_perm_stats:
            stats.update(i, getattr(self, i))
        return stats

    def get_all_adventure_stats(self):
        stats = {}
        for i in self.adv_perm_stats:
            stats.update(i, getattr(self, i))
        return stats

    def get_stats_by_names(self, name):
        return getattr(self, name)

    def list_stats(self):
        print (self.combat_perm_stats + self.adv_perm_stats)


    def print_combat_stats(self):
        print_text_fancily("Showing Combat Stats ...")
        for i in self.combat_perm_stats:
            s = (' - %s = %d' % (i, getattr(self, i)))
            print_text_fancily(s, 0.02, False)

    def print_adventure_stats(self):
        print_text_fancily("Showing Secondary Stat ...")
        for i in self.adv_perm_stats:
            s = (' - %s = %d' % (i, getattr(self, i)))
            print_text_fancily(s, 0.02, False)

    def print_all_stats(self):
        print_title_fancily(None,"Character Stats")
        print()
        print_text_fancily(" Combat stats")
        for i in (self.combat_perm_stats):
            s = ("     - %-10s : %d" % (i.upper(), getattr(self, i)))
            print_text_fancily(s,0.01,False)
        print()
        print_text_fancily(" Adventure stats")
        for i in (self.adv_perm_stats):
            s = ('     - %-10s : %d' % (i.upper(), getattr(self, i)))
            print_text_fancily(s,0.01,False)


    def calculate_stats(self):
        # get all stats modifiers
        skill_stats_modifiers = self.character.skill_tree.get_stat_modifiers()
        item_stats_modifiers = self.character.equipments.get_stat_modifiers()
        self.hp = self.b_hp
        self.dmg = self.b_dmg
        self.defs = self.b_defs
        self.acc  = self.b_acc
        self.eva = self.b_eva
        self.crt_chc = self.b_crt_chc
        self.crt_mult = self.b_crt_mult
        self.hp_reg = self.b_hp_reg
        self.chrg_incr = self.b_chrg_incr
        self.chrg_rstr = self.b_chrg_rstr
        self.luck = self.b_luck
        for stat in (skill_stats_modifiers + item_stats_modifiers):
            base_stat = getattr(self,"b_"+stat[0])
            modify_value = calc_mod_value(base_stat, stat[1])
            curr_stat = getattr(self,stat[0])
            curr_stat = curr_stat + modify_value
            setattr(self,stat[0],curr_stat)


# class TestStats(unittest.TestCase):
#     def setUp(self):
#         self.stat = Stats()
#         self.stat.print_all_stats()







