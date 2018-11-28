class Backpack:
    def __init__(self, owner, max_length = 64):
        self.owner = owner
        self.items = []
        self.max_length = max_length
    
    def is_full(self):
        return True if len(self.items) >= self.max_length else False

    def add_item(self, item):
        if not self.is_full():
            self.items.append(item)

    def get_item_by_name(self, item_name):
        try:
            item_index = self.items.index(item_name)
            item = self.get_item_by_slot(item_index)
            return item
        except:
            return -1
    
    def get_item_by_slot(self,slot):
        item = self.items[slot]
        self.items = self.items[:slot] + self.items[slot+1]
        return item

