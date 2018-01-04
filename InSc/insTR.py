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
████████╗██████╗ ██╗████████╗██╗   ██╗
╚══██╔══╝██╔══██╗██║╚══██╔══╝╚██╗ ██╔╝
   ██║   ██████╔╝██║   ██║    ╚████╔╝ 
   ██║   ██╔══██╗██║   ██║     ╚██╔╝  
   ██║   ██║  ██║██║   ██║      ██║   
   ╚═╝   ╚═╝  ╚═╝╚═╝   ╚═╝      ╚═╝   
_______________                                                        
|     By      |
|SimplyPancake|
|_____________|
(\__/) || 
(•ㅅ•) || 
/ 　 \づ  
	  """
    print "What to do with Trity?:"
    print "1. Run Trity"
    print "2. Install Trity"
    print "3. Update Trity"
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

# run trity
def runTR():
    os.system('trity')
    return

#update trity
def updtTR():
    os.system('cd Trity && sudo git pull')
    os.system('clear')
    os.system('python insTR.py')

#install trity
def insTR():
    os.system('git clone https://github.com/toxic-ig/Trity.git')
    os.system('chmod +x Trity/install.py')
    os.system('chmod +x Trity/trity.py')
    os.system('cd Trity')
    os.system('clear')
    print "Somehow, someway, executing scripts in scripts is really hard. Please type 'cd Trity && sudo python install.py'"

#about
def about():
    print"Trity is an advanced pentesting framework dedicated to everything from vulnerability testing to cryptography."


# Exit program
def exit():
    sys.exit()

# =======================
#    MENUS DEFINITIONS
# =======================

# Menu definition
menu_actions = {
    'main_menu': main_menu,
    '1': runTR,
    '2': insTR,
    '3': updtTR,
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
