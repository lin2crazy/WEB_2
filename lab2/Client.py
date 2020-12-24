import socket
import json


def start_client(port):
    user_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    user_socket.connect(('localhost', port))

    user_name = input("Input a name:")
    user_id = input("Input an ID:")
    user_info = {"Name": user_name, "ID": user_id}

    sending = json.dumps(user_info)
    user_socket.sendall(sending.encode())

    data = user_socket.recv(2048)
    print(f"Users: {data.decode()}")

    user_socket.close()


if __name__ == '__main__':
    port = 7777
    start_client(port)
