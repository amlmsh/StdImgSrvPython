#!/usr/bin/python           # This is client.py file

import socket               # Import socket module
import time

GET_VERSION    = "GET_VERSION";
GET_META_DATA  = "GET_META_DATA";
GET_IMAGE_DATA = "GET_IMAGE_DATA";

s = socket.socket()         # Create a socket object
host = socket.gethostname() # Get local machine name
port = 12345                # Reserve a port for your service.

s.connect((host, port))

s.send(GET_VERSION)
response = s.recv(1024)
print("Version StdImgSrv:   " + response)

s.send(GET_META_DATA)
response = s.recv(1024)
print("Meta data StdImgSrv: " + response)



while True:
    s.send(GET_IMAGE_DATA)
    response = s.recv(1024)
    print("Image data StdImgSrv: " + response)
    time.sleep(2)

