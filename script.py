import platform
import os
for octet in range (254):
    #Assign IP Address
    ip = "128.0.0.{0}".format(octet+1)
    #Find current OS
    current_os = platform.system().lower()
    if current_os == 'windows':
        ping_cmd = f"ping -c 1 -t 2 {ip} > test.txt"
    else:
        ping_cmd = f"ping -c 1 -t 2 {ip} > test.txt 2>&1"
        #run command and capture exit code
    exit_code = os.system(ping_cmd)
    #Print exit code to screen
    print("{0}: {1}".format(ip,exit_code))