import socket
import threading
import sys
import  pyfiglet
from datetime import datetime
import queue


banner= pyfiglet.figlet_format("PORT SCANNER")#Banner of Port scannner 
print(banner)
date= datetime.date(datetime.now())


target = input("Please Enter Host to scan : ")#Get the target or host 
host = socket.gethostbyname(target)

starting_time = datetime.now() #The Starting time 

print("[Start Time ] : {}".format(starting_time.strftime("%H:%M:%S")))
print("[Target] : "+target)
print("[Host] : " + host)


def scan_port(port):# sacan port function
   sock = socket.socket(socket.AF_INET ,socket.SOCK_STREAM)
   sock.settimeout(2)
   result= sock.connect_ex((host ,port))
   if result== 0:
     try:
         print("Port {} is Open Protocol service Name : {}".format(port,socket.getservbyport(port ,'tcp')))
   
     except socket.error:
         print("Port {} is Open Protocol service Name : {}".format(port,"UNKNOWN"))
   sock.close() 
def worker(q): #worker function.. 
    while True:
        port = q.get()
        if port is None:
            break
        scan_port(port)
        q.task_done()
   
try:
    q = queue.Queue()
    threads = []

    # Start worker threads
    for _ in range(1000):  # Adjust the number of threads as needed
        thread = threading.Thread(target=worker, args=(q,))
        threads.append(thread)
        thread.start()

    # Enqueue ports to be scanned
    for port in range(1, 65536):  # Adjust the port range as needed
        q.put(port)

    # Block until all tasks are done
    q.join()

    # Stop the worker threads by enqueuing None for each thread
    for _ in range(len(threads)):
        q.put(None)
    # Wait for all threads to finish
    for thread in threads:
        thread.join()

except socket.gaierror:
    print("Invalid Hostname. Exiting.")
    sys.exit()
except KeyboardInterrupt:
    print("Scan interrupted by user. Exiting.")
    sys.exit()
except Exception as e:
    print(f"An unexpected error occurred: {e}")
    sys.exit()

End_time = datetime.now()
print("[End Time ] : {}".format(End_time.strftime("%H:%M:%S")))
total_time = End_time-starting_time
print("Total Time  : {}".format(total_time))
