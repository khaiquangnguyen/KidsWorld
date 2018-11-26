from enum import Enum
islands = ["MathParadise", "HistoryField"]


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