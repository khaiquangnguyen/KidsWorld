#!/usr/bin/python
# Version 1

#------ IMPORT ----------

from helpers import *
from player import Player
from pptree import *
import time

#------ GLOBAL VARS -------

global player

#------- FUNCTIONS --------

def create_main_menu():
    clear_screen()
    print (30 * '-')
    print ("   M A I N - M E N U")
    print (30 * '-')
    print ("1. Start Game")
    print ("2. Load Game")
    print ("3. Exit")
    print (30 * '-')

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
        print ("Invalid number. Try again...")


def start_game():
    # clear the screen for a better UI
    clear_screen()
    # get the name of the player from input
    get_player_name()
    print ('-' * 30)
    input ("Press any key on your keyboard to on to next step...")
    # let the player select the skill tree
    player_select_skill_tree()

def get_player_name():
    clear_screen()
    print (30 * '-')
    print ("  C H A R A C T E R - C R E A T I O N")
    print (30 * '-')
    print ()
    print_text_fancily (" - Hey adventurer, what is your name?")    
    player_name = input(" + My name is ")
    print ()
    global player
    player = Player(player_name)
    print_text_fancily(" - That's a cool name, %s! " % player_name)
    print_text_fancily (' - This will be your avatar from now on. \n')
    player.draw_player_shape()
    print_text_fancily(' - Looking good, huh? \n')
    time.sleep(0.5)
    print()
    
def player_select_skill_tree():
    clear_screen()
    print (30 * '-')
    print ("  S E L E C T - S K I L L T R E E")
    print (30 * '-')
    print ()
    print_text_fancily (' - Now, your journey cannot begin without some skills. \n')
    print_text_fancily (' - Which skill tree do you want?')



def load_game():
    print ("Loading up your game files...")

def exit_game():
    print ("Bye Bye ...")


create_main_menu()