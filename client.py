#!/Applications/anaconda3/bin/python3

import time
import socket
import ciphers
import threading

s = socket.socket()

host = ""
port = int(input("PORT: "))

s.connect((host, port))
ch = ciphers.CipherHandler()

time.sleep(1)

if s.recv(8).decode() == "GET_KEY:":
    print("recieved key")
    public_key = eval(s.recv(1024).decode())
    ch.public_key = public_key

print(ch.public_key)

while True:
    text = input('> ')

    ch.encrypt(text)
    s.send(str(ch.ciphertext).encode())
