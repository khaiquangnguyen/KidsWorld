from skills import PassiveStatModifer


class Item:
    def __init__(self, name, equipment_slot, description, cost, effects, life_time = 20):
        self.name = name
        self.equipment_slot = equipment_slot
        self.description = description
        self.cost = cost
        self.effects = effects
        self.life_time = life_time


# ------------ ITEM LIST ------------- #

Pencil = Item("pencil", "hands", "the basic tool of students",
              "1", [PassiveStatModifer("+dmg", 1)])

Notebook = Item("notebook", "hands", "The basic tool of students",
                "1", [PassiveStatModifer("+defense", 1)])

Eraser = Item("eraser", "hands", "The basic tool of students", "1",
              [PassiveStatModifer("+dmg", 1.5)])

Laptop = Item("laptop", "accesories", "The advanced productivity tool of students", "1",
              [PassiveStatModifer("*dmg", 1.3),
               PassiveStatModifer("+crit_mult", 0.5),
               PassiveStatModifer("+crit_chance", 0.2)])

Calculator = Item("calculator", "accesories", "The best friend of math students", "1",
                  [PassiveStatModifer("*dmg", 1.1)])

RunningShoes = Item("running shoes", "foot", "Everyone needs a pair of running shoes", "1",
                    [PassiveStatModifer("+hp", 2)])
