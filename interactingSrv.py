#!/usr/bin/python           # This is server.py file

import socket               # Import socket module


GET_VERSION    = "GET_VERSION";
GET_META_DATA  = "GET_META_DATA";
GET_IMAGE_DATA = "GET_IMAGE_DATA";


s = socket.socket()         # Create a socket object
host = socket.gethostname() # Get local machine name
port = 12345                # Reserve a port for your service.
s.bind((host, port))        # Bind to the port

s.listen(5)                 # Now wait for client connection.
while True:
   c, addr = s.accept()     # Establish connection with client.
   print ('Got connection from', addr)

   while True:
       request = c.recv(1024)
       print("handle request: " + request)


       if request == GET_VERSION:
           c.send("Ver. Std Img Server python 1.0");
       elif request == GET_META_DATA:
           c.send("200x300")
       elif request == GET_IMAGE_DATA:
           c.send("IMAGEDATA")
       else:
           break

   print("Closing connection")
   c.close()                # Close the connection
