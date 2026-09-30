import pygame
import config
from imagens import carregar

def criar_jogador():
    imagem = carregar("wizzard_m_idle_anim_f0")
    jogador = imagem.get_frect(center=(config.LARGURA // 2, config.ALTURA // 2))
    return jogador

def mover_jogador(jogador, dt, teclas):
    if teclas[pygame.K_w]:
        jogador.y -= config.JOGADOR_VELOCIDADE * dt
    if teclas[pygame.K_s]:
        jogador.y += config.JOGADOR_VELOCIDADE * dt
    if teclas[pygame.K_a]:
        jogador.x -= config.JOGADOR_VELOCIDADE * dt
    if teclas[pygame.K_d]:
        jogador.x += config.JOGADOR_VELOCIDADE * dt
    jogador.clamp_ip(pygame.Rect(0, 0, config.LARGURA, config.ALTURA))

def desenhar_jogador(tela, jogador):
    imagem = carregar("wizzard_m_idle_anim_f0")
    tela.blit(imagem, jogador)