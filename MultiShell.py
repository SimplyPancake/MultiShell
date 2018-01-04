#!/usr/bin/env python
# -*- coding: utf-8 -*-
#title           :multiSH.py
#description     :This program displays an interactive menu on CLI
#author          :SimplyPancake
#date            :
#version         :0.1
#usage           :
#notes           :
#python_version  :2.7.6  
#================================================================
				#SETUP
#================================================================
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
    
    print"""
███╗   ███╗██╗   ██╗██╗  ████████╗██╗   ███████╗██╗  ██╗
████╗ ████║██║   ██║██║  ╚══██╔══╝██║   ██╔════╝██║  ██║
██╔████╔██║██║   ██║██║     ██║   ██║   ███████╗███████║
██║╚██╔╝██║██║   ██║██║     ██║   ██║   ╚════██║██╔══██║
██║ ╚═╝ ██║╚██████╔╝███████╗██║   ██║██╗███████║██║  ██║
╚═╝     ╚═╝ ╚═════╝ ╚══════╝╚═╝   ╚═╝╚═╝╚══════╝╚═╝  ╚═╝
v1.6
_______________                                                        
|     By      |
|SimplyPancake|
|_____________|
(\__/) || 
(•ㅅ•) || 
/ 　 \づ  
"""
    print "Please choose the menu you want to start:"
    print "1. Fsociety"
    print "2. RED_HAWK"
    print "3. TheFatRat"
    print "4. Trity"
    print "5. DZGEN"
    print "6. Fluxion"
    print "7. Yuki-Chan"
    print "8. RouterSploit"
    print "m. Enter mass-action menu(DOES NOT WORK FOR SOME REASON)"
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

# fsociety
def fsociety():
    os.system('cd InSc && python insFS.py')
    return


# redhawk
def redhawk():
    os.system('cd InSc && python insRH.py')
    return

#fatrat
def fatrat():
    os.system('cd InSc && python insFR.py')

#trity
def trity():
    os.system('cd InSc && python insTR.py')

#dzgen
def dzgen():
    os.system('cd InSc && python insDZ.py')

#fluxion
def fluxion():
    os.system('cd InSc && python insFL.py')

#yuki
def yuki():
    os.system('cd InSc && python insYC.py')

#routersploit
def rsploit():
    os.system('cd InSc && python insRS.py')

#mass action menu
def mass():
    os.system('python MassUpdate.py')

# Exit program
def exit():
    sys.exit()

# =======================
#    MENUS DEFINITIONS
# =======================

# Menu definition
menu_actions = {
    'main_menu': main_menu,
    '1': fsociety,
    '2': redhawk,
    '3': fatrat,
    '4': trity,
    '5': dzgen,
    '6': fluxion,
    '7': yuki,
    '8': rsploit,
    'm': mass,
    '99': exit,
}

# =======================
#      MAIN PROGRAM
# =======================

# Main Program
if __name__ == "__main__":
    # Launch main menu
    main_menu()
