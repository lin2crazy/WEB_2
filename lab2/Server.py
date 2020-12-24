import socket
import time
import threading
import datetime
import json


is_send = False
cycle = False
user_list = []
timer_start = ""


def timer():
    global timer_start
    global is_send
    timer_start = str(datetime.datetime.now())
    time.sleep(3)
    is_send = True


def start_server(port):
    global cycle
    global is_send
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('localhost', port))
    server.listen()
    print("Server is listening")
    while True:
        user_socket, address = server.accept()
        data = user_socket.recv(2048)
        users_data = (json.loads(data.decode()))

        user_accept_socket = threading.Thread(target=timer)
        user_accept_socket.start()

        users_data["connection_time"] = str(datetime.datetime.now())
        users_data["timer_start"] = timer_start

        user_list.append(users_data["Name"])
        user_list.append(users_data["connection_time"])
        user_list.append(users_data["timer_start"])

        send_json = json.dumps(user_list)
        print(f"User:{send_json}")

        while not cycle:
            if is_send:
                user_socket.send(send_json.encode())
                break
        is_send = False


if __name__ == '__main__':
    port = 7777
    start_server(port)

