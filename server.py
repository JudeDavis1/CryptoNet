'''

TODO:
- Make server multi-threaded and run on parallel
- Add cipher key exchange

'''

import sys
import time
import logger
import socket
import random
import ciphers
import banners
import threading
from colorama import Fore


class Server:

    def __init__(self, sock, host, port):
        self.sock = sock
        self.host = host
        self.port = port
        self.n_threads = 0
        self.cipherHandler = ciphers.CipherHandler()

    def _did_accept_connection(self, conn):
        print("started threAD	")
        ch = ciphers.CipherHandler()  # object used to encrypt and decrypt data

        ch.keypair_gen()
        conn.send(f"GET_KEY:".encode())
        conn.send(f"{ch.public_key}".encode("utf-8"))

        while True:
            # look for other data or connections
            data = eval(conn.recv(65535).decode())
            logger.INFO("RECIEVED DATA:\n" + ch.decrypt(data) + "\n\n")

    def run(self):
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 0)
        self.sock.bind((self.host, self.port))
        self.sock.listen(5)  # start listening

        logger.INFO("Started running")

        while True:
            c, addr = self.sock.accept()  # retrieve connection and address when a connection is initialized

            logger.INFO("Accepted connection with {}".format(addr))
            thread = threading.Thread(target=self._did_accept_connection(c))
            self.n_threads += 1
            print(self.n_threads)

            thread.start()
            data = c.recv(1024)
            if data == b"Close-Connection":
                logger.INFO("Closing connection with {}".format(addr))
                thread.join()
                c.close()

                break
			
            else:
                logger.INFO(f"Recieved some Data:\n\n{data.decode()}\n\n")

        self.sock.close()


if __name__ == "__main__":
    print(Fore.BLUE + random.choice(banners.banners) + Fore.RESET);time.sleep(1)

    server = Server(socket.socket(), "", int(input("PORT: ")))

    try:
        server.run()
    except KeyboardInterrupt:
        print("\n")
        logger.INFO("Exiting...\n\n")
        server.sock.close()
        sys.exit(1)
