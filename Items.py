class Item:
    def __init__(self, name, equipment_slot, description, cost, effects):
        self.name = name
        self.equipment_slot = equipment_slot
        self.description = description
        self.cost = cost
        self.effects = effects


# ------------ ITEM LIST ------------- #

Pencil = Item("pencil", "hands", "the basic tool of students", "1", {
              "+dmg": (1, -1)},)

Notebook = Item("notebook", "hands", "The basic tool of students", "1", {
    "+defense": (1, -1)},)

Eraser = Item("eraser", "hands", "The basic tool of students", "1", {
    "+dmg": (1.5, -1)},)

Laptop = Item("laptop", "accesories", "The advanced productivity tool of students", "1", {
    "*dmg": (1.3, -1),
    "+crit_mult": (0.5, -1),
    "+crit_chance": (0.2, -1)})

Calculator = Item("calculator", "accesories", "The best friend of math students", "1", {
    "*dmg": (1.1, -1)})

RunningShoes = Item("running shoes", "foot", "Everyone needs a pair of running shoes", "1", {
    "+hp": (2, -1)})
