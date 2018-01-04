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
███████╗██╗     ██╗   ██╗██╗  ██╗██╗ ██████╗ ███╗   ██╗
██╔════╝██║     ██║   ██║╚██╗██╔╝██║██╔═══██╗████╗  ██║
█████╗  ██║     ██║   ██║ ╚███╔╝ ██║██║   ██║██╔██╗ ██║
██╔══╝  ██║     ██║   ██║ ██╔██╗ ██║██║   ██║██║╚██╗██║
██║     ███████╗╚██████╔╝██╔╝ ██╗██║╚██████╔╝██║ ╚████║
╚═╝     ╚══════╝ ╚═════╝ ╚═╝  ╚═╝╚═╝ ╚═════╝ ╚═╝  ╚═══╝
_______________                                                        
|     By      |
|SimplyPancake|
|_____________|
(\__/) || 
(•ㅅ•) || 
/ 　 \づ  

WARNING: Fluxion DOES NOT WORK on Linux Subsystem For Windows 10, because the subsystem doesn't allow access to network interfaces. Any Issue regarding the same would be Closed Immediately
	  """
    print "What to do with Fluxion?:"
    print "1. Run Fluxion"
    print "2. Install Fluxion"
    print "3. Update Fluxion"
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
    os.system('git clone https://github.com/FluxionNetwork/fluxion.git')
    os.system('clear')
    os.system('python insFL.py')
    return


# run Fsociety
def runFS():
    os.system('./fluxion/fluxion.sh')

# update Fsociety
def updtFS():
    os.system('cd fluxion && sudo git pull')
    os.system('clear')
    os.system('python insFL.py')

#about
def about():
    print"Fluxion is a security auditing and social-engineering research tool. It is a remake of linset by vk496 with (hopefully) less bugs and more functionality. The script attempts to retrieve the WPA/WPA2 key from a target access point by means of a social engineering (phising) attack. It's compatible with the latest release of Kali (rolling). Fluxion's attacks' setup is mostly manual, but experimental auto-mode handles some of the attacks' setup parameters. Read the FAQ before requesting issues."

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
