# Roteiro do trabalho

Entrega: **12/10/2026**. ZIP com o exe e a pasta `assets` ao lado.

Jogo: **atirador na arena**. O jogador anda com WASD, mira com o mouse e atira com o clique. Os inimigos perseguem o jogador.

Documentação do pygame-ce: https://pyga.me/docs/

## Como usar este roteiro

- Faça um passo por vez. Só passe para o próximo quando o "Pronto quando" funcionar.
- Para rodar: abra o terminal do VS Code (Ctrl+') na pasta do projeto e rode `python main.py`.
- Travou? Mande o código e a mensagem de erro inteira.
- Ao terminar cada passo, faça um commit:
  ```
  git add .
  git commit -m "Passo 1: janela"
  ```

## Python que você vai usar

- variáveis, `if`/`elif`/`else`, `while`, `for`
- listas: `append`, `remove`, percorrer com `for`
- dicionários: guardar valores por nome (`partida["vida"]`)
- funções com parâmetros e `return`
- importar seus próprios arquivos (`import config` e depois `config.LARGURA`)

Não precisa de classe.

## Como os arquivos vão ficar no final

```
main.py      loop principal, eventos e estados (menu, jogando, fim)
config.py    números do jogo: tamanho da tela, velocidades, vida...
imagens.py   carregar as imagens da pasta assets
jogador.py   criar, mover e desenhar o jogador
inimigos.py  criar, mover e desenhar os inimigos
tiros.py     criar, mover e desenhar os tiros
telas.py     escrever texto, HUD, menu e tela de fim
```

Cada arquivo é criado no passo em que ele é necessário.

## Antes de começar

- [ ] Perguntar ao professor/tutor, pelo AVA, se pode usar IA como apoio (e como declarar).

---

# Parte 1: jogo completo, sem tiro

Ao fim da Parte 1 o jogo já cumpre todos os requisitos: sobreviver X segundos na arena.
Se o tempo apertar, ela já é entregável.

## Passo 1: janela

**Arquivos:** `main.py`

1. No `main.py`, importe o `pygame`.
2. Chame `pygame.init()`.
3. Crie a janela de 1280x720 com `pygame.display.set_mode` e guarde numa variável `tela`.
4. Dê um título à janela com `pygame.display.set_caption`.
5. Crie um relógio com `pygame.time.Clock` e guarde numa variável `relogio`.
6. Crie uma variável `rodando = True` e um `while` que repete enquanto ela for verdadeira.
7. Dentro do `while`, percorra os eventos de `pygame.event.get()` com um `for`. Se o tipo do evento for `pygame.QUIT` (clicou no X), `rodando` vira `False`.
8. Ainda dentro do `while`, depois do `for`:
   - pinte o fundo com `tela.fill`, usando uma cor escura em RGB, por exemplo `(20, 15, 25)`;
   - mostre o quadro com `pygame.display.flip()`;
   - chame `relogio.tick(60)` para o jogo rodar a 60 quadros por segundo.
9. Depois do `while`, fora dele, chame `pygame.quit()`.

**Pronto quando:** a janela abre com fundo escuro, fica aberta e fecha no X sem erro.

**Cuidado:** em Python, a indentação define o que está dentro do `while` e do `for`.

## Passo 2: config e um quadrado que anda

**Arquivos:** `config.py` (novo), `jogador.py` (novo), `main.py`

1. Crie o `config.py` só com números, em MAIÚSCULAS: `LARGURA = 1280`, `ALTURA = 720`, `FPS = 60`, `COR_FUNDO` e `JOGADOR_VELOCIDADE = 250` (pixels por segundo).
2. No `main.py`, importe o `config` e troque os números soltos pelas constantes (`config.LARGURA`...).
3. **dt (delta time):** `relogio.tick` devolve quantos milissegundos passaram desde o último quadro. Divida por 1000 e guarde numa variável `dt`, que fica em segundos. Faça isso no começo de cada volta do `while`.
   Movimento = velocidade × dt. Assim o jogo tem a mesma velocidade em qualquer computador.
4. Crie o `jogador.py`, importando `pygame` e `config`. Nele:
   - a função `criar_jogador()` devolve um `pygame.FRect` de 40x40 no centro da tela. Um FRect é um retângulo que guarda posição e tamanho, e aceita números com vírgula;
   - a função `mover_jogador(jogador, teclas, dt)`: com W o `y` diminui velocidade × dt, com S aumenta, com A o `x` diminui, com D aumenta. As teclas são `pygame.K_w`, `pygame.K_s`, `pygame.K_a` e `pygame.K_d`. No fim, prenda o jogador dentro da tela com `jogador.clamp_ip(...)`, passando um `pygame.Rect` do tamanho da tela;
   - a função `desenhar_jogador(tela, jogador)` desenha o retângulo com `pygame.draw.rect`.
5. No `main.py`, importe as funções com `from jogador import criar_jogador, mover_jogador, desenhar_jogador`.
6. Antes do `while`, crie o jogador. Dentro do `while`, depois dos eventos:
   - pegue as teclas com `pygame.key.get_pressed()` e chame `mover_jogador`;
   - depois do `tela.fill`, chame `desenhar_jogador`.

**Pronto quando:** o quadrado anda com WASD e não sai da tela.

**Cuidado:**
- Não faça `import jogador` e depois uma variável chamada `jogador`: a variável esconde o arquivo. Por isso o passo 5 usa `from ... import`.
- Desenhe depois do `fill`, senão o fundo cobre o jogador.
- Na diagonal o jogador anda mais rápido. Por enquanto, tudo bem.

## Passo 3: imagens

**Arquivos:** `imagens.py` (novo), `jogador.py`, `config.py`, `main.py`

1. No `config.py`, adicione `ESCALA = 3`. Os sprites são pequenos (16 pixels) e vão ser aumentados 3 vezes.
2. Crie o `imagens.py` com a função `carregar(nome)`:
   - monte o caminho `"assets/sprites/" + nome + ".png"`;
   - carregue com `pygame.image.load`, chame `.convert_alpha()` (deixa o desenho rápido e mantém a transparência) e aumente com `pygame.transform.scale_by(imagem, config.ESCALA)`;
   - **cache:** crie um dicionário vazio fora da função. Antes de carregar, veja se o nome já está no dicionário e, se estiver, devolva de lá. Assim o arquivo não é lido do disco 60 vezes por segundo.
3. No `jogador.py`:
   - `criar_jogador()` agora pega a imagem com `carregar("wizzard_m_idle_anim_f0")` e devolve `imagem.get_frect(center=...)`, com o centro da tela. O retângulo fica do tamanho da imagem;
   - `desenhar_jogador` troca o `draw.rect` por `tela.blit(imagem, jogador)`.
4. **(Opcional) Chão:** antes do `while`, crie uma `pygame.Surface` do tamanho da tela e preencha com a imagem `floor_1`, usando dois `for` (x e y andando de 48 em 48, que é 16 × 3). No loop, desenhe essa Surface no lugar do `tela.fill`.

**Pronto quando:** o mago aparece e anda.

**Cuidado:**
- `convert_alpha` só funciona depois do `set_mode`. Carregue as imagens depois de criar a janela.
- O caminho é relativo à pasta de onde você roda o jogo. Rode sempre com o terminal na pasta do projeto.
- `FileNotFoundError` quer dizer que o nome do arquivo ou a pasta está errado.

## Passo 4: inimigos

**Arquivos:** `inimigos.py` (novo), `config.py`, `main.py`

1. No `config.py`: `INIMIGO_VELOCIDADE = 100` e `INTERVALO_INIMIGO = 1.0` (segundos entre um inimigo e outro).
2. Crie o `inimigos.py`, importando `random`, `pygame`, `config` e o `carregar`:
   - `criar_inimigo()`: sorteie um lado com `random.choice(["cima", "baixo", "esquerda", "direita"])`. Escolha uma posição logo fora da tela nesse lado (use `random.uniform` para o outro eixo). Devolva `carregar("skelet_run_anim_f0").get_frect(center=...)`;
   - `mover_inimigos(inimigos, alvo, dt)`: para cada inimigo da lista:
     - direção = `pygame.Vector2(alvo.center)` − `pygame.Vector2(inimigo.center)`;
     - se o tamanho da direção (`.length()`) for maior que 0, normalize-a (`.normalize()`) e mova: novo centro = centro atual + direção × velocidade × dt;
   - `desenhar_inimigos(tela, inimigos)`: faz o `blit` da imagem em cada inimigo.
3. No `main.py`, antes do `while`: uma lista vazia `inimigos` e um cronômetro `proximo_inimigo` com o valor do intervalo.
4. No `while`: diminua `proximo_inimigo` em `dt`. Quando ficar ≤ 0, faça `append` de um `criar_inimigo()` e volte o cronômetro para o intervalo. Depois mova e desenhe os inimigos.

**Pronto quando:** esqueletos surgem das bordas e perseguem o mago.

**Cuidado:**
- Vector2 é uma "seta" com x e y. Normalizar deixa a seta com tamanho 1, ou seja, só a direção. Por isso depois se multiplica pela velocidade.
- Sem o teste `length() > 0` aparece o erro `ValueError: Can't normalize Vector of length zero`.

## Passo 5: colisão, vida e derrota

**Arquivos:** `telas.py` (novo), `config.py`, `main.py`

1. No `config.py`: `JOGADOR_VIDA = 100`, `DANO_INIMIGO = 10`, `TEMPO_INVULNERAVEL = 1.0` e `FONTE = "assets/fontes/PressStart2P-Regular.ttf"`.
2. **Organize a partida:** no `main.py`, crie a função `nova_partida()`, que devolve um dicionário com tudo que muda durante o jogo: `"jogador"`, `"inimigos"`, `"proximo_inimigo"`, `"vida"` e `"invulneravel"` (começa em 0). Troque as variáveis soltas por `partida["..."]`.
   Para recomeçar o jogo depois, basta chamar `nova_partida()` de novo.
3. **Colisão:** a cada quadro, diminua `invulneravel` em `dt`. Para cada inimigo, se `jogador.colliderect(inimigo)` e `invulneravel <= 0`, a vida perde o dano e `invulneravel` volta para `TEMPO_INVULNERAVEL`.
4. Crie o `telas.py` com a função `escrever(tela, texto, tamanho, cor, centro)`:
   - `pygame.font.Font(config.FONTE, tamanho)` cria a fonte (use um cache em dicionário, como nas imagens);
   - `fonte.render(texto, True, cor)` gera uma imagem do texto;
   - posicione com `get_rect(center=centro)` e faça o `blit`.
5. No `telas.py`, crie `desenhar_hud(tela, partida)`, que escreve `"Vida 70"` no canto de cima.
6. **Estado:** no `main.py`, crie a variável `estado = "jogando"`. Só mova e teste colisões quando `estado == "jogando"`. Quando a vida chegar a 0, `estado = "fim"`. Desenhe sempre, e com `estado == "fim"` escreva `"FIM DE JOGO"` no meio da tela.

**Pronto quando:** encostar num inimigo tira 10 de vida (no máximo 1 vez por segundo), a vida aparece na tela e, quando chega a zero, aparece "FIM DE JOGO".

**Cuidado:**
- Sem o tempo de invulnerabilidade, a vida some num piscar, porque a colisão é testada 60 vezes por segundo.
- Nessa fonte, letra maiúscula com acento fica espremida. Escreva `VITORIA`, e não `VITÓRIA`.

## Passo 6: vitória por tempo

**Arquivos:** `config.py`, `main.py`, `telas.py`

1. No `config.py`: `TEMPO_VITORIA = 90` (segundos).
2. Adicione `"tempo": 0` na `nova_partida()` e some `dt` a ele enquanto estiver jogando.
3. No HUD, mostre o tempo em minutos e segundos (a função `divmod` ajuda).
4. Quando o tempo chegar a `TEMPO_VITORIA`, `estado = "vitoria"`, e a tela mostra `"VITORIA!"`.
5. **(Opcional) Dificuldade:** faça o intervalo entre inimigos diminuir com o tempo, com um valor mínimo.

**Pronto quando:** sobreviver 90 segundos dá vitória.

## Passo 7: menu com os controles (obrigatório)

**Arquivos:** `telas.py`, `main.py`

1. O estado inicial vira `"menu"`.
2. No `telas.py`, crie `desenhar_menu(tela)` com:
   - o nome do jogo;
   - `ENTER - Jogar` e `ESC - Sair`;
   - um quadro de controles com `WASD - Mover`.
3. No `for` de eventos, trate `pygame.KEYDOWN` (tecla apertada) de acordo com o estado:
   - menu + Enter (`pygame.K_RETURN`): `partida = nova_partida()` e `estado = "jogando"`;
   - menu + ESC (`pygame.K_ESCAPE`): sai do jogo;
   - fim ou vitória + Enter: nova partida;
   - fim ou vitória + ESC: volta ao menu.
4. Na tela de fim, escreva `ENTER - Jogar de novo    ESC - Menu`.
5. **(Opcional)** ESC durante o jogo pausa (`estado = "pausa"`), e ESC de novo continua.

**Pronto quando:** dá para ir do menu ao jogo, do jogo ao fim e de lá voltar a jogar ou ao menu.

**Marco:** a Parte 1 está pronta e o jogo já é entregável. Faça o Passo 12 (compilar) uma vez agora, para descobrir cedo algum problema no exe.

---

# Parte 2: tiro

## Passo 8: atirar

**Arquivos:** `tiros.py` (novo), `config.py`, `main.py`, `telas.py`

1. No `config.py`: `TIRO_VELOCIDADE = 500` e `TIRO_RECARGA = 0.25` (segundos entre tiros).
2. Cada tiro precisa de posição e direção, então vai ser um dicionário: `{"rect": ..., "direcao": ...}`.
3. Crie o `tiros.py`:
   - `criar_tiro(origem, mira)`: direção = mira − origem (como Vector2), normalizada (lembre do teste `length() > 0`). O rect é um `pygame.FRect` de 12x12 centralizado na origem;
   - `mover_tiros(tiros, dt)`: move cada tiro na sua direção. Remova da lista os que saíram da tela, ou seja, que não colidem mais com o retângulo da tela;
   - `desenhar_tiros(tela, tiros)`: `pygame.draw.circle` laranja no centro de cada tiro.
4. Na `nova_partida()`, adicione `"tiros": []` e `"recarga": 0`.
5. No `while`, enquanto estiver jogando:
   - diminua a recarga em `dt`;
   - se o botão esquerdo estiver apertado (`pygame.mouse.get_pressed()[0]`) e a recarga ≤ 0, adicione `criar_tiro(centro do jogador, pygame.mouse.get_pos())` e volte a recarga para `TIRO_RECARGA`.
6. No menu, adicione `Mouse - Mirar` e `Clique - Atirar`.

**Pronto quando:** segurar o clique solta tiros na direção do mouse, e eles somem ao sair da tela.

**Cuidado:** remover itens de uma lista enquanto você percorre ela com `for` pula itens. Percorra uma cópia: `for tiro in tiros[:]`.

## Passo 9: matar inimigos

**Arquivos:** `main.py`, `telas.py`

1. Para cada tiro (cópia da lista), percorra cada inimigo (cópia). Se colidirem: remova os dois, some 1 em `partida["abates"]` e dê `break`, porque esse tiro já acabou.
2. No HUD, mostre os abates.
3. Decida como se ganha: manter o tempo, fazer X abates ou algo seu.
4. **(Opcional)** Inimigos diferentes: um mais rápido (`imp_run_anim_f0`), um que aguenta vários tiros (`ogre_run_anim_f0`). Aí cada inimigo vira um dicionário com `"rect"`, `"vida"` e `"velocidade"`.

**Pronto quando:** o tiro mata o inimigo e os abates aparecem na tela.

**Cuidado:** sem o `break`, um tiro que acerta dois inimigos é removido duas vezes e dá `ValueError: list.remove(x): x not in list`.

---

# Parte 3: acabamento

## Passo 10: animação (opcional)

1. Na partida, guarde um `"tempo"`, que você já tem.
2. O quadro da animação é `int(tempo * 8) % 4`: 8 quadros por segundo, voltando ao 0 depois do 3.
3. Monte o nome da imagem com o número do quadro: `wizzard_m_run_anim_f` + quadro quando estiver andando, `wizzard_m_idle_anim_f` + quadro quando estiver parado.
4. Para olhar para a esquerda: `pygame.transform.flip(imagem, True, False)`.

## Passo 11: som e música (opcional)

1. `pygame.mixer.Sound("assets/sons/tiro.wav")` carrega um som (use cache), e `.play()` toca.
2. Toque sons no tiro, no dano, na morte do inimigo, na vitória e na derrota.
3. Música de fundo: `pygame.mixer.music.load("assets/musica/ambiente.wav")` e `pygame.mixer.music.play(-1)`. O -1 repete para sempre.

## Passo 12: compilar (guia do professor)

1. Na pasta do projeto, digite `cmd` na barra de endereço do Explorer.
2. Rode `PyInstaller --onefile main.py`. Com `--noconsole` junto, a janela preta não aparece.
3. Copie a pasta `assets` para dentro de `dist`, ao lado do `main.exe`.
4. Teste com dois cliques no exe. Se der erro, rode o exe pelo CMD para ver a mensagem.

**Pronto quando:** o exe roda a partir de outra pasta. Por exemplo, copie `main.exe` + `assets` para a Área de Trabalho e teste.

## Passo 13: entrega

1. Escreva o `README.md`: nome do jogo, como jogar, controles, créditos (veja `assets/CREDITOS.txt`) e a declaração de uso de IA, conforme a resposta do professor.
2. Zipe o `main.exe` junto com a pasta `assets`.
3. Teste o ZIP: extraia em outra pasta e rode.

## Checklist dos requisitos

- [ ] Jogo 2D em janela (não pode ser no console)
- [ ] Controle do jogador
- [ ] Desafio
- [ ] Vitória
- [ ] Derrota
- [ ] Menu mostrando os comandos
- [ ] Caminhos relativos para os assets
- [ ] ZIP com exe + assets
