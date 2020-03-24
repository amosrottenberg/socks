import socketserver
import threading
import managed_tcp_server
import packet

class ListenerHandeler(socketserver.BaseRequestHandler):
    """
    The request handler class for our server.

    It is instantiated once per connection to the server, and must
    override the handle() method to implement communication to the
    client.
    """

    def handle(self):
        # self.request is the TCP socket connected to the client
        self.amos()
        self.data = self.request.recv(1024).strip()
        print("{} wrote:".format(self.client_address[0]))
        print(self.data)
        print(self.client_address)
        client_address, client_port = self.server_address
        # just send back the same data, but upper-cased
        self.server.packet_list.append(packet.Packet(client_address, client_port, self.data))

    def amos(self):
        print("amos")


if __name__ == "__main__":
    HOST, PORT = "localhost", 9999

    # Create the server, binding to localhost on port 9999
    packet_list = []
    server = managed_tcp_server.ManagedTCPServer((HOST, PORT), ListenerHandeler, packet_list)
        # Activate the server; this will keep running until you
        # interrupt the program with Ctrl-C
    t = threading.Thread(target=server.serve_forever)
    t.daemon = True
    t.start()
    # while True:
    #     pass
    while len(server.packet_list) < 2:
    	print(server.packet_list)