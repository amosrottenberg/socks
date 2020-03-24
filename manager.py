import socks_server
import managed_tcp_server

HOST, PORT = "localhost", 9999


if __name__ == "__main__":

    recived_packets = []
    packets_to_send = []
    socket_server = managed_tcp_server.ManagedTCPServer((HOST, PORT), socks_server.SocksServer, recived_packets, packets_to_send)
    socket_server.serve_forever()
    while True:
        print("here")
        if recived_packets:
            packets_to_send.append(recived_packets.pop(0))


        
    