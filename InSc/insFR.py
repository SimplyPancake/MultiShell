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
███████╗ █████╗ ████████╗██████╗  █████╗ ████████╗
██╔════╝██╔══██╗╚══██╔══╝██╔══██╗██╔══██╗╚══██╔══╝
█████╗  ███████║   ██║   ██████╔╝███████║   ██║
██╔══╝  ██╔══██║   ██║   ██╔══██╗██╔══██║   ██║
██║     ██║  ██║   ██║   ██║  ██║██║  ██║   ██║
╚═╝     ╚═╝  ╚═╝   ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝
_______________
|     By      |
|SimplyPancake|
|_____________|
(\__/) ||
(•ㅅ•) ||
/ 　 \づ
	  """
    print "What to do with TheFatRat?:"
    print "1. Run TheFatRat"
    print "2. install TheFatRat"
    print "3. Update TheFatRat"
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
def Install():
    os.system('git clone https://github.com/Screetsec/TheFatRat.git')
    os.system('chmod +x TheFatRat/setup.sh')
    os.system('clear')
    print "somehow, someway, running scripts in python messes up a bit. Please run 'cd TheFatRat && ./setup.sh'. The install script will ask you if you want to create a shortcut. Please answer with 'y', otherwise this script won't work."

#run fatrat
def run():
    os.system('fatrat')

#update fatrat
def updt():
    os.system('chmod +x TheFatRat/update && ./TheFatRat/update && chmod +x TheFatRat/setup.sh && ./TheFatRat/setup.sh')
    os.system('clear')
    os.system('python insFR.py')

#about
def about():
    print"An easy tool to generate backdoor and easy tool to post exploitation attack like browser attack,dll . This tool compiles a malware with popular payload and then the compiled malware can be execute on windows, android, mac . The malware that created with this tool also have an ability to bypass most AV software protection ."

# Back to main menu
def back():
    menu_actions['main_menu']()

# Exit program
def exit():
    sys.exit()

# =======================
#    MENUS DEFINITIONS
# =======================

# Menu definition
menu_actions = {
    'main_menu': main_menu,
    '2': Install,
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
