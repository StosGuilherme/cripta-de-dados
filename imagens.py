import os
import pygame
import config

cache = {}                              


def carregar(nome):
    if nome in cache:                   
        return cache[nome]              

    caminho = os.path.join("assets/sprites/" + nome + ".png")
    imagem = pygame.image.load(caminho).convert_alpha()
    largura = imagem.get_width() * config.ESCALA
    altura = imagem.get_height() * config.ESCALA
    imagem = pygame.transform.scale(imagem, (largura, altura))
    cache[nome] = imagem                
    return imagem