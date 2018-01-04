#!/usr/bin/env python
# -*- coding: utf-8 -*-
#title           :menu.py
#description     :This program displays an interactive menu on CLI
#author          :
#date            :
#version         :0.1
#usage           :
#notes           :
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
███╗   ███╗ █████╗ ███████╗███████╗
████╗ ████║██╔══██╗██╔════╝██╔════╝
██╔████╔██║███████║███████╗███████╗
██║╚██╔╝██║██╔══██║╚════██║╚════██║
██║ ╚═╝ ██║██║  ██║███████║███████║
╚═╝     ╚═╝╚═╝  ╚═╝╚══════╝╚══════╝
                                   
_______________                                                        
|     By      |
|SimplyPancake|
|_____________|
(\__/) || 
(•ㅅ•) || 
/ 　 \づ  
	  """
    print "1. Update all tools(ONLY WORKS IF ALL TOOLS INSTALLED)"
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

#===============
#update
#===============
def upd8():
#Update DZGEN
    os.system('cd InSc/DZGEN && sudo git pull')
    os.system('clear')
#Update Fluxion
    os.system('cd InSc/fluxion && sudo git pull')
    os.system('clear')
#Update FatRat
    os.system('chmod +x InSc/TheFatRat/update && ./InSc/TheFatRat/update && chmod +x InSc/TheFatRat/setup.sh && ./InSc/TheFatRat/setup.sh')
    os.system('clear')
#Update Fsociety
    os.system('chmod +x InSc/fsociety/update.sh && ./InSc/fsociety/update.sh')
    os.system('clear')
#Update RedHawk
    os.system('cd InSc/RED_HAWK && sudo git pull')
    os.system('clear')
#Update routersploit
    os.system('cd InSc/routersploit && sudo git pull')
    os.system('clear')
#Update Trity
    os.system('cd InSc/Trity && sudo git pull')
    os.system('clear')
#Update Yuki Chan
    os.system('cd InSc/Yuki-Chan-The-Auto-Pentest && sudo git pull')
    os.system('clear')


# Exit program
def exit():
    sys.exit()

# =======================
#    MENUS DEFINITIONS
# =======================

# Menu definition
menu_actions = {
    'main_menu': main_menu,
    '1': upd8,
    '99': exit,
}

# =======================
#      MAIN PROGRAM
# =======================

# Main Program
if __name__ == "__main__":
    # Launch main menu
    main_menu()
