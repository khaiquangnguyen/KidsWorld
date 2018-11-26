# ------ IMPORT ----------

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
        # delete_last_lines()
    if end_with_newline:
        print(s, "\n")
    else:
        print(s)


def print_title_fancily(title=None, subtitle=None):
    print("-" * 30)
    print()
    new_s1 = ""
    new_s2 = ""
    if title is not None:
        title = title.upper()
        for i in title:
            new_s1 += i + " "
    if subtitle is not None:
        subtitle = subtitle.upper()
        for i in subtitle:
            new_s2 += i + " "

    if title and not subtitle:
        cprint(figlet_format(new_s1, font='small'), attrs=['bold'])
        print("-" * 30)
        print()
    elif not title and subtitle:
        print(f'  #--- {new_s2}---#')
    else:
        cprint(figlet_format(new_s1, font='small'), attrs=['bold'])
        print()
        print(f'  #--- {new_s2}---#')
        print()
        print("-" * 30)
    print()
