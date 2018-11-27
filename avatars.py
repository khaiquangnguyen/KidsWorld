from helpers import print_text_fancily
from shapes import SOLDIER


class Avatar:
    def __init__(self, shape):
        self.shape = shape

    def show_avatar(self):
        shape_by_line = self.shape.split('\n')
        for a_line in shape_by_line:
            print_text_fancily(a_line, 0.005, False)
        return self.shape

    def __str__(self):
        return self.shape


class SoldierAvatar(Avatar):
    def __init__(self):
        super().__init__(SOLDIER)
