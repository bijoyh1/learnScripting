import nmap

#Identify target address
target_address = "45.33.32.156"

#Start and stop port
port_start = 75
port_end = 100

#create scanner
scanner = nmap.PortScanner()

print("Scanning {0}".format(target_address))
#Looping through each port and scan
for port in range(port_start,port_end+1):
    result = scanner.scan(target_address, str(port))
    port_status = result['scan'][target_address]['tcp'][port]['state']
    print("\tPort: {0} is {1}".format(port, port_status))