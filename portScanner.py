import socket
import threading
import sys
import  pyfiglet
import time
from datetime import datetime 
banner= pyfiglet.figlet_format("PORT SCANNER")
print(banner)
date= datetime.date(datetime.now())
start= time.time()
target = input("Please Enter Host to scan : ")
host = socket.gethostbyname(target)
starting_time = datetime.now()
print("[Start Time ] : {}".format(starting_time.strftime("%H:%M:%S")))
print("[Target] : "+target)
print("[Host] : " + host)
def scan_port(port):
   sock = socket.socket(socket.AF_INET ,socket.SOCK_STREAM)
   sock.settimeout(2)
   result= sock.connect_ex((host ,port))
   if result== 0:
     try:
         print("Port {} is Open Protocol service Name : {}".format(port,socket.getservbyport(port ,'tcp')))
   
     except socket.error:
         print("Port {} is Open Protocol service Name : {}".format(port,"UNKNOWN"))
   sock.close()    
try:
    for port in range(1, 1025):
        # scan_port(port)
        thread = threading.Thread(target= scan_port ,args=(port,))
        thread.start() 
except socket.gaierror:
    print("Hostname could not resolved. Existing")
    sys.exit()
except socket.error:
    print("Could not connect to server. Existing")
    sys.exit()




End_time = datetime.now()
print("[End Time ] : {}".format(End_time.strftime("%H:%M:%S")))
end= time.time()
total_time = End_time-starting_time
print("Total Time  : {}".format(total_time))
totaltime= end-start
print("total time : ",totaltime)