import subprocess

interface = "wlp3s0"
new_mac= "11:22:33:44:55:66"

print("Changing the MAC address of"+ interface + "to" + new_mac)

subprocess.call("ifconfig" + interface + " down", shell=True)
subprocess.call("ifconfig" + interface + "hw" + interface + new_mac, shell=True)
subprocess.call("ifconfig" + interface +  "up", shell=True)
