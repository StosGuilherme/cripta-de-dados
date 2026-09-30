import random 
import pygame
import config
from imagens import carregar

def criar_inimigo():
    lado = random.choice(["cima", "baixo", "esquerda", "direita"])
    if lado == "cima":
        x = random.randint(0, config.LARGURA)
        y = random.randint(-100, -50)
    elif lado == "baixo":
        x = random.randint(0, config.LARGURA)
        y = random.randint(config.ALTURA + 50, config.ALTURA + 100)
    elif lado == "esquerda":
        x = random.randint(-100, -50)
        y = random.randint(0, config.ALTURA)
    else:  # "direita"
        x = random.randint(config.LARGURA + 50, config.LARGURA + 100)
        y = random.randint(0, config.ALTURA)
        ...
    return carregar("skelet_run_anim_f0").get_frect(center=(x, y))

def mover_inimigo(inimigo, dt, alvo):
    direcao = pygame.Vector2(alvo.center) - pygame.Vector2(inimigo.center)
    if direcao.length() > 0:
        direcao.normalize_ip()
        inimigo.move_ip(direcao * config.INIMIGOS_VELOCIDADE * dt)
    
def desenhar_inimigo(tela, inimigo):
    imagem = carregar("skelet_run_anim_f0")
    tela.blit(imagem, inimigo)
    