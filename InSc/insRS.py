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
██████╗       ███████╗██████╗ ██╗      ██████╗ ██╗████████╗
██╔══██╗      ██╔════╝██╔══██╗██║     ██╔═══██╗██║╚══██╔══╝
██████╔╝█████╗███████╗██████╔╝██║     ██║   ██║██║   ██║   
██╔══██╗╚════╝╚════██║██╔═══╝ ██║     ██║   ██║██║   ██║   
██║  ██║      ███████║██║     ███████╗╚██████╔╝██║   ██║   
╚═╝  ╚═╝      ╚══════╝╚═╝     ╚══════╝ ╚═════╝ ╚═╝   ╚═╝   
                                                          
_______________                                                        
|     By      |
|SimplyPancake|
|_____________|
(\__/) || 
(•ㅅ•) || 
/ 　 \づ  
	  """
    print "What to do with Routersploit?:"
    print "1. Run Routersploit"
    print "2. Install Routersploit for Kali"
    print "3. Install Routersploit for Ubuntu 16.04"
    print "4. Update Routersploit"
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
    os.system('./routersploit/rsf.py')
    return

#install for kali
def insRHK():
    os.system('pip install requests')
    os.system('pip install paramiko')
    os.system('pip install beautifulsoup4')
    os.system('pip install pysnmp')
    os.system('git clone https://github.com/reverse-shell/routersploit')
    os.system('clear')
    os.system('python insRS.py')

#install for Ubuntu 16.04
def insRHU():
    os.system('pip install requests')
    os.system('pip install paramiko')
    os.system('pip install beautifulsoup4')
    os.system('pip install pysnmp')
    os.system('sudo apt-get install python-dev python-pip libncurses5-dev git')
    os.system('git clone https://github.com/reverse-shell/routersploit')
    os.system('cd routersploit && sudo pip install -r requirements.txt')

#update redhawk
def updtRH():
    os.system('cd routersploit && sudo git pull')
    os.system('clear')
    os.system('python insRS.py')

#about
def about():
    print"""
The RouterSploit Framework is an open-source exploitation framework dedicated to embedded devices. It consists of various modules that aids penetration testing operations:

exploits - modules that take advantage of identified vulnerabilities
creds - modules designed to test credentials against network services
scanners - modules that check if a target is vulnerable to any exploit
"""

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
    '2': insRHK,
    '3': insRHU,
    '4': updtRH,
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
