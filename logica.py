from random import randint
from time import sleep

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
        
        

            

def computador_repetiu_jogada():
            x = randint(0, 9)
            y = randint(0, 9)
            posicao_ataque = str(x)+str(y)
            return posicao_ataque