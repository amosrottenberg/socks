import socket
import threading
import socks_client_packet

class ClientSession:

    def __init__(self, client_ip, client_port, conn):
        self.client_ip = client_ip
        self.client_port = client_port
        self.client_conn = conn
        self.target_ip = None
        self.target_port = None
        self.target_conn = None
        self.seesion_thread = None
        self.new_connection_handler()

    # def start_new_connection(self):

    def new_connection_handler(self):
        with self.client_conn:
            print('Connected by', self.client_ip, self.client_port)
            while True:
                data = self.client_conn.recv(1024)
                print(data)
                client_packet = socks_client_packet.SocksClientPacket()
                client_packet.resolve_data(data)
                # print(str(data.decode('utf-16-le'), "utf-16"))
                data_to_send = client_packet.create_result_packet(90)
                if not data_to_send: break
                self.client_conn.sendall(data_to_send)

if __name__ == '__main__':
    HOST = '127.0.0.1'
    PORT = 1080
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen(1)
        conn, addr = s.accept()
        client = ClientSession(addr[0], addr[1], conn)
