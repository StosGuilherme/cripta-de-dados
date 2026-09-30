import pygame
import config
from jogador import criar_jogador, mover_jogador, desenhar_jogador
from telas import montar_chao

pygame.init()

tela = pygame.display.set_mode((config.LARGURA, config.ALTURA))
pygame.display.set_caption("Cripta de Dados")
chao = montar_chao()

relogio = pygame.time.Clock()
rodando = True
jogador = criar_jogador()


while rodando:
    dt = relogio.tick(config.FPS) / 1000
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False
    mover_jogador(jogador, dt, pygame.key.get_pressed())
    tela.blit(chao, (0, 0))
    desenhar_jogador(tela, jogador)
    pygame.display.flip()

pygame.quit()

