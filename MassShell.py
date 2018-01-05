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
    print "1. Install all tools(INSTALLS ROUTERSPLOIT KALI VERSION)"
    print "2. Update all tools(ONLY WORKS IF ALL TOOLS INSTALLED)"
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
#Update FatRat
    os.system('chmod +x InSc/TheFatRat/update && ./InSc/TheFatRat/update && chmod +x InSc/TheFatRat/setup.sh && ./InSc/TheFatRat/setup.sh')
    os.system('clear')
#Go back to main menu
    os.system('python MassShell.py')

#================
#install all
#================
def installall():
#install DZGEN
    os.system('cd InSc && git clone https://github.com/joker25000/DZGEN.git')
    os.system('chmod +x InSc/DZGEN/DZGEN')
    os.system('clear')
#install Fluxion
    os.system('cd InSc && git clone https://github.com/FluxionNetwork/fluxion.git')
    os.system('clear')
#install fsociety
    os.system('cd InSc && git clone https://github.com/Manisso/fsociety.git')
    os.system('./fsociety/install.sh')
    os.system('clear')
#install redhawk
    os.system('cd InSc && git clone https://github.com/Tuhinshubhra/RED_HAWK.git')
    os.system('clear')
#install routersploit for kali
    os.system('pip install requests')
    os.system('pip install paramiko')
    os.system('pip install beautifulsoup4')
    os.system('pip install pysnmp')
    os.system('cd InSc && git clone https://github.com/reverse-shell/routersploit')
    os.system('clear')
#install yuki chan
    os.system('cd InSc && git clone https://github.com/Yukinoshita47/Yuki-Chan-The-Auto-Pentest.git')
    os.system('cd InSc/Yuki-Chan-The-Auto-Pentest && chmod 777 wafninja joomscan install-perl-module.sh yuki.sh')
    os.system('cd InSc/Yuki-Chan-The-Auto-Pentest && chmod 777 Module/WhatWeb/whatweb')
    os.system('pip install -r InSc/Yuki-Chan-The-Auto-Pentest/requirements.txt')
    os.system('cd InSc/Yuki-Chan-The-Auto-Pentest && ./install perl-module.sh')
    os.system('clear')
#print msg to install trity and fatrat.
    os.system('clear')
    print "Please install Trity and TheFatRat manually, because python..."

#install trity
#    os.system('git clone https://github.com/toxic-ig/Trity.git')
#    os.system('chmod +x Trity/install.py')
#    os.system('chmod +x Trity/trity.py')
#    os.system('cd Trity')
#    os.system('clear')
#    print "Somehow, someway, executing scripts in scripts is really hard. #Please type 'cd Trity && sudo python install.py. After that is completed, #please type 'cd ..' '
#install FatRat (install last)
#    os.system('git clone https://github.com/Screetsec/TheFatRat.git')
#    os.system('chmod +x TheFatRat/setup.sh')
#    os.system('clear')
#    print "somehow, someway, running scripts in python messes up a bit. #Please run 'cd TheFatRat && ./setup.sh'. The install script will ask you #if you want to create a shortcut. Please answer with 'y', otherwise this #script won't work."

# Exit program
def exit():
    sys.exit()

# =======================
#    MENUS DEFINITIONS
# =======================

# Menu definition
menu_actions = {
    'main_menu': main_menu,
    '1': installall,
    '2': upd8,
    '99': exit,
}

# =======================
#      MAIN PROGRAM
# =======================

# Main Program
if __name__ == "__main__":
    # Launch main menu
    main_menu()
