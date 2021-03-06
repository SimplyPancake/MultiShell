#!/usr/bin/env python
# -*- coding: utf-8 -*-
#author          :SimplyPancake
#python_version  :2.7.6
#=======================================================================

# Import the modules needed to run the script.
import sys, os

# Main definition - constants
menu_actions  = {}

# =======================
#     MENUS FUNCTIONS
# =======================

# Main menu
def main_menu():
    os.system('clear')

    print """
██████╗ ███████╗ ██████╗ ███████╗███╗   ██╗
██╔══██╗╚══███╔╝██╔════╝ ██╔════╝████╗  ██║
██║  ██║  ███╔╝ ██║  ███╗█████╗  ██╔██╗ ██║
██║  ██║ ███╔╝  ██║   ██║██╔══╝  ██║╚██╗██║
██████╔╝███████╗╚██████╔╝███████╗██║ ╚████║
╚═════╝ ╚══════╝ ╚═════╝ ╚══════╝╚═╝  ╚═══╝
_______________
|     By      |
|SimplyPancake|
|_____________|
(\__/) ||
(•ㅅ•) ||
/ 　 \づ
	  """
    print "What to do with DZGEN?:"
    print "1. Run DZGEN"
    print "2. Install DZGEN"
    print "3. Update DZGEN"
    print "a. About this tool"
    print "\n99. Quit"
    choice = raw_input(" >>  ")
    exec_menu(choice)

    return

# Execute menu
def exec_menu(choice):
    os.system('clear')
    ch = choice.lower()
    if ch == '':
        menu_actions['main_menu']()
    else:
        try:
            menu_actions[ch]()
        except KeyError:
            print "Invalid selection, please try again.\n"
            menu_actions['main_menu']()
    return

# run
def run():
    os.system('./DZGEN/DZGEN')
    return

#update
def updt():
    os.system('cd DZGEN && sudo git pull')
    os.system('clear')
    os.system('python insDZ.py')

#install
def install():
    os.system('git clone https://github.com/joker25000/DZGEN.git')
    os.system('chmod +x DZGEN/DZGEN')
    os.system('clear')
    os.system('python insDZ.py')

#about
def about():
    print"this tool is working with kali linux tools scan port , Brute force protocol Service ,scan website , exploit system , exploit sql injection website and also have other characteristics"

# Exit program
def exit():
    sys.exit()

# =======================
#    MENUS DEFINITIONS
# =======================

# Menu definition
menu_actions = {
    'main_menu': main_menu,
    '1': run,
    '2': install,
    '3': updt,
    'a': about,
    '99': exit,
}

# =======================
#      MAIN PROGRAM
# =======================

# Main Program
if __name__ == "__main__":
    # Launch main menu
    main_menu()
