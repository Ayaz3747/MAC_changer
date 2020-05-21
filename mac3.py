import subprocess

interface = input("Enter interface name: ")
new_mac= input("Enter new MAC address in format xx:xx:xx:xx:xx:xx :")

print("Changing the MAC address of"+ interface + "to" + new_mac)
subprocess.call("ifconfig" + interface + " down", shell=True)
subprocess.call("ifconfig" + interface + "hw" + interface + new_mac, shell=True)
subprocess.call("ifconfig" + interface +  "up", shell=True)
