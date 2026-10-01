import pygame
import config
from imagens import carregar

veu = pygame.Surface((config.LARGURA, config.ALTURA), pygame.SRCALPHA)
veu.fill((0, 0, 0, 150))

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
    div, mod = divmod(partida['tempo'], 60)
    escrever(tela, f"Tempo: {int(div)}:{int(mod):02d}", 24, (255, 255, 255), (160, 80))
    
def desenha_menu(tela):
    caixa = desenha_caixa(tela, 760, 490, (config.LARGURA // 2, 420))
    escrever(tela, "CRIPTA DE DADOS", 64, (255, 255, 255), (config.LARGURA // 2, 110))
    escrever(tela, "ENTER - JOGAR", 32, (255, 255, 255), (caixa.centerx, caixa.y + 50))
    escrever(tela, "ESC - SAIR", 32, (255, 255, 255), (caixa.centerx, caixa.y + 100))

    escrever(tela, "CONTROLES:", 32, (255, 255, 255), (caixa.centerx, caixa.y + 180))
    escrever(tela, "W - MOVER PARA CIMA", 24, (255, 255, 255), (caixa.centerx, caixa.y + 235))
    escrever(tela, "S - MOVER PARA BAIXO", 24, (255, 255, 255), (caixa.centerx, caixa.y + 270))
    escrever(tela, "A - MOVER PARA ESQUERDA", 24, (255, 255, 255), (caixa.centerx, caixa.y + 305))
    escrever(tela, "D - MOVER PARA DIREITA", 24, (255, 255, 255), (caixa.centerx, caixa.y + 340))
    escrever(tela, "ESC - PAUSAR", 24, (255, 255, 255), (caixa.centerx, caixa.y + 375))
    escrever(tela, "MOUSE - MIRAR", 24, (255, 255, 255), (caixa.centerx, caixa.y + 410))
    escrever(tela, "BOTAO ESQUERDO - ATIRAR", 24, (255, 255, 255), (caixa.centerx, caixa.y + 445))
     
def desenha_modal(tela, titulo, cor_titulo, linha1, linha2):
    caixa = desenha_caixa (tela, 720, 260, (config.LARGURA // 2, config.ALTURA // 2))    

    escrever(tela, titulo, 48, cor_titulo, (caixa.centerx, caixa.y + 60))        
    escrever(tela, linha1, 32, (255, 255, 255), (caixa.centerx, caixa.y + 140))
    escrever(tela, linha2, 32, (255, 255, 255), (caixa.centerx, caixa.y + 190))
    
def desenha_caixa (tela, largura, altura, centro):
    tela.blit(veu, (0, 0))
    caixa = pygame.Rect(0, 0, largura, altura)
    caixa.center = centro
    
    pygame.draw.rect(tela, (30, 22, 30), caixa, border_radius=10)          
    pygame.draw.rect(tela, (240, 200, 80), caixa, 4, border_radius=10)
    
    return caixa