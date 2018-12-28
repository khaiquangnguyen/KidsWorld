from helpers import print_title_fancily
from shapes import MATH_PARADISE_ISLAND
from Item import *
islands = ["MathParadise"]


class Island:
    def __init__(self, name, description, shape):
        self.buildings = []
        self.name = name
        self.description = description
        self.shape = shape

    def show_island_name(self):
        print_title_fancily(self.name, self.description)

    def show_buildings(self):
        for building in self.buildings:
            building


class Building:
    def __init__(self, type, parent_island):
        self.type = type
        self.parent_island = parent_island


class Marketplace(Building):
    def __init__(self, parent_island=None):
        super().__init__("marketplace", parent_island)
        self.vendors = []

    def get_all_vendors(self):
        return self.vendors


class Mapmaker(Building):
    def __init__(self, maps=[], parent_island=None):
        super().__init__("mapmaker", parent_island)
        self.maps = maps

    def add_map(self, map):
        self.maps.append(map)


class Map:
    def __init__(self, name, description, rewards):
        self.name = name
        self.description = description
        self.rewards = rewards
        # A list of hint. Basically a series of challenges that the player have to solve.
        self.hints = []


class Vendor:
    def __init__(self, name, items=[]):
        self.name = name
        self.items = items

    def add_item(self, item):
        self.items.append(item)


def create_math_island():
    MathParadise = Island(
        "MathParadise", "A paradise for math nerds", MATH_PARADISE_ISLAND)
    # add buildings to MathParadise
    mapmaker = Mapmaker(MathParadise)
    marketplace = Marketplace(MathParadise)
    bot_vendor = Vendor(
        "Poor Student", [Pencil, Notebook, Eraser, Laptop, Calculator, RunningShoes])
    MathParadise.buildings = [mapmaker, marketplace]
    return MathParadise


MathParadise = create_math_island()
