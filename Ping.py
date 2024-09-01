import platform
import os

ip = "128.0.0.1"
current_os = platform.system().lower()
if current_os == 'windows':
    ping_cmd = f"ping -c 1 -t 2 {ip} > test.txt"
else:
    ping_cmd = f"ping -c 1 -t 2 {ip} > test.txt 2>&1"
exit_code = os.system(ping_cmd)
print(exit_code)