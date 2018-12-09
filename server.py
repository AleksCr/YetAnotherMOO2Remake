import socket
import json
import time

ships = []


class Ship:

    def __init__(self, pos):
        self.x, self.y = pos

    def get_pos(self):
        return self.x, self.y


def server():
    sock = socket.socket()
    sock.bind(('', 9901))
    sock.listen(1)

    while True:

        print('test')
        conn, addr = sock.accept()
        print('ree')

        while True:
            try:
                raw_data = conn.recv(2048)
            except socket.error:
                print('client disconnected')
                conn.close()
                break

            if not raw_data:
                break

            print(raw_data)
            raw_data = json.loads(raw_data)
            if raw_data['newship']:
                print(raw_data['newship'])
                sh = Ship(raw_data['newship'])
                ships.append(sh)

            full_load_json = []
            for ship in ships:
                full_load_json.append({'ship': ship.get_pos()})
            full_load_json = {'full_update': full_load_json}
            print(full_load_json)
            resp_json = {'message': 'ok'}
            response_data = json.dumps(resp_json)
            full_loadd_json = json.dumps(full_load_json)
            conn.sendto(full_loadd_json.encode(), addr)
            print(response_data)
    print('kek')


if __name__ == "__main__":
    server()
