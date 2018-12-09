import pygame
import socket
import json


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
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                server.close()
                running = False
            if event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                # print(pos)
                visual_data = send_json_data(server, {'newship': pos})
                if not visual_data:
                    continue
                visual_data = visual_data['full_update']
                for data in visual_data:
                    for type, coords in data.items():
                        heh = type
                        peh = coords
                        screen.blit(logo, peh)

        pygame.display.flip()


def send_json_data(server, send_data):
    s = json.dumps(send_data)
    server.sendto(s.encode(), ('localhost', 9901))

    response_data = server.recv(2048)

    if not response_data:
        return

    response_data = json.loads(response_data)
    print(response_data)
    return response_data


def client():
    pass


if __name__ == "__main__":
    client_main_cycle()
