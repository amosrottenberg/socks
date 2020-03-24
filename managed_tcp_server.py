import socketserver

class ManagedTCPServer(socketserver.TCPServer):
    def __init__(self, server_address, RequestHandlerClass, received_packets, packets_to_send, bind_and_activate=True):
        self.received_packets = received_packets
        self.packets_to_send = packets_to_send
        socketserver.TCPServer.__init__(self, server_address, RequestHandlerClass, bind_and_activate=True)
