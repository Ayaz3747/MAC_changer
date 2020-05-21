# in this version I have handled User Arguments with the optparse Module
import subprocess
import optparse

reader = optparse.OptionParser()						    # here we created reader object

reader.add_option("-i","--interface", dest="interface", help="Enter interface")     # whatever is typed after --interface will go into interface 										              variable. Just like -h or --help
reader.add_option("-m","--mac", dest="new_mac", help="New MAC address")

(values,keys) = reader.parse_args()						    # values are whatever the user type such as wlan0
										    # keys are the arguments like --interface and --mac

interface = values.interface
new_mac= values.new_mac

print("Changing the MAC address of"+ interface + "to" + new_mac)
subprocess.call(["ifconfig" , interface , " down"])
subprocess.call(["ifconfig" , interface , "hw" , interface , new_mac])
subprocess.call(["ifconfig" , interface ,  "up"])




#output commands
# $ python3 mac4.py -i wlan0 -m 11:22:33:44:55:66	OR
# $ python3 mac4.py --interface=wlan0 --new_mac=11:22:33:44:55:66 
