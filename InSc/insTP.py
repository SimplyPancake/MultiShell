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
███████╗██████╗  █████╗ ██████╗ ███████╗
╚══██╔══╝██╔══██╗██╔══██╗██╔══██╗██╔════╝
   ██║   ██████╔╝███████║██████╔╝█████╗
   ██║   ██╔══██╗██╔══██║██╔═══╝ ██╔══╝
   ██║   ██║  ██║██║  ██║██║     ███████╗
   ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝     ╚══════╝

_______________
|     By      |
|SimplyPancake|
|_____________|
(\__/) ||
(•ㅅ•) ||
/ 　 \づ
	  """
    print "What to do Trape?:"
    print "1. Run Trape"
    print "2. Install Trape"
    print "3. Update Trape"
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

# install
def install():
    os.system('git clone https://github.com/boxug/trape.git')
    os.system('cd trape && pip install requirements.txt')
    os.system('python insTP.py')
    return


# run
def run():
    os.system('python trape/trape.py -h')
    print("Now choose from the menu!")
    choice = raw_input("trape ")
    os.system( "python trape/trape.py " + choice)
    os.system("python insTP.py")
    return

# update
def updt():
    os.system('cd trape && sudo git pull')
    os.system('cd trape && pip install requirements.txt')
    os.system('clear')
    os.system('python insTP.py')

#about
def about():
    print"Trape is a recognition tool that allows you to track people, the information you can get is very detailed. We want to teach the world through this, as large Internet companies could monitor you, obtaining information beyond your IP."

# Exit program
def exit():
    sys.exit()

# =======================
#    MENUS DEFINITIONS
# =======================

# Menu definition
menu_actions = {
    'main_menu': main_menu,
    '2': install,
    '1': run,
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
