#! /usr/bin/env python 

import subprocess
import optparse
import pyfiglet
from colorama import Fore 

banner = pyfiglet.figlet_format("MAC-CHANGER")
pyfiglet.figlet_format(banner , font='digital')
print(Fore.GREEN + banner)
dis= "MADE BY XABIT ONLY FOR EDUCATIONAL PURPOSES AND SAFETY use --help "
print(Fore.RED + dis)
change = "[+]mac address has started to change ........."
change2 = "your mac address was changed successfully !"
print(Fore.YELLOW + change,change2)
parser= optparse.OptionParser()
parser.add_option("-i" , "--interface" , dest="interface" , help="for interface")
parser.add_option("-m" , "--mac" , dest="new_mac" , help=" new mac")

(options , arguments)=parser.parse_args()


interface=options.interface
new_mac=options.new_mac


def change_mac(interface , new_mac):
    subprocess.call(["ifconfig" , interface , "down" ])
    subprocess.call(["ifconfig" , interface , "hw" , "ether" , new_mac])
    subprocess.call(["ifconfig" , interface , "up" ])
    
    
change_mac(options.interface,options.new_mac)
    

    
