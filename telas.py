import pygame
import config
from imagens import carregar


def montar_chao():
    chao = pygame.Surface((config.LARGURA, config.ALTURA))
    for y in range(0, config.ALTURA, 48):
        for x in range(0, config.LARGURA, 48):
            chao.blit(carregar("floor_1"), (x, y))
    return chao