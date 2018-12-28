# ------ IMPORT ----------

import unittest

from termcolor import cprint
from pyfiglet import figlet_format
import os
import sys
import time
from colorama import init
init(strip=not sys.stdout.isatty())  # strip colors if stdout is redirected

# ------- FUNCTIONS --------

CURSOR_UP_ONE = '\x1b[1A'
ERASE_LINE = '\x1b[2K'
TEXT_DELAY = 0.02


def delete_last_lines(n=1):
    #     for _ in range(n):
    #         # sys.stdout.write(CURSOR_UP_ONE)
    #         # sys.stdout.write(ERASE_LINE)
    print(" " * 1000, end="\r")


def clear_screen():
    # Works on macs and linux only
    # print('\033[H\033[J')
    os.system('cls')  # For Windows


def print_text_fancily(s, delay=TEXT_DELAY, end_with_newline=True):
    for i in range(len(s)):
        print(s[:i], end="\r")
        time.sleep(delay)
    if end_with_newline:
        print(s, "\n")
    else:
        print(s)


def print_title_fancily(title=None, subtitle=None):
    print("-" * 30)
    new_s1 = ""
    new_s2 = ""
    if title is not None:
        title = title.lower()
        for i in title:
            new_s1 += i + " "
    if subtitle is not None:
        subtitle = subtitle.upper()
        for i in subtitle:
            new_s2 += i + " "

    if title and not subtitle:
        cprint(figlet_format(new_s1, font='doom'))
        print("-" * 30)
    elif not title and subtitle:
        print(f'  {new_s2}   ')
        print("-" * 30)

    else:
        cprint(figlet_format(new_s1, font='doom'))
        print(f'  #--- {new_s2}---#')
        print("-" * 30)


def calc_mod_value(number, math_string):
    if math_string[-1] != "%":
        return eval(math_string)
    else:
        return eval(math_string[0] + str(number * eval(math_string[1:-1])/100))


class TestHelper(unittest.TestCase):
    def test_pure_value(self):
        self.assertEquals(-10, calc_mod_value(5, "-10"))
        self.assertEquals(10, calc_mod_value(10, "10"))
        self.assertEquals(10, calc_mod_value(100, "10"))

    def test_perc_value(self):
        self.assertEquals(-10, calc_mod_value(100, "-10%"))
        self.assertEquals(10, calc_mod_value(100, "+10%"))

    def test_calculation(self):
        mod_value = calc_mod_value(100, "-10%")
        value = 100 + mod_value
        self.assertEquals(90, value)
        mod_value = calc_mod_value(100, "10%")
        value = 100 + mod_value
        self.assertEquals(110, value)
