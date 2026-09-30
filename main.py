import pygame

pygame.init()

tela = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Cripta de Dados")

relogio = pygame.time.Clock()
rodando = True

while rodando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False
    tela.fill((20, 15, 25))
    pygame.display.flip()
    relogio.tick(60)

pygame.quit()

