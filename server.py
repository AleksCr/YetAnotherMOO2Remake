import socket
import json


def server():
    sock = socket.socket()
    sock.bind(('', 1011))
    sock.listen(1)
    conn, addr = sock.accept()

    print('connected:', addr)

    while True:
        raw_data = conn.recv(2048)
        print(raw_data)

        if not raw_data:
            break

        resp_json = {'message': 'ok'}
        response_data = json.dumps(resp_json)
        conn.sendto(response_data.encode(), addr)
        print(response_data)

    conn.close()


if __name__ == "__main__":
    server()