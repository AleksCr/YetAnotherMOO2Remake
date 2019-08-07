import pygame
import socket
import json
import time


def client_main_cycle():
    pygame.init()
    logo = pygame.image.load("smallship.gif")
    pygame.display.set_icon(logo)
    pygame.display.set_caption("another moo2 remake")

    screen = pygame.display.set_mode((800, 600))

    running = True

    server = socket.socket()
    server.connect(('localhost', 9901))

    while running:
        pygame.time.Clock().tick(60)
        # send_json_data(server, {'data': 'something'})
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                server.close()
                time.sleep(5)
                running = False
            if event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                # print(pos)
                visual_data = send_json_data(server, {'newship': pos})
                if not visual_data:
                    continue
                visual_data = visual_data['full_update']
                # a = visual_data['full_update']
                for data in visual_data:
                    for type, coords in data.items():
                        heh = type
                        peh = coords
                        screen.blit(logo, peh)
                # screen.blit(logo, pos)


        pygame.display.flip()


def send_json_data(server, send_data):
    # server = socket.socket()
    # server.connect(('localhost', 1013))

    # send_data = {'data': 'something'}
    s = json.dumps(send_data)
    server.sendto(s.encode(), ('localhost', 9901))

    response_data = server.recv(2048)
    # server.close()

    if not response_data:
        return

    response_data = json.loads(response_data)
    print(response_data)
    return response_data


def client():
    pass


if __name__ == "__main__":
    client_main_cycle()
