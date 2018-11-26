from helpers import *
class Player:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return (self.draw_player_shape())

    def draw_player_shape(self):
        player_shape = (r"""
 _   _   _   _+       |
/_`-'_`-'_`-'_|  \+/  |
\_`M'_`D'_`C'_| _<=>_ |
  `-' `-' `-' 0/ \ / o=o
              \/\ ^ /`0
              | /_^_\
              | || ||
            __|_d|_|b__

                """)
        shape_by_line = player_shape.split('\n')
        for a_line in shape_by_line:
            print_text_fancily(a_line,0.005)
            delete_last_lines()
        return player_shape
        

