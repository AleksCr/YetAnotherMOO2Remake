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

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False


def send_json_data():
    server = socket.socket()
    server.connect(('localhost', 1011))

    send_data = {'data': 'something'}
    s = json.dumps(send_data)
    server.sendto(s.encode(), ('localhost', 1011))

    response_data = server.recv(1024)
    server.close()

    print(response_data)


def client():
    pass


if __name__ == "__main__":
    client_main_cycle()
    send_json_data()