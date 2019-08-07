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
    # conn, addr = sock.accept()

    # print('connected:', addr)

    while True:

        print('test')
        conn, addr = sock.accept()
        print('connected:', addr)
        time.sleep(2)

        # if conn:
        try:
            raw_data = conn.recv(2048)
        except Exception as e:
            # Some logging if you want
            # raise e
            print(e)

        if not raw_data:
            # conn, addr = sock.accept()
            break

        print(raw_data)
        raw_data = json.loads(raw_data)
        if raw_data['newship']:
            print(raw_data['newship'])
            sh = Ship(raw_data['newship'])
            ships.append(sh)

        # if not raw_data:
        #     break

        full_load_json = []
        for ship in ships:
            full_load_json.append({'ship': ship.get_pos()})
        full_load_json = {'full_update': full_load_json}
        print(full_load_json)
        resp_json = {'message': 'ok'}
        response_data = json.dumps(resp_json)
        # conn.sendto(response_data.encode(), addr)
        full_loadd_json = json.dumps(full_load_json)
        conn.sendto(full_loadd_json.encode(), addr)
        print(response_data)

        conn.close()
    print('kek')


if __name__ == "__main__":
    server()
