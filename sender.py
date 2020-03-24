import socketserver
import threading
import managed_tcp_server
import time

class SenderHandeler(socketserver.BaseRequestHandler):
    """
    The request handler class for our server.

    It is instantiated once per connection to the server, and must
    override the handle() method to implement communication to the
    client.
    """

    def handle(self):
        self.request.sendall(bytes(self.server.packet_list.pop(0), "utf-8"))

if __name__ == "__main__":
    HOST, PORT = "localhost", 9999

    # Create the server, binding to localhost on port 9999
    packet_list = ["amos", "ilan", "shira"]
    server = managed_tcp_server.ManagedTCPServer((HOST, PORT), SenderHandeler, packet_list)
        # Activate the server; this will keep running until you
        # interrupt the program with Ctrl-C
    t = threading.Thread(target=server.serve_forever)
    t.daemon = True
    t.start()
    while server.packet_list:
        print(server.packet_list)
    time.sleep(3)