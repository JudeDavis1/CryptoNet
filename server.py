'''

TODO:
- Make server multi-threaded and run on parallel
- Add cipher key exchange

'''

import sys
import logger
import socket
import ciphers


class Server:

    def __init__(self, sock, host, port):
        self.sock = sock
        self.host = host
        self.port = port
        self.cipherHandler = ciphers.CipherHandler()


    def run(self):
        self.sock.bind((self.host, self.port))
        self.sock.listen(5)  # start listening

        while True:
            c, addr = self.sock.accept()  # retrieve connection and address when a connection is initialized
            ch = ciphers.CipherHandler()  # object used to encrypt and decrypt data

            ch.keypair_gen()

            c.send(f"KEY:{ch.public_key}".encode("utf-8"))


if __name__ == "__main__":
    logger.INFO("Started running")
    
    server = Server(socket.socket(), "", 3456)
    
    try:
        server.run()
    except KeyboardInterrupt:
        print("\n")
        logger.INFO("Exiting...\n\n")
        server.sock.close()
        sys.exit(1)
