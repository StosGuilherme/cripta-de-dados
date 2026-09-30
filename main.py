import pygame
import config
from jogador import criar_jogador, mover_jogador, desenhar_jogador
from telas import desenha_hud, escrever, montar_chao
from inimigos import criar_inimigo, mover_inimigo, desenhar_inimigo

pygame.init()

tela = pygame.display.set_mode((config.LARGURA, config.ALTURA))
pygame.display.set_caption("Cripta de Dados")
chao = montar_chao()

relogio = pygame.time.Clock()
rodando = True

estado = "jogando"



def nova_partida():
    global jogador, INIMIGOS, proximo_inimigo, vida_jogador, invencivel
    jogador = criar_jogador()
    INIMIGOS = []
    proximo_inimigo = 0
    vida_jogador = config.JOGADOR_VIDA
    invencivel = 0


nova_partida()

while rodando:
    dt = relogio.tick(config.FPS) / 1000
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False
    if estado == "jogando":
        mover_jogador(jogador, dt, pygame.key.get_pressed())
        proximo_inimigo -= dt
        if proximo_inimigo <= 0:
            INIMIGOS.append(criar_inimigo())
            proximo_inimigo = config.INTERVALO_INIMIGO
        invencivel -= dt
        for inimigo in INIMIGOS:
            mover_inimigo(inimigo, dt, jogador)
            if inimigo.colliderect(jogador) and invencivel <= 0:
                vida_jogador -= config.DANO_INIMIGO
                invencivel = config.TEMPO_INVENCIVEL
        if vida_jogador <= 0:
            estado = "FIM DE JOGO"
            
    tela.blit(chao, (0, 0))
    for inimigo in INIMIGOS:
        desenhar_inimigo(tela, inimigo)
    desenhar_jogador(tela, jogador)
    desenha_hud(tela, {"vida": vida_jogador, "inimigos": INIMIGOS})
    if estado == "FIM DE JOGO":
        escrever(tela, "FIM DE JOGO", 64, (255, 0, 0), (config.LARGURA // 2, config.ALTURA // 2))
    pygame.display.flip()

pygame.quit()

