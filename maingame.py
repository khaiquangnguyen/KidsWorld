#!/usr/bin/python
# Version 1

# ------ IMPORT ----------
from helpers import print_text_fancily, clear_screen, print_title_fancily
from player import Player
from skills import Math_Tree
from islands import islands, MathParadise
from shapes import WORLD_MAP
import time
import sys


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

    ## Get input ###
    choice = input('Enter your choice [1-3] : ')

    ### Convert string to int type ##
    choice = int(choice)

    ### Take action as per selected menu-option ###
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
    print_text_fancily('-' * 30)
    print_text_fancily(
        "Now, when you are ready for next step, just press any key...")
    input("")
    # let the player select the skill tree
    player_select_skill_tree()


def get_player_name():
    clear_screen()
    print_title_fancily("character creation")
    print_text_fancily(" - Hey adventurer, what is your name? ")
    player_name = input(" + My name is [Type in your name here]: ")
    print()
    global player
    player = Player(player_name)
    print_text_fancily(" - That's a cool name, %s! " % player_name)
    print_text_fancily(' - This will be your avatar from now on. \n')
    player.draw_player_avatar()
    print_text_fancily(' - Looking not too shabby, huh? \n')
    time.sleep(0.5)
    print()


def player_select_skill_tree():
    global player
    clear_screen()
    print_title_fancily("select skilltree")

    print_text_fancily(
        ' - Now, your journey cannot begin without some skills. \n')
    print_text_fancily(' - Which skill tree do you want?')
    time.sleep(0.5)
    skill_tree = Math_Tree
    skill_tree.show()
    print(30 * '-', "\n")
    print("1. Select Math Tree")
    ## Get input ###
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
    print_title_fancily("final check")
    print_text_fancily(
        "- Now, let's check your character again before we start our journey...")
    global player
    input('Press any key to show the avatar of the player ...')
    player.draw_player_avatar()
    input('Press any key to show the skill tree ...')
    player.draw_player_skill_tree()
    input('Press any key to show the stats of the character ...')
    player.show_player_stats()
    time.sleep(1)
    print_text_fancily(" - Everything seems fine! Let the journey begins!")
    input('Press any key to begin your yourney ...')
    begin_journey()


def begin_journey():
    clear_screen()
    print_title_fancily("world map")
    shape_by_line = WORLD_MAP.split('\n')
    for a_line in shape_by_line:
        print(a_line)
        time.sleep(0.05)
    time.sleep(0.5)
    print_text_fancily("- Now, let's select a place to explore... \n")
    for i in range(len(islands)):
        print(f'{(i+1):d}. Go to {islands[i]}')
    choice = input('Enter your choice [1-{}] : '.format(len(islands)))
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
    skill_tree = Math_Tree
    player = Player("khai")
    player.skill_tree = skill_tree


if __name__ == "__main__":
    create_main_menu()
    # create_test_char()
    # show_character_confirmation()
    # begin_journey()
