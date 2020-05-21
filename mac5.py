# in this version I have handled User Arguments with the optparse Module

import subprocess
import optparse

def input_values():									#this function passes the user argument
	reader = optparse.OptionParser()						    
	reader.add_option("-i","--interface", dest="interface", help="Enter interface")    
	reader.add_option("-m","--mac", dest="new_mac", help="New MAC address")
	return reader.parse_args()							#return the reader object
					    
#interface = values.interface
#new_mac= values.new_mac

def change_mac(interface,new_mac):							#this function changes the MAC
	print("Changing the MAC address of"+ interface + "to" + new_mac)
	subprocess.call(["ifconfig" , interface , " down"])
	subprocess.call(["ifconfig" , interface , "hw" , interface , new_mac])
	subprocess.call(["ifconfig" , interface ,  "up"])

(values,keys) = input_values()
change_mac(values.interface, values.new_mac)




