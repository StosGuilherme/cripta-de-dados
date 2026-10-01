import pygame
import config


def criar_tiro(origem, mira):
    direcao = pygame.Vector2(mira) - pygame.Vector2(origem)   
    if direcao.length() > 0:
        direcao.normalize_ip()
    rect = pygame.FRect(0, 0, 12, 12)
    rect.center = pygame.Vector2(origem)                     
    return {"rect": rect, "direcao": direcao}


def mover_tiros(tiros, dt):
    area = pygame.Rect(0, 0, config.LARGURA, config.ALTURA)
    for tiro in tiros[:]:
        tiro["rect"].move_ip(tiro["direcao"] * config.TIRO_VELOCIDADE * dt)
        if not area.colliderect(tiro["rect"]):             
            tiros.remove(tiro)                              


def desenhar_tiros(tela, tiros):
    for tiro in tiros:
        pygame.draw.circle(tela, (255, 140, 40), tiro["rect"].center, 6)