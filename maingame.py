#!/usr/bin/python
# Version 1

# ------ IMPORT ----------
from helpers import print_text_fancily, clear_screen, print_title_fancily
from player import Player
from shapes import WORLD_MAP
from MathTree import *
import time
from Island import islands
import unittest

# ------ GLOBAL VARS -------

global player

# ------- FUNCTIONS --------


def create_main_menu():
    clear_screen()
    print(30 * '-')
    print("   M A I N - M E N U")
    print(30 * '-')
    print("1. Start Game")
    print("2. Load Game")
    print("3. Exit")
    print(30 * '-')

    choice = input('Enter your choice [1-3] : ')
    choice = int(choice)
    if choice == 1:
        start_game()
    elif choice == 2:
        load_game()
    elif choice == 3:
        exit_game()
    else:  # default ##
        print("Invalid number. Try again...")


def start_game():
    # clear the screen for a better UI
    clear_screen()
    # get the name of the player from input
    get_player_name()
    # let the player select the skill tree
    player_select_skill_tree()


def get_player_name():
    clear_screen()
    print_title_fancily(None, "name selection")
    print_text_fancily(" - Hey adventurer, what is your name? ")
    player_name = input(" + My name is [Type in your name here]: ")
    print()
    global player
    player = Player(player_name)
    print_text_fancily(" - Nice to meet you, %s! " % player_name)
    time.sleep(0.5)
    clear_screen()
    print_text_fancily(
        " - Every knight needs a shiny armor. Please accept it ...")
    player.draw_player_avatar()
    time.sleep(1)
    print_text_fancily(" __ Press any key to accept the armor __ ")
    input()


def player_select_skill_tree():
    global player
    clear_screen()
    print_title_fancily(None, "skill-tree")
    print_text_fancily(
        ' - Now, your journey cannot begin without some skills.')
    print_text_fancily(' - Which skill tree do you want?')
    time.sleep(1)
    skill_tree = MathTree
    skill_tree.show()
    print(30 * '-', "\n")
    print("1. Select Math Tree")
    choice = input('Enter your choice [1] : ')
    print(30 * '-')

    ### Convert string to int type ##
    choice = int(choice)
    if choice == 1:
        player.skill_tree = skill_tree
    print_text_fancily(' - Congratulation! You have a skill tree of your own!')
    time.sleep(1)
    show_character_confirmation()


def show_character_confirmation():
    clear_screen()
    print_title_fancily(None, "final check")
    print_text_fancily(
        "- Now, let's check your character again before we start our journey...")
    global player
    input('Press any key to show the avatar of the player ... \n')
    player.draw_player_avatar()
    input('Press any key to show the skill tree ... \n')
    player.draw_player_skill_tree()
    input('Press any key to show the stats of the character ... \n')
    player.show_player_stats()
    time.sleep(1)
    print_text_fancily(" - Everything seems fine! Let the journey begins!")
    input('Press any key to begin your yourney ...')
    begin_journey()


def begin_journey():
    clear_screen()
    print_title_fancily("KnowLand")
    shape_by_line = WORLD_MAP.split('\n')
    for a_line in shape_by_line:
        print(a_line)
        time.sleep(0.05)
    time.sleep(0.5)
    print_text_fancily(
        "- Welcome to KnowLand, adventurer. Where do you want to go? \n")
    print(30 * '-')
    print("   D E S T I N A T I O N ")
    print(30 * '-')
    for i in range(len(islands)):
        print(f'{(i+1):d}. Go to {islands[i]}')
    print(30 * '-')

    choice = input('Enter your choice [{}] : '.format(len(islands)))
    ### Convert string to int type ##
    choice = islands[int(choice) - 1]
    explore_island(choice)


def explore_island(island_name):
    clear_screen()
    island = globals()[island_name]
    island.show_island_name()


def load_game():
    print("Loading up your game files...")


def exit_game():
    print("Bye Bye ...")


def create_test_char():
    global player
    skill_tree = MathTree
    player = Player("khai")
    player.skill_tree = skill_tree


if __name__ == "__main__":
    create_main_menu()
    # create_test_char()
    # show_character_confirmation()
    # begin_journey()
    pass
