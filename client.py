#!/Applications/anaconda3/bin/python3

import socket
import ciphers

s = socket.socket()

host = ""
port = 3456

s.connect((host, port))

key = s.recv(1024)

while True:
    text = input("> ")
    s.send(f"BEGIN-DATA:".encode("utf-8"))
