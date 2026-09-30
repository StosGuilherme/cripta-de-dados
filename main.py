import pygame
import config
from jogador import criar_jogador, mover_jogador, desenhar_jogador
from telas import montar_chao
from inimigos import criar_inimigo, mover_inimigo, desenhar_inimigo

pygame.init()

tela = pygame.display.set_mode((config.LARGURA, config.ALTURA))
pygame.display.set_caption("Cripta de Dados")
chao = montar_chao()

relogio = pygame.time.Clock()
rodando = True
jogador = criar_jogador()

INIMIGOS = []
proximo_inimigo = 0



while rodando:
    dt = relogio.tick(config.FPS) / 1000
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False
    mover_jogador(jogador, dt, pygame.key.get_pressed())
    proximo_inimigo -= dt
    if proximo_inimigo <= 0:
        INIMIGOS.append(criar_inimigo())
        proximo_inimigo = config.INTERVALO_INIMIGO
    tela.blit(chao, (0, 0))
    for inimigo in INIMIGOS:
        mover_inimigo(inimigo, dt, jogador)
        desenhar_inimigo(tela, inimigo)
    desenhar_jogador(tela, jogador)
    pygame.display.flip()

pygame.quit()

