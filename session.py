import socket
import threading
import client_session
import target_session

class SessionsManager:

    def __init__(self):
        self.send_to_client = []
        self.send_to_target = []
        self.client_session = None
        self.target_session = None

    def start_sessions(self, client_conn, client_ip, client_port):
        self.client_session = client_session.ClientSession(client_conn, client_ip, client_port)
        target_ip, target_port = self.client_session.new_connection_handler()
        self.target_session = target_session.TargetSession(target_ip, target_port)
        self.target_session.create_connection()
        self.client_session.start_threads(self.send_to_target, self.send_to_client)
        self.target_session.start_threads(self.send_to_target, self.send_to_client)
        while True:
            pass


if __name__ == '__main__':
    HOST = '127.0.0.1'
    PORT = 1080
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen(20)
        while True:
            conn, addr = s.accept()
            session = SessionsManager()
            session.start_sessions(conn, addr[0], addr[1])
        
