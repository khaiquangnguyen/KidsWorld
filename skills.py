from Skill import Skill,TreeSoul, PassiveSkill, ActiveSkill, CombatStatsModifier, PassiveStatModifer
from SkillTree import SkillTree, SkillTreeNode
# -------  A LIST OF SKILLS -------------#

MathSoul = TreeSoul("The Essence Of Mathematics", 1)
Geometry = TreeSoul("The Beauty of Geometry", 1)
Integral = ActiveSkill("Integral", 5, 90, 3, [],
                       "Overwhelm the opponent with a difficult integral, dealing fatal damage.")
Addition = ActiveSkill("Addition", 20, 90, 1, [CombatStatsModifier("self", '+defense', 1, 5)],
                       "Force opponent to do mental addition, dealing minor damage.")
Think = ActiveSkill("Think", 5, 100, 0, [()],
                    "It's always useful to use your brain!")

QuickCalculation = PassiveSkill("Quick Calculation", [PassiveStatModifer("+dmg", 1)],
                                "Your ability to quickly calculate provides you an edge in battle!")

Imagination = PassiveSkill("Imagination", [PassiveStatModifer("+crit_chance", 0.1)],
                           "Imagination helps you doing unimaginable things!")
DrawingSkill = PassiveSkill("DrawingSkill", [PassiveStatModifer("+crit_mult", 0.2)],
                            "Good drawing skill allows to hit the right spot of a geometry problem easier!")

Meditation = PassiveSkill("Meditation", [PassiveStatModifer("+hp_regen", 0.1)],
                          "Meditation allows you to heal faster outside of battle!")


HistorySoul = TreeSoul("The Worth of History", 1)
Battles = TreeSoul("Knowledge of Battles", 1)
Short_Term_Memory = PassiveSkill("Short_Term_Memory", [PassiveStatModifer("+defense", 1)],
                                 " Short term memory of opponent's actions allows you to divise effective defense measures")
Long_Term_Memory = PassiveSkill("Long_Term_Memory", [PassiveStatModifer("+evasion", 0.1)],
                                " Memory of past battles allows you to predict the future.")

# ------ CREATE THE SKILL TREES --------- #

math_root = SkillTreeNode(MathSoul)
geometry_branch = SkillTreeNode(Geometry, math_root)
integral_leaf = SkillTreeNode(Integral, math_root)
addition_leaf = SkillTreeNode(Addition, math_root)
quick_calculation_leaf = SkillTreeNode(QuickCalculation, math_root)
imagination_leaf = SkillTreeNode(Imagination, geometry_branch)
drawing_leaf = SkillTreeNode(DrawingSkill, geometry_branch)
meditation_leaf = SkillTreeNode(Meditation, math_root)
empty_1_leaf = SkillTreeNode("[]", math_root)
empty_2_leaf = SkillTreeNode("[]", geometry_branch)
Math_Tree = SkillTree(math_root)
