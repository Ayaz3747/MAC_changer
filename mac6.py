# in this version I am using conditional statements for handling error

import subprocess
import optparse

def input_values():									#this function passes the user argument
	reader = optparse.OptionParser()						    
	reader.add_option("-i","--interface", dest="interface", help="Enter interface")    
	reader.add_option("-m","--mac", dest="new_mac", help="New MAC address")
	(values,keys) = reader.parse_args()

	if not values.interface:
		reader.error("Please enter interface name, OR use --help option")               #if user has not
	elif not values.new_mac:								#given interface or new_mac
		reader.error("Please enter new MAC address, OR use --help option")	
	return values			 																
					    


def change_mac(interface,new_mac):							#this function changes the MAC
	print("Changing the MAC address of"+ interface + "to" + new_mac)
	subprocess.call(["ifconfig" , interface , " down"])
	subprocess.call(["ifconfig" , interface , "hw" , interface , new_mac])
	subprocess.call(["ifconfig" , interface ,  "up"])

values = input_values()
change_mac(values.interface, values.new_mac)




