class Equipments:
    def __init__(self, owner):
        """ Modelled after heroes 3
        """
        self.owner = owner
        self.left_hand = None
        self.right_hand = None
        self.feet = None
        self.head = None
        self.cape = None
        self.belt = None
        self.misc_1 = None
        self.misc_2 = None
        self.misc_3 = None
        self.misc_4 = None
        self.misc_5 = None

    def equip(self, slot, item):
        if getattr(self, slot) is None:
            setattr(self, slot, item)
            return 1
        else:
            ret_val = self.unequip(slot)
            if ret_val == -1:
                return -1
            else:
                setattr(slot, item)
                return 1

    def unequip(self, slot):
        # if backpack is full or slot is empty
        if self.owner.backpack.is_full():
            return -1
        item = getattr(self, slot)
        setattr(self, slot, None)
        # add the item to the backpack
        self.owner.backpack.add_item(item)
        return item

    def swap(self, slot, backpack_slot):
        # take the item out of the backpack first
        backpack_item = self.owner.backpack.get_item_by_slot(backpack_slot)
        # Then unequip the current item
        item = self.unequip(slot)
        # check if we can equip the new item
        if self.equip(slot, backpack_item) == 1:
            #  add the item to backpack
            self.owner.backpack.add_item(item)
            return 1
        else:
            # something goes wrong. Return the item to backpack
            self.owner.backpack.add_item(backpack_item)
            self.equip(item)
            return -1


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
        return item

    def take_item_by_name(self,item_name):
        try:
            item_index = self.items.index(item_name)
            item = self.take_item_by_slot(item_index)
            return item
        except:
            return -1

    def take_item_by_slot(self, slot):    
        item = self.items[slot]
        self.items = self.items[:slot] + self.items[slot+1]
        return item

    def get_all_items(self):
        return self.items   
    
    def get_items_of_equipment_slot(self,equipment_slot):
        # 
        items = []
        for item in self.items:
            if item.equipment_slot == equipment_slot:
                items.append(item)
        return items

