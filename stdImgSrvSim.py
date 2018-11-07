#!/usr/bin/python           # This is server.py file

import socket               # Import socket module
import random


GET_VERSION     = "GET_VERSION"
GET_META_DATA   = "GET_META_DATA"
GET_IMAGE_DATA  = "GET_IMAGE_DATA"
UNKNOWN_COMMAND = "UNKNOWN COMMAND";

WIDTH_  = 10
HEIGHT_ = 30
COLOR_  =  0
IMG_SIZE = WIDTH_*HEIGHT_

VERSION_STRING   = "IRG STD IMG SRV 1.0.0"
META_DATA_STRING = "[W=%d,H=%d,O=W,C=%d,X=RGB,B=%d,BTS=0]" % (WIDTH_, HEIGHT_, COLOR_, IMG_SIZE)
UNKNOWN_RESPONSE_STRING = "%s please try:\n  %s\n  %s\n  %s\n" % (UNKNOWN_COMMAND, GET_VERSION, GET_META_DATA, GET_IMAGE_DATA)



print(VERSION_STRING)
print(META_DATA_STRING)
print(UNKNOWN_RESPONSE_STRING)


s = socket.socket()         # Create a socket object
#host = socket.gethostname() # Get local machine name
host = socket.gethostbyname('localhost')
port = 34567                # Reserve a port for your service.
s.bind((host, port))        # Bind to the port

s.listen(5)                 # Now wait for client connection.
while True:
   c, addr = s.accept()     # Establish connection with client.
   print ('Got connection from', addr)

   while True:
       request = c.recv(1024)
       print("handle request: " + request)


       if request == GET_VERSION:
           c.send(VERSION_STRING);
       elif request == GET_META_DATA:
           c.send(META_DATA_STRING)
       elif request == GET_IMAGE_DATA:
           for i in range(0, IMG_SIZE):
               c.send(chr(random.randint(0,255)));
       else:
           c.send(UNKNOWN_RESPONSE_STRING)

   print("Closing connection")
   c.close()                # Close the connection
