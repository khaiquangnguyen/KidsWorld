from helpers import print_text_fancily


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
        shape = (r"""
 _   _   _   _+       |
/_`-'_`-'_`-'_|  \+/  |
\_`M'_`D'_`C'_| _<=>_ |
  `-' `-' `-' 0/ \ / o=o
              \/\ ^ /`0
              | /_^_\
              | || ||
            __|_d|_|b__

                """)
        super().__init__(shape)
