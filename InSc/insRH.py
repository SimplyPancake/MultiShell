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
██████╗ ███████╗██████╗ ██╗  ██╗ █████╗ ██╗    ██╗██╗  ██╗
██╔══██╗██╔════╝██╔══██╗██║  ██║██╔══██╗██║    ██║██║ ██╔╝
██████╔╝█████╗  ██║  ██║███████║███████║██║ █╗ ██║█████╔╝
██╔══██╗██╔══╝  ██║  ██║██╔══██║██╔══██║██║███╗██║██╔═██╗
██║  ██║███████╗██████╔╝██║  ██║██║  ██║╚███╔███╔╝██║  ██╗
╚═╝  ╚═╝╚══════╝╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝ ╚══╝╚══╝ ╚═╝  ╚═╝
_______________
|     By      |
|SimplyPancake|
|_____________|
(\__/) ||
(•ㅅ•) ||
/ 　 \づ
	  """
    print "What to do with RedHawk?:"
    print "1. Run RedHawk"
    print "2. Install RedHawk"
    print "3. Update RedHawk"
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

# run redhawk
def runRH():
    os.system('php RED_HAWK/rhawk.php')
    return

#install redhawk
def insRH():
    os.system('git clone https://github.com/Tuhinshubhra/RED_HAWK.git')
    os.system('clear')
    os.system('python insRH.py')

#update redhawk
def updtRH():
    os.system('cd RED_HAWK && sudo git pull')
    os.system('clear')
    os.system('python insRH.py')

#about
def about():
    print"All in one tool for Information Gathering and Vulnerability Scanning"


# Exit program
def exit():
    sys.exit()

# =======================
#    MENUS DEFINITIONS
# =======================

# Menu definition
menu_actions = {
    'main_menu': main_menu,
    '1': runRH,
    '2': insRH,
    '3': updtRH,
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
