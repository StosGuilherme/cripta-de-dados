import pygame
import config
from jogador import criar_jogador, mover_jogador, desenhar_jogador
from telas import desenha_hud, escrever, montar_chao, desenha_menu, desenha_modal
from inimigos import criar_inimigo, mover_inimigo, desenhar_inimigo
from tiros import criar_tiro, mover_tiros, desenhar_tiros

pygame.init()

tela = pygame.display.set_mode((config.LARGURA, config.ALTURA))
pygame.display.set_caption("Cripta de Dados")
chao = montar_chao()

relogio = pygame.time.Clock()
rodando = True

estado = "menu"



def nova_partida():
    global jogador, INIMIGOS, tiros, recarga, proximo_inimigo, vida_jogador, invencivel, tempo
    jogador = criar_jogador()
    INIMIGOS = []
    tiros = []
    recarga = 0
    proximo_inimigo = 0
    vida_jogador = config.JOGADOR_VIDA
    invencivel = 0
    tempo = 0 


nova_partida()

while rodando:
    dt = relogio.tick(config.FPS) / 1000

    # ---------- EVENTOS ----------
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False
        if evento.type == pygame.KEYDOWN:
            if estado == "menu":
                if evento.key == pygame.K_RETURN:
                    estado = "jogando"
                    nova_partida()
                elif evento.key == pygame.K_ESCAPE:
                    rodando = False
            elif estado == "jogando":
                if evento.key == pygame.K_ESCAPE:
                    estado = "pausa"
            elif estado == "pausa":
                if evento.key == pygame.K_ESCAPE:
                    estado = "jogando"
                if evento.key == pygame.K_RETURN:
                    estado = "menu"
            elif estado in ["FIM DE JOGO", "VITÓRIA"]:
                if evento.key == pygame.K_RETURN:
                    estado = "jogando"
                    nova_partida()
                elif evento.key == pygame.K_ESCAPE:
                    estado = "menu"

    # ---------- ATUALIZAR ----------
    if estado == "jogando":
        tempo += dt
        if tempo >= config.TEMPO_VITORIA:
            estado = "VITÓRIA"
        mover_jogador(jogador, dt, pygame.key.get_pressed())
        recarga -= dt
        if pygame.mouse.get_pressed()[0] and recarga <= 0:
            tiros.append(criar_tiro(jogador.center, pygame.mouse.get_pos()))
            recarga = config.TIRO_RECARGA
        mover_tiros(tiros, dt)
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

    # ---------- DESENHAR ----------
    tela.blit(chao, (0, 0))
    if estado == "menu":
        desenha_menu(tela)
    else:
        for inimigo in INIMIGOS:
            desenhar_inimigo(tela, inimigo)
        desenhar_jogador(tela, jogador)
        desenhar_tiros(tela, tiros)
        desenha_hud(tela, {"vida": vida_jogador, "inimigos": INIMIGOS, "tempo": tempo})
        if estado == "FIM DE JOGO":
            desenha_modal(tela, "FIM DE JOGO", (255, 0, 0), "ENTER - Jogar de novo", "ESC - Menu")
        if estado == "pausa":
            desenha_modal(tela, "PAUSADO", (255, 255, 0), "ESC - Retomar", "ENTER - Menu")
        if estado == "VITÓRIA":
            desenha_modal(tela, "VITORIA!", (0, 255, 0), "ENTER - Jogar de novo", "ESC - Menu")
    pygame.display.flip()

pygame.quit()

