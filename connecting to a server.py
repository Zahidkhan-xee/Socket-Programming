import socket
import sys

try:
        sock = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
        print("SystemSOCKET READY to connect")
except socket.error as errmsg:
        print("Error occured while establishing connection with error as %s", (errmsg) )

port = 1234
server_name = "localhost"
try:
    server_ip = "127.0.0.1"   # socket.gethostbyname(server_name)
    print "Address of " , server_name, "is mapping to the IP"
    print "The IP ADDRESS OF " , server_name ," is ", server_ip
except socket as gaierror:
    print("Error in finding IP ADDRESS ");

try:
            sock.connect( (server_ip,port) )
except socket.error as gaierror:
            print "Error in connection TIMEOUT with errror", gaierror
            sock.close()
            exit()
print "the socket has successfully connected to google on port == %s" %(server_ip) 
sock.close()