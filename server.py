import log
import socket
import threading


class Server:

    def __init__(self, sock, host, port):
        self.sock = sock
        self.host = host
        self.port = port


    def run(self):
        self.sock.bind((self.host, self.port))
        self.sock.listen(5)  # start listening

        while True:
            c, addr = self.sock.accept()  # retrieve connection and address when a connection is initialized


if __name__ == "__main__":
    log.info("Started running")
    server = Server(socket.socket(), "", 3456)
    thread = threading.Thread(target=server.run)

    thread.start()
