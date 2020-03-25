import socket
import threading
import socks_client_packet

class TargetSession:

    def __init__(self,target_ip, target_port):
        self.target_ip = target_ip
        self.target_port = target_port
        self.target_conn = None
        self.listener_thread = None
        self.sender_thread = None
        
    def create_connection(self):
        self.target_conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.target_conn.connect((self.target_ip, self.target_port))

    def listener_handler(self, send_to_client):
        while True:
            send_to_client.append(self.target_conn.recv(1024))

    def sender_handler(self, send_to_target):
        while True:
            if send_to_target:
                self.target_conn.sendall(send_to_target.pop(0))

    def start_threads(self, send_to_target, send_to_client):
        self.listener_thread = threading.Thread(target=self.listener_handler,
                                              args=(send_to_client,))
        self.sender_thread = threading.Thread(target=self.sender_handler,
                                              args=(send_to_target,))
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
    while True:
            conn, addr = s.accept()
            client = ClientSession(addr[0], addr[1], conn)
