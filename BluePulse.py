
import pygame
import random
import math
import sys

pygame.init()

info = pygame.display.Info()
WIDTH, HEIGHT = info.current_w, info.current_h
screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.FULLSCREEN)
pygame.display.set_caption("BluePulse")

data = [HEIGHT // 2] * 256
tiempo = 0
reloj = pygame.time.Clock()

def generar_valor(tiempo):
    ruido_aleatorio = random.uniform(-100, 100)
    sinusoide = 40 * math.sin(tiempo * random.uniform(0.5, 2))
    ruido_perlin = 50 * random.uniform(0, 1)
    pico = random.uniform(80, 150) if random.random() > 0.985 else 0

    valor = HEIGHT / 2 + ruido_aleatorio + sinusoide + ruido_perlin + pico
    return max(0, min(HEIGHT - 1, int(valor)))

while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT or (
            evento.type == pygame.KEYDOWN and evento.key == pygame.K_ESCAPE):
            pygame.quit()
            sys.exit()

    nuevo_valor = generar_valor(tiempo)
    data.pop(0)
    data.append(nuevo_valor)

    screen.fill((0, 0, 0))
    puntos = [
        (i * (WIDTH / len(data)), HEIGHT - y) for i, y in enumerate(data)
    ]
    pygame.draw.lines(screen, (0, 255, 0), False, puntos, 2)
    pygame.draw.line(screen, (0, 100, 0), (0, HEIGHT // 2), (WIDTH, HEIGHT // 2), 1)

    pygame.display.flip()
    tiempo += 0.03
    reloj.tick(30)
