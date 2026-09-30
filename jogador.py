import pygame
import config

def criar_jogador():
    jogador = pygame.FRect(config.LARGURA // 2 - 20, config.ALTURA // 2 - 20, 40, 40)
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
    pygame.draw.rect(tela, (255, 255, 255), jogador)