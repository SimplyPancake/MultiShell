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
███████╗ ██████╗ ██╗     ███╗   ███╗ █████╗ ██████╗
██╔════╝██╔═══██╗██║     ████╗ ████║██╔══██╗██╔══██╗
███████╗██║   ██║██║     ██╔████╔██║███████║██████╔╝
╚════██║██║▄▄ ██║██║     ██║╚██╔╝██║██╔══██║██╔═══╝
███████║╚██████╔╝███████╗██║ ╚═╝ ██║██║  ██║██║
╚══════╝ ╚══▀▀═╝ ╚══════╝╚═╝     ╚═╝╚═╝  ╚═╝╚═╝
_______________
|     By      |
|SimplyPancake|
|_____________|
(\__/) ||
(•ㅅ•) ||
/ 　 \づ
	  """
    print "What to do with SQLMap?:"
    print "1. Run SQLMap"
    print "2. Install SQLMap"
    print "3. Update SQLMap"
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
    os.system('python sqlmap-dev/sqlmap.py -h')
    choice = raw_input(" Run options >>  ")
    os.system( "python sqlmap-dev/sqlmap.py " + choice)
    return

#update
def updt():
    os.system('cd sqlmap-dev && sudo git pull')
    os.system('clear')
    os.system('python insSM.py')

#install
def install():
    os.system('git clone --depth 1 https://github.com/sqlmapproject/sqlmap.git sqlmap-dev')
    os.system('clear')
    os.system('python insSM.py')

#about
def about():
    print"sqlmap is an open source penetration testing tool that automates the process of detecting and exploiting SQL injection flaws and taking over of database servers. It comes with a powerful detection engine, many niche features for the ultimate penetration tester and a broad range of switches lasting from database fingerprinting, over data fetching from the database, to accessing the underlying file system and executing commands on the operating system via out-of-band connections."


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
