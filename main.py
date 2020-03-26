import socket
import session

HOST = '10.100.102.14'
PORT = 1080

def main():
    sessions_list = []
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen(50)
        while True:
            conn, addr = s.accept()
            client_sessios = session.SessionsManager()
            client_sessios.start_sessions(conn, addr[0], addr[1])
            sessions_list.append(client_sessios)
            print(addr)
            print(len(sessions_list))


if __name__ == '__main__':
    main()