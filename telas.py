import pygame
import config
from imagens import carregar


def montar_chao():
    chao = pygame.Surface((config.LARGURA, config.ALTURA))
    for y in range(0, config.ALTURA, 48):
        for x in range(0, config.LARGURA, 48):
            chao.blit(carregar("floor_1"), (x, y))
    return chao

def escrever (tela, texto, tamanho, cor, centro):
    fonte = pygame.font.Font(config.FONTE, tamanho)
    superficie_texto = fonte.render(texto, True, cor)
    retangulo_texto = superficie_texto.get_rect(center=centro)
    tela.blit(superficie_texto, retangulo_texto)
    
def desenha_hud (tela, partida):
    escrever(tela, f"Vida: {partida['vida']}", 24, (255, 255, 255), (140, 20))
    escrever(tela, f"Inimigos: {len(partida['inimigos'])}", 24, (255, 255, 255), (170, 50))