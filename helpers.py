#------ IMPORT ----------

import sys
import time

#------- FUNCTIONS --------

CURSOR_UP_ONE = '\x1b[1A'
ERASE_LINE = '\x1b[2K'
TEXT_DELAY = 0.02

def delete_last_lines(n=1):
    for _ in range(n):
        sys.stdout.write(CURSOR_UP_ONE)
        sys.stdout.write(ERASE_LINE)

def clear_screen():
    print('\033[H\033[J')

def print_text_fancily(s,delay = TEXT_DELAY):
    for i in range(len(s)):
        time.sleep(delay)
        print (s[:i])
        delete_last_lines()
    print (s, "\n")



