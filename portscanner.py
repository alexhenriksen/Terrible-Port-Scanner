#This is a terrible port scanner for high performance
#scans please use Nmapor other portscanning tools

#Future Updates: If a port is open it gets written to a file of choice

import sys
import socket
from datetime import datetime

#Define our Target
if len(sys.argv) == 2:
    target = socket.gethostbyname(sys.argv[1]) #Translates a host name to IPV4
else:
    print("Invalid amount of arguments.")
    print("Syntax: python3 terribleportscanner.py <ip>")
    sys.exit()

#Add a pretty banner
print("-" * 50)
print("Scanning target " + target)
print("Time started: " + str(datetime.now()))
print("-" * 50)

try:
    for port in range(50,8081):
        #change range depending on what ports you want checked
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(0.01) #is a float
        result = s.connect_ex((target,port)) #returns error indicator
        print("Checking port {}".format(port))
        if result == 0:
            print("Port {} is open".format(port))
        s.close()
        
except KeyboardInterrupt:
    print("\nExiting program.")
    sys.exit()

except socket.gaierror:
    print("Hostname could not be resolved.")
    sys.exit()

except socket.error:
    print("Couldn't connect to server")
    sys.exit()
    
