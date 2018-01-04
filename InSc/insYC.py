#!/usr/bin/env python
# -*- coding: utf-8 -*-
#title           :menu.py
#description     :This program displays an interactive menu on CLI
#author          :
#date            :
#version         :0.1
#usage           :python menu.py
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
██╗   ██╗██╗   ██╗██╗  ██╗██╗     ██████╗██╗  ██╗ █████╗ ███╗   ██╗
╚██╗ ██╔╝██║   ██║██║ ██╔╝██║    ██╔════╝██║  ██║██╔══██╗████╗  ██║
 ╚████╔╝ ██║   ██║█████╔╝ ██║    ██║     ███████║███████║██╔██╗ ██║
  ╚██╔╝  ██║   ██║██╔═██╗ ██║    ██║     ██╔══██║██╔══██║██║╚██╗██║
   ██║   ╚██████╔╝██║  ██╗██║    ╚██████╗██║  ██║██║  ██║██║ ╚████║
   ╚═╝    ╚═════╝ ╚═╝  ╚═╝╚═╝     ╚═════╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝
_______________                                                        
|     By      |
|SimplyPancake|
|_____________|
(\__/) || 
(•ㅅ•) || 
/ 　 \づ  
	  """
    print "What to do Yuki Chan?:"
    print "1. Run Yuki Chan"
    print "2. Install Yuki Chan"
    print "3. Update Yuki Chan"
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

# install fsociety
def install():
    os.system('git clone https://github.com/Yukinoshita47/Yuki-Chan-The-Auto-Pentest.git')
    os.system('cd Yuki-Chan-The-Auto-Pentest && chmod 777 wafninja joomscan install-perl-module.sh yuki.sh')
    os.system('cd Yuki-Chan-The-Auto-Pentest && chmod 777 Module/WhatWeb/whatweb')
    os.system('pip install -r Yuki-Chan-The-Auto-Pentest/requirements.txt')
    os.system('cd Yuki-Chan-The-Auto-Pentest && ./install perl-module.sh')
    os.system('clear')
    os.system('python insYC.py')
    return


# run Fsociety
def runFS():
    os.system('./Yuki-Chan-The-Auto-Pentest/yuki.sh')

# update Fsociety
def updtFS():
    os.system('cd Yuki-Chan-The-Auto-Pentest && sudo git pull')
    os.system('clear')
    os.system('python insYC.py')

#about
def about():
    print"The Yuki Chan is an Automated Penetration Testing tool this tool will auditing all standard security test method for you."

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
    '1': runFS,
    '3': updtFS,
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
