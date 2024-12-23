import flet as ft
from random import randint
import speech_recognition as sr
from time import sleep


# CÓDIGO JOGO####################################################################################################################################

def tabuleiro(linhas, colunas):
    # Cria a matriz do tabuleiro
    return [[0 for _ in range(colunas)] for _ in range(linhas)]

def tabuleiro_visivel(linhas, colunas):
    # Cria a matriz do tabuleiro
    return [["?" for _ in range(colunas)] for _ in range(linhas)]

def adicionar_posicoes_adjacentes(posicoes_jogador, x, y):
    # Adiciona posições adjacentes à lista de posições
    adjacentes = [(x+i, y+j) for i in range(-1, 2) for j in range(-1, 2) if 0 <= x+i < 10 and 0 <= y+j < 10] # a condição garante que os valores gerados estejam dentro do escopo da matriz
    # A lista adjacentes é criada iterando sobre i e j que variam de -1 a 1. Para cada combinação de i e j, a posição (x+i, y+j) é gerada.
    for ax, ay in adjacentes: # ax, ay são usados para iterar sobre cada posição adjacente gerada. ax e ay representam as coordenadas x e y das posições adjacentes.
        posicoes_jogador.append(f'{ax}{ay}') # Cada par (ax, ay) é convertido em uma string e adicionado à lista posicoes_jogador.

def gerar_navio(tabuleiro, posicoes_jogador, tamanho):
    # Gera navios de determinado tamanho
    validacao = 0
    while validacao < 1: # esse while garante que todos os navios foram gerados
        x, y = randint(0, 9), randint(0, 10 - tamanho) # gera a posição inicial do navio garantindo que o y caiba dentro do tabuleiro
        orientacao = randint(0, 1)  # 0 para horizontal, 1 para vertical
        if orientacao == 0:  # horizontal
            x, y = randint(0, 9), randint(0, 10 - tamanho)
            coords = [(x, y+i) for i in range(tamanho)] # essa lista armazena as coordenadas que o navio ocupará (para os navios de mais de uma casa)
        else:  # vertical
            x, y = randint(0, 10 - tamanho), randint(0, 9)
            coords = [(x+i, y) for i in range(tamanho)] # essa lista armazena as coordenadas que o navio ocupará (para os navios de mais de uma casa)

        if all(f'{cx}{cy}' not in posicoes_jogador for cx, cy in coords): # verifica se todas as coordenadas do navio gerado estão livres, com cx e cy sendo as coordenadas específicas de cada parte do navio
            for cx, cy in coords: # as posições sendo válidas o navio é colocado no tabuleiro e as posições adicionadas à lista de posições
                tabuleiro[cx][cy] = tamanho # atribuindo o valor do tamanho do navio à célula específica no tabuleiro representada pelas coordenadas (cx, cy).
                posicoes_jogador.append(f'{cx}{cy}')
            for cx, cy in coords: # adicionando posições adjacentes
                adicionar_posicoes_adjacentes(posicoes_jogador, cx, cy)
            validacao += 1
    return tabuleiro

#DIFICULDADE FÁCIL 
def dif_FACIL_jogador():
    jogador = tabuleiro(10, 10)
    posicoes_jogador = []
    navios_facil = [3, 3, 3, 3, 3, 2, 2, 2, 2, 2]
    for tamanho in navios_facil:
        matriz_jogador = gerar_navio(jogador, posicoes_jogador, tamanho)
    return matriz_jogador

def dif_FACIL_computador():
    computador = tabuleiro(10, 10)
    posicoes_computador = []
    navios_facil = [3, 3, 3, 3, 3, 2, 2, 2, 2, 2]
    for tamanho in navios_facil:
        matriz_computador = gerar_navio(computador, posicoes_computador, tamanho)
    return matriz_computador

#DIFICULDADE MÉDIO
def dif_MEDIO_jogador():
    jogador = tabuleiro(10, 10)
    posicoes_jogador = []
    navios_medio = [4, 3, 3, 2, 2, 2, 1, 1, 1, 1]
    for tamanho in navios_medio:
        matriz_jogador = gerar_navio(jogador, posicoes_jogador, tamanho)
    return matriz_jogador

def dif_MEDIO_computador():
    computador = tabuleiro(10, 10)
    posicoes_computador = []
    navios_medio = [4, 3, 3, 2, 2, 2, 1, 1, 1, 1]
    for tamanho in navios_medio:
        matriz_computador = gerar_navio(computador, posicoes_computador, tamanho)
    return matriz_computador

#DIFICULDADE DIFÍCIL
def dif_DIFICIL_jogador():
    jogador = tabuleiro(10, 10)
    posicoes_jogador = []
    navios_dificil = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    for tamanho in navios_dificil:
        matriz_jogador = gerar_navio(jogador, posicoes_jogador, tamanho)
    return matriz_jogador

def dif_DIFICIL_computador():
    computador = tabuleiro(10, 10)
    posicoes_computador = []
    navios_dificil = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    for tamanho in navios_dificil:
        matriz_computador = gerar_navio(computador, posicoes_computador, tamanho)
    return matriz_computador

#DIFICULDADE KEZIA
def dif_KEZIA_jogador():
    jogador = tabuleiro(10, 10)
    posicoes_jogador = []
    navios_kezia = [4, 3, 3, 2, 2, 2, 1, 1, 1, 1]
    for tamanho in navios_kezia:
        matriz_jogador = gerar_navio(jogador, posicoes_jogador, tamanho)
    return matriz_jogador

def dif_KEZIA_computador():
    # matriz_computador = [[2, 2, '~', 1, '~', '~', '~', '~', 2, '~'], ['~', '~', '~', '~', '~', '~', '~', '~', 2, '~'], ['~', '~', '~', 3, 3, 3, '~', '~', '~', '~'], ['~', 1, '~', '~', '~', '~', '~', '~', 2, 2], ['~', '~', '~', '~', '~', '~', '~', '~', '~', '~'], ['~', '~', '~', '~', '~', '~', '~', '~', '~', '~'], ['~', '~', '~', '~', 4, 4, 4, 4, '~', '~'], [1, '~', 3, '~', '~', '~', '~', '~', '~', '~'], ['~', '~', 3, '~', '~', '~', '~', '~', '~', '~'], ['~', '~', 3, '~', '~', '~', '~', '~', '~', 1]]
    matriz_computador = [[2, 2, 0, 1, 0, 0, 0, 0, 2, 0], [0, 0, 0, 0, 0, 0, 0, 0, 2, 0], [0, 0, 0, 3, 3, 3, 0, 0, 0, 0], [0, 1, 0, 0, 0, 0, 0, 0, 2, 2], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 4, 4, 4, 4, 0, 0], [1, 0, 3, 0, 0, 0, 0, 0, 0, 0], [0, 0, 3, 0, 0, 0, 0, 0, 0, 0], [0, 0, 3, 0, 0, 0, 0, 0, 0, 1]]
    return matriz_computador

#MATRIZ VISÍVEL DO SISTEMA
def gerar_matriz_visivel_pc():
    matriz_visivel_pc = tabuleiro_visivel(10, 10)
    return matriz_visivel_pc


# INTERFACE GRÁFICA##############################################################################################################################
def main(page):

    page.title = "Jogo de Batalha Naval com comando de voz"
    page.window_width = 1900
    page.window_height = 900
    page.update()


    page.theme_mode = ft.ThemeMode.LIGHT
    titulo_jogo = ft.Text(value="BATALHA NAVAL", size=70, weight=ft.FontWeight.W_900, selectable=True, color="#073763")
    page.controls.append(titulo_jogo)
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.add(
        ft.ElevatedButton("Jogar", on_click=lambda e: menu(page), bgcolor="#5aace5", width=500, height=100)
    )

    def menu(page):
        page.clean()
        page.add(
            ft.Text("Escolha a dificuldade: ", size=50),
            ft.ElevatedButton("Fácil", on_click=lambda e: escolher_tabuleiro(page, dif_FACIL_jogador, dif_FACIL_computador), bgcolor="#63da11", width=300, height=50),
            ft.ElevatedButton("Média", on_click=lambda e: escolher_tabuleiro(page, dif_MEDIO_jogador, dif_MEDIO_computador), bgcolor="#ffd966", width=300, height=50),
            ft.ElevatedButton("Difícil", on_click=lambda e: escolher_tabuleiro(page, dif_DIFICIL_jogador, dif_DIFICIL_computador), bgcolor="#f53a3a", width=300, height=50),
            ft.ElevatedButton("Kézia", on_click=lambda e: escolher_tabuleiro(page, dif_KEZIA_jogador, dif_KEZIA_computador), bgcolor="#990000", width=300, height=50)

        )

#para gerar os tabuleiros e mostrar enquanto ainda se escolha o tabuleiro que irá usar para jogar
    def criar_tabuleiro_grid(matriz, dificuldade):
        grid = ft.Column(
            expand=True,
            spacing=5
        )
        grid.controls.append(
            ft.Text("Tabuleiro do jogador", size=65, color="#073763"),
        )
        cabecario_row = ft.Row(spacing=5)
        cabecario_row.controls.append(ft.Container(width=50, height=50))  # Espaço vazio para alinhar com a coluna de números
        for i in range(10):
            cabecario_row.controls.append(
                ft.Container(
                    content=ft.Text(str(i), size=20, color="black"),
                    bgcolor="#0c589e",
                    alignment=ft.alignment.center,
                    border_radius=0,
                    width=50,
                    height=50
                )
            )
        grid.controls.append(cabecario_row)

        linha_index = 0
        for linha in matriz:
            row = ft.Row(
                spacing=5
            )
            # Adiciona a coluna de números ao lado da matriz, de forma que cada linha da matriz seja adicionada de forma alinhadaa co m cada linha da coluna 
            row.controls.append(
                ft.Container(
                    content=ft.Text(str(linha_index), size=20, color="black"),
                    bgcolor="#0c589e",
                    alignment=ft.alignment.center,
                    border_radius=0,
                    width=50,
                    height=50
                )
            )
            linha_index += 1
            for celula in linha:
                def cor_elemento(celula):
                    if celula == 0:
                        return "#60b3ff"
                    elif celula == 1:
                        return "#ff8800"
                    elif celula == 2:
                        return "#38af05"
                    elif celula == 3:
                        return "#f1c232"
                    elif celula == 4:
                        return "#6a329f"
                    elif celula == "?":
                        return "#bcbcbc"
                
                celula_container = ft.Container(
                    content=ft.Text(str(celula), size=20, color="white"),
                    bgcolor=cor_elemento(celula),
                    alignment=ft.alignment.center,
                    border_radius=5,
                    width=50,
                    height=50
                )
                row.controls.append(celula_container)
            grid.controls.append(row)

        botao_reset = ft.ElevatedButton("Resetar tabuleiro", on_click=lambda e: escolher_tabuleiro_jogador(page, dificuldade), bgcolor="#bcbcbc", width=300, height=50)
        botao_jogar = ft.ElevatedButton("Começar jogo", on_click=lambda e: comecar_jogo(page), bgcolor="#8fce00", width=300, height=50)

        botoes_row = ft.Row(
            spacing=10
        )
        botoes_row.controls.append(botao_reset)
        botoes_row.controls.append(botao_jogar)

        grid.controls.append(botoes_row)

        return grid
    
#para mostrar os tabuleiros que irão aparecer no jogo, tanto o do jogador quanto o do computador
    def mostrar_tabuleiros_grid(matriz, cor, titulo):
        grid = ft.Column(
            expand=True,
            spacing=5
        )
        grid.controls.append(
            ft.Text(titulo, size=65, color=cor),
        )
        cabecario_row = ft.Row(spacing=5)
        cabecario_row.controls.append(ft.Container(width=50, height=50))  # Espaço vazio para alinhar com a coluna de números
        for i in range(10):
            cabecario_row.controls.append(
                ft.Container(
                    content=ft.Text(str(i), size=20, color="black"),
                    bgcolor=cor,
                    alignment=ft.alignment.center,
                    border_radius=0,
                    width=50,
                    height=50
                )
            )
        grid.controls.append(cabecario_row)

        linha_index = 0
        for linha in matriz:
            row = ft.Row(
                spacing=5
            )
            # Adiciona a coluna de números ao lado da matriz, de forma que cada linha da matriz seja adicionada de forma alinhadaa co m cada linha da coluna 
            row.controls.append(
                ft.Container(
                    content=ft.Text(str(linha_index), size=20, color="black"),
                    bgcolor=cor,
                    alignment=ft.alignment.center,
                    border_radius=0,
                    width=50,
                    height=50
                )
            )
            linha_index += 1
            for celula in linha:
                def cor_elemento(celula):
                    if celula == 0:
                        return "#60b3ff"
                    elif celula == 1:
                        return "#ff8800"
                    elif celula == 2:
                        return "#38af05"
                    elif celula == 3:
                        return "#f1c232"
                    elif celula == 4:
                        return "#6a329f"
                    elif celula == "?":
                        return "#bcbcbc"
                    elif celula == "X":
                        return "#ff1100"
                    elif celula == "^":
                        return "#ff948c"
                
                celula_container = ft.Container(
                    content=ft.Text(str(celula), size=20, color="white"),
                    bgcolor=cor_elemento(celula),
                    alignment=ft.alignment.center,
                    border_radius=5,
                    width=50,
                    height=50
                )
                row.controls.append(celula_container)
            grid.controls.append(row)

        return grid    
    
    def escolher_tabuleiro_jogador(page, dificuldade):
        page.clean()
        global matriz_tabuleiro
        matriz_tabuleiro = dificuldade()
        grid = criar_tabuleiro_grid(matriz_tabuleiro, dificuldade)
        page.add(grid)
        page.update()

    def escolher_tabuleiro(page, dificuldade_jogador, dificuldade_computador):
        page.clean()
        global matriz_tabuleiro
        matriz_tabuleiro = dificuldade_jogador()
        global matriz_computador
        matriz_computador = dificuldade_computador()
        grid = criar_tabuleiro_grid(matriz_tabuleiro, dificuldade_jogador)
        page.add(grid)
        page.update()    

    def selecionar_matriz():
        matriz_selecionada = matriz_tabuleiro
        return matriz_selecionada            

    def comecar_jogo(page):
        page.clean()
        global matriz_jogador
        matriz_jogador = selecionar_matriz() 
        global matriz_visivel_pc
        matriz_visivel_pc = gerar_matriz_visivel_pc()
        grid1 = mostrar_tabuleiros_grid(matriz_jogador, "#235e94", "Tabuleiro do Jogador")
        global grid2
        grid2 = mostrar_tabuleiros_grid(matriz_visivel_pc, "#c72e2e", "Tabuleiro do PC")
        global row_jogo
        row_jogo = ft.Row(spacing=20)
        row_jogo.controls.append(grid1)
        row_jogo.controls.append(grid2)


        #PARTE FUNCIONAL DO JOGO########################################################################################################################
        recognizer = sr.Recognizer()
        ataque_computador = []
        ataque_jogador = []

        def record_audio():
            with sr.Microphone() as source:
                print("escutando...")
                recognizer.adjust_for_ambient_noise(source)
                audio = recognizer.listen(source)
            return audio
        
        def recognize_speech(record_audio):
            audio = record_audio()
            xy = ""
            try:
                text = recognizer.recognize_google(audio, language='pt-BR')
                print(f"Você disse: {text}")
                for caractere in text:
                    if caractere.isdigit():
                        xy += caractere

            except sr.UnknownValueError:
                print("Não entendido")
            except sr.RequestError:
                print("Sorry, there was an error processing your request.")
            return xy


        def ataque(tabuleiro,x,y,ataque):
            if str(x)+str(y) in ataque:
                print("Já atacou essa posição! perdeu a vez.")
                return False
            else:
                ataque.append(str(x)+str(y))
                if tabuleiro[x][y] != 0 and tabuleiro[x][y] != 'X':
                    tabuleiro[x][y] = 'X'
                    return True
                return False


        def vitoria(tabuleiro): #A função vitoria analisa a matriz para conferir se algum dos elementios é diferente de 0 ou X
            for linha in tabuleiro:
                for elemento in linha:
                    if elemento not in [0, 'X']:  
                        return False
            return True

        def jogar(recognize_speech, record_audio):
            atualizar()
            ganhou = False
            perdeu = False
            turno_jogador = True
            turno_computador = False
            jogar = True
            jogador = matriz_jogador
            while jogar:
                if turno_jogador:
                    print("sua vez de atacar!")
                    sleep(1)
                    atacar = recognize_speech(record_audio)
                    if len(atacar) == 2:
                        x = int(atacar[0])
                        y = int(atacar[1])
                        sleep(1)
                        if ataque(matriz_computador, x, y,ataque_jogador):
                            print("Você acertou um navio!")
                            global matriz_visivel_pc
                            matriz_visivel_pc[x][y] = 'X'
                            atualizar()
                        else:
                            print("Você errou!")
                            if matriz_visivel_pc[x][y] != 'X':
                                matriz_visivel_pc[x][y] = '^'
                                atualizar()
                            turno_jogador = False
                            turno_computador = True
                        sleep(1)
                    else:
                        print("você não disse as coordenadas corretas")
                else:
                    if turno_computador:
                        print("ataque do computador")
                        sleep(2)
                        posicao_do_ataque = computador_repetiu_jogada()
                        while posicao_do_ataque in ataque_computador:
                            posicao_do_ataque = computador_repetiu_jogada()
                        if posicao_do_ataque not in ataque_computador:
                            j = int(posicao_do_ataque[0])
                            k = int(posicao_do_ataque[1])
                            ataque_computador.append(str(j)+str(k))
                            if matriz_jogador[j][k] != 0 and matriz_jogador[j][k] != 'X':
                                matriz_jogador[j][k] = 'X'
                                atualizar()
                                print("o computador acertou o seu navio!!")
                            else:
                                print("o computador errou!!")
                                matriz_jogador[j][k] = '^'
                                atualizar()
                                turno_computador = False
                                turno_jogador = True
                                jogar = False

                if vitoria(matriz_computador):  #Se todos os elementos da matriz_computador forem ou 0 ou X, o JOGADOR ganha
                    print("você ganhou!!")
                    jogar = False
                    ganhou = True
                    ganhou_atualizar()
                if vitoria(matriz_jogador): #Se todo elemento da matriz_jogador for igual a 0 ou X é o COMPUTADOR quem ganha
                    print("você perdeu!!")
                    jogar = False
                    perdeu = True
                    perdeu_atualizar()
            if not ganhou and not perdeu:   
                pode_atacar()

        def computador_repetiu_jogada():
            x = randint(0, 9)
            y = randint(0, 9)
            posicao_ataque = str(x)+str(y)
            return posicao_ataque
        
        def atualizar():
            page.clean()
            matriz_jogador_atualizada = matriz_jogador
            matriz_visivel_pc_atualizada = matriz_visivel_pc
            grid1 = mostrar_tabuleiros_grid(matriz_jogador_atualizada, "#235e94", "Tabuleiro do Jogador")
            grid2 = mostrar_tabuleiros_grid(matriz_visivel_pc_atualizada, "#c72e2e", "Tabuleiro do PC")
            row_jogo = ft.Row(spacing=20)
            row_jogo.controls.append(grid1)
            row_jogo.controls.append(grid2)

            coluna_informacoes = ft.Column(
                expand=True,
                spacing= 5,
            )

            quadro_informacoes = ft.Container(
                content=coluna_informacoes,
                bgcolor="#fff0c5",
                border_radius=5,
                width=500,
                height=800
            )
            row_jogo.controls.append(quadro_informacoes)
            page.add(row_jogo)
            page.update()


        botao_audio=ft.ElevatedButton("Atacar", on_click= lambda e: jogar(recognize_speech, record_audio), width=500, height=50, bgcolor="#ff9300")

        coluna_informacoes = ft.Column(
            expand=True,
            spacing= 5,
        )

        coluna_informacoes.controls.append(botao_audio)

        quadro_informacoes = ft.Container(
            content=coluna_informacoes,
            bgcolor="#fff0c5",
            border_radius=5,
            width=500,
            height=800
        )
        row_jogo.controls.append(quadro_informacoes)
        page.add(row_jogo)

        def ganhou_atualizar():
            page.clean()
            texto_ganhou = ft.Text(value="GANHOU! =)", size=70, weight=ft.FontWeight.W_900, selectable=True, color="#52d11b")
            page.add(texto_ganhou)

        def perdeu_atualizar():
            page.clean()
            texto_perdeu = ft.Text(value="PERDEU! =(", size=70, weight=ft.FontWeight.W_900, selectable=True, color="#ff1919")
            page.add(texto_perdeu)

        def pode_atacar():
            page.clean()
            matriz_jogador_atualizada = matriz_jogador
            matriz_visivel_pc_atualizada = matriz_visivel_pc
            grid1 = mostrar_tabuleiros_grid(matriz_jogador_atualizada, "#235e94", "Tabuleiro do Jogador")
            grid2 = mostrar_tabuleiros_grid(matriz_visivel_pc_atualizada, "#c72e2e", "Tabuleiro do PC")
            row_jogo = ft.Row(spacing=20)
            row_jogo.controls.append(grid1)
            row_jogo.controls.append(grid2)
            botao_audio=ft.ElevatedButton("Atacar", on_click= lambda e: jogar(recognize_speech, record_audio), width=500, height=50, bgcolor="#ff9300")

            coluna_informacoes = ft.Column(
                expand=True,
                spacing= 5,
            )

            coluna_informacoes.controls.append(botao_audio)

            quadro_informacoes = ft.Container(
                content=coluna_informacoes,
                bgcolor="#fff0c5",
                border_radius=5,
                width=500,
                height=800
            )
            row_jogo.controls.append(quadro_informacoes)
            page.add(row_jogo)
            page.update()


ft.app(target=main)