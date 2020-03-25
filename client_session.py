import socket
import threading
import socks_client_packet

class ClientSession:

    def __init__(self, conn, client_ip, client_port):
        self.client_ip = client_ip
        self.client_port = client_port
        self.client_conn = conn
        self.listener_thread = None
        self.sender_thread = None
        
    def new_connection_handler(self):
        print('Connected by', self.client_ip, self.client_port)
        data = self.client_conn.recv(1024)
        print(data)
        client_packet = socks_client_packet.SocksClientPacket()
        client_packet.resolve_data(data)
        data_to_send = client_packet.create_result_packet(90)
        self.client_conn.sendall(data_to_send)
        return (client_packet.remote_address, client_packet.remote_port)

    def listener_handler(self, send_to_target):
        while True:
            send_to_target.append(self.client_conn.recv(1024))

    def sender_handler(self, send_to_client):
        while True:
            if send_to_client:
                self.client_conn.sendall(send_to_client.pop(0))

    def start_threads(self, send_to_target, send_to_client):
        self.listener_thread = threading.Thread(target=self.listener_handler,
                                              args=(send_to_target,))
        self.sender_thread = threading.Thread(target=self.sender_handler,
                                              args=(send_to_client,))
        self.listener_thread.daemon = True
        self.sender_thread.daemon = True
        self.listener_thread.start()
        self.sender_thread.start()


if __name__ == '__main__':
    HOST = '127.0.0.1'
    PORT = 1080
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen(1)
        conn, addr = s.accept()
        client = ClientSession(addr[0], addr[1], conn)
