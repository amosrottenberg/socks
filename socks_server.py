import socketserver
import threading
import managed_tcp_server
import time
import packet

class SocksServer(socketserver.BaseRequestHandler):
    """
    The request handler class for our server.

    It is instantiated once per connection to the server, and must
    override the handle() method to implement communication to the
    client.
    """

    def handle(self):
        receiver_thread = threading.Thread(target=self.receive())
        sender_thread = threading.Thread(target=self.send())
        receiver_thread.daemon = True
        sender_thread.daemon = True
        receiver_thread.start()
        sender_thread.start()
        self.handle_data()

    def receive(self):
        self.data = self.request.recv(1024).strip()
        print(self.data)
        client_address, client_port = self.server.server_address
        self.server.received_packets.append(packet.Packet(client_address, client_port, self.data))
        print(len(self.server.received_packets))

    def send(self):
        if self.server.packets_to_send:
            packet = self.server.packets_to_send.pop(0)
            # self.request.sendto(bytes(packet.data, "utf-8"), (packet.host, packet.port))
            self.request.sendto(packet.data, (packet.host, packet.port))

    def handle_data(self):
        if self.server.received_packets:
            self.server.packets_to_send.append(self.server.received_packets.pop(0))


# if __name__ == "__main__":
#     HOST, PORT = "localhost", 9999

#     # Create the server, binding to localhost on port 9999
#     packet_list = ["amos", "ilan", "shira"]
#     server = managed_tcp_server.ManagedTCPServer((HOST, PORT), SenderHandeler, packet_list)
#         # Activate the server; this will keep running until you
#         # interrupt the program with Ctrl-C
#     t = threading.Thread(target=server.serve_forever)
#     t.daemon = True
#     t.start()
#     while server.packet_list:
#         print(server.packet_list)
#     time.sleep(3)