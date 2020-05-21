import subprocess

subprocess.call("ifconfig wlp3s0 down", shell=True)
subprocess.call("ifconfig wlp3s0 hw wlp3s0 00:ab:ba:cd:dc:ff", shell=True)
subprocess.call("ifconfig wlp3s0 up", shell=True)
