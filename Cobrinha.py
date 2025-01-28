import pygame
from pygame.locals import *
from sys import exit
from random import randint
pygame.init()


def cobradraw(lista_cobra):
    for move in lista_cobra:
        pygame.draw.rect(tela, (0, 190, 0), (move[0], move[1], 20, 20))


def restart():
    global body, head, x, y, alive, pontos
    body = []
    head = []
    x = 320
    y = 240
    pontos = 0
    alive = False


tempo = pygame.time.Clock()
tela = pygame.display.set_mode((640, 480))
pygame.display.set_caption('Snake game')
x = 320
y = 240
speed = 5
x_path = 5
y_path = 0
z = randint(40, 600)
w = randint(40, 440)
pontos = 0
body = []
alive = False
fonte = pygame.font.SysFont('algerian', 35, True, False)
while True:
    write = fonte.render(f'Pontos: {pontos}', False, (200, 200, 200))
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        if event.type == KEYDOWN:
            if event.key == K_a:
                if x_path == speed:
                    pass
                else:
                    x_path = -speed
                    y_path = 0
            if event.key == K_d:
                if x_path == -speed:
                    pass
                else:
                    x_path = speed
                    y_path = 0
            if event.key == K_w:
                if y_path == speed:
                    pass
                else:
                    y_path = -speed
                    x_path = 0
            if event.key == K_s:
                if y_path == -speed:
                    pass
                else:
                    y_path = speed
                    x_path = 0
    x += x_path
    y += y_path
    tempo.tick(55)
    tela.fill((0, 0, 0))
    cobra = pygame.draw.rect(tela, (0, 190, 0), (x, y, 20, 20))
    maca = pygame.draw.rect(tela, (200, 0, 0), (z, w, 20, 20))
    if cobra.colliderect(maca):
        z = randint(40, 600)
        w = randint(40, 440)
        pontos += 1
    head = []
    head.append(x)
    head.append(y)
    body.append(head)
    if len(body) > pontos+1:
        body.pop(0)
    if body.count(head) > 1 or x > 640 or x < 0 or y > 480 or y < 0:
        alive = True
        while alive:
            tela.fill((0, 0, 0))
            game_over = fonte.render('Game Over. Esc para reiniciar.', False, (240, 0, 0))
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    exit()
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        restart()
            tela.blit(game_over, game_over.get_rect())
            pygame.display.update()
    cobradraw(body)
    tela.blit(write, (410, 35))
    pygame.display.update()
