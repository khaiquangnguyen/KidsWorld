from Skill import TreeSoul, Leaf, CbtFlower, CbtFruit
from SkillTree import SkillTree, SkillTreeNode

# Create the main Math Tree
MathSoul = TreeSoul("The Essence Of Mathematics", "Mathematics can turn you into a superman")
MathSoul.b_hp = 91
MathSoul.b_dmg = 134
MathSoul.b_defs = 95
MathSoul.b_spd = 80
MathSoul.b_eva = 0.25
MathSoul.b_acc = 1
MathSoul.b_crt_chc = 0.1
MathSoul.b_crt_mult = 1.5
MathSoul.hp_incr = 1
MathSoul.dmg_incr = 4
MathSoul.defs_incr = 2
MathSoul.spd_incr = 2
MathSoul.eva_incr = 0 
MathSoul.acc_incr = 0
MathSoul.crt_chc_incr = 0
MathSoul.crt_mult_incr = 0

MentalMath = CbtFlower("Mental Math", None,"MentalMath","Your ability to quickly calculate provides you an edge in battle!")
Imagination = CbtFlower("Imagination",("crt_chc",0.1),"Imagination","Imagination helps you doing unimaginable things in math!")
Limit = CbtFruit("Limit",20,1,40,"Limit","Overwhelm the opponent with a difficult limit problem, dealing psy damage.")
Focus = CbtFruit("Focus",20,-1,-1,"Focus","Focus helps you do your math better!")
Leaf_1 = Leaf("Dmg Booster",("dmg",4,2),"Boost Damage")
Leaf_2 = Leaf("Spd Booster",("spd",2,2),"Boost Speed")
Leaf_3 = Leaf("Defs Booster",("defs",1,0.5),"Boost Defense")
Leaf_4 = Leaf("Critical Chance Booster",("crt_chc",0,0.01),"Boost Critical Damage Chance")
Leaf_5 = Leaf("Critical Multiplier Booster",("crt_mult",0.5,0.1),"Boost Critical Multiplier")


Geometry = TreeSoul("Geometry","Geometry is one the oldest form of mathematics.")
Geometry.b_hp = 4
Geometry.hp_incr = 2
Geometry.b_defs = 4
Geometry.defs_incr = 1
Triangulate = CbtFlower("Triangulate",None,"Triangulate","triangulation helps you heal yourself.")


NumberTheory = TreeSoul("Number Theory","Number Theory is the queen of mathematics.")
NumberTheory.b_dmg = 4
NumberTheory.dmg_incr = 2
NumberTheory.b_crt_mult = 0.5
NumberTheory.crt_mult_incr = 0.2
Logic = CbtFruit("Logic",10,0.9,70,None,"Throw a logic problem at your enemy, causing confusion and psy damage.")


root = SkillTreeNode(MathSoul)
geometry_branch = SkillTreeNode(Geometry,root)
flower_geo = SkillTreeNode(Triangulate,geometry_branch)
number_branch = SkillTreeNode(NumberTheory,root)
fruit_numb = SkillTreeNode(Logic,number_branch)
leaf_1 = SkillTreeNode(Leaf_1,root)
leaf_2 = SkillTreeNode(Leaf_2,root)
leaf_3 = SkillTreeNode(Leaf_3,root)
leaf_4 = SkillTreeNode(Leaf_4,root)
leaf_5 = SkillTreeNode(Leaf_5,root)
flower_1 = SkillTreeNode(MentalMath,root)
flower_2 = SkillTreeNode(Imagination,root)
fruit_1 = SkillTreeNode(Limit,root)
fruit_2 = SkillTreeNode(Focus,root)

MathTree = SkillTree(root)
MathTree.show()