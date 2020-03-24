import socketserver

class ManagedTCPServer(socketserver.TCPServer):
    def __init__(self, server_address, RequestHandlerClass, bind_and_activate=True, packet_list):
	   self.packet_list = packet_list
	   socketserver.TCPServer.__init__(self, server_address, RequestHandlerClass, bind_and_activate=True)
