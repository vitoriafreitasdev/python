

#------------------------------------------------------------
## CONSTANTES QUE VOCÊ PODE USAR SE QUISER

VAZIO  = 0
CHEIO  = 1
PAREDE = ' '

DEBUG = False

TAB_INICIAL = [
    [' ', ' ', 1, 1, 1, ' ', ' '],
    [' ', ' ', 1, 1, 1, ' ', ' '],
    [ 1 ,  1 , 1, 1, 1,  1 ,  1 ],
    [ 1 ,  1 , 1, 0, 1,  1 ,  1 ],
    [ 1 ,  1 , 1, 1, 1,  1 ,  1 ],
    [' ', ' ', 1, 1, 1, ' ', ' '],
    [' ', ' ', 1, 1, 1, ' ', ' '],
    ]


#------------------------------------------------------------
# FUNÇÃO MAIN

def main():
    '''(None) -> None
    programa para executar o resta um.
    '''
    sol = [] # recebe a sequência de movimentos
    tab = TAB_INICIAL
    print("Tabuleiro Inicial")
    mostre_tabuleiro(tab)
    possivel = resta_um(tab, sol)

    if not possivel:
        print("Impossível")
    else:
        for movimento in sol:
            xo, yo, xd, yd = movimento
            print(f"({xo}, {yo}) -> ({xd}, {yd})")

    print("\nF I M")

#------------------------------------------------------------
# FUNÇÃO -- R E S T A   U M --
# Solução recursiva com backtracking

def resta_um( tab, sol ):
    ''' (tabuleiro, list) -> bool
    Recebe um tabuleiro de resta um e retorna True caso haja solução. Caso contrário retorna False.
    A solução encontrada, caso exista, é carregada na lista sol.
    A solução é uma sequência de movimentos. Um movimento é uma
    tupla do tipo (xo, yo, xd, xy), onde (xo, yo) que representa
    a posição da origem de um pulo e (xd, yd) o destino do pulo.
    Caso não haja solução, a função retorna uma lista vazia.
    '''

    # modifique o restante desse código
    # print("Vixe, ainda não fiz a função recursiva resta_um()")

    memoria = [tab] # cria uma lista para registrar o estado inicial

    tab_buracos = procura_buracos(tab) # verifica onde estão os buracos iniciais e retorna uma lista com as coord. deles

    return resta_umR(tab, sol, memoria, tab_buracos) # chama a recursão

#------------------------------------------------------------
## Escreva aqui outras funções que desejar

def resta_umR(tab, sol, memoria, tab_buracos):
    # mostre_tabuleiro(tab)
    # pause()

    ''' (tabuleiro, list) -> bool
    Resolve o tabuleiro recursivamente e registra os estados que não levaram à solução na lista cache
    para otimização de tempo e utilização do estado inicial do tabuleiro para efeito de comparação na função ta_invertido() '''

    global CHEIO

    if ta_invertido(tab, memoria[0], tab_buracos): # verifica se o tab está invertido em relação ao estado inicial, se estiver, então está resolvido.
      return True

    for i in range (len(tab)):
      for j in range (len(tab[0])):
        if (tab[i][j] == CHEIO): # testa se tem peça nessa posição pra tentar movimentar ela

          # alteracao no i é movimento vertical, alteracao no j é movimento horizontal
          # tenta um movimento em todas as direções
          encontrou = tenta_movimento(tab, memoria, tab_buracos, sol, i, j, i+2, j, i+1, j) or \
                      tenta_movimento(tab, memoria, tab_buracos, sol, i, j, i-2 , j, i-1, j) or \
                      tenta_movimento(tab, memoria, tab_buracos, sol, i, j, i, j+2, i, j+1) or \
                      tenta_movimento(tab, memoria, tab_buracos, sol, i, j, i, j-2, i, j-1)

          if encontrou:
            return True

    return False # se testou todas as possibilidades e mesmo assim não resolveu, então não tem solução.


def tenta_movimento(tab, memoria, tab_buracos, sol, xo, yo, xd, yd, xi, yi): #xi, yi é a posicao intermediária (a peça que vai ser "morta")

  global CHEIO
  global VAZIO

  if (xd < 0) or (xd >= len(tab) or (yd < 0) or (yd >= len(tab[0]))): # testa se o destino está fora do tabuleiro. Se estiver, não é possível se mover.
    return False

  elif (tab[xi][yi] == CHEIO) and (tab[xd][yd] == VAZIO): # testa se é possível se mover e faz o movimento

            #if foi_isolado(tab, xd, yd) and (not [xd,yd] in tab_buracos): # devolve falso se a peça vai ser isolada das outras indevidamente (isto é, se não está no 'buraco').
              #return False # se vai ser isolada, então não tem solução nesse caminho.

            tab[xi][yi] = VAZIO # faz movimento
            tab[xo][yo], tab[xd][yd] = tab[xd][yd], tab[xo][yo]

            encontrou = resta_umR(tab, sol, memoria, tab_buracos) # com o tab alterado, resolve recursivamente

            if encontrou: # se o movimento levou a solucao, inclui ele na lista e retorna que deu certo
              sol.append([xo,yo,xd,yd])
              return True

            tab[xi][yi] = CHEIO # desfaz o movimento se não encontrou
            tab[xo][yo], tab[xd][yd] = tab[xd][yd], tab[xo][yo]


  return False # não é possível se mover

def foi_isolado(tab, xd, yd): # testa se o movimento isolou a peça. Se demonstrou inútil.

  lins, cols = len(tab), len (tab[0])

  soma1 = 0 # conta os 1

  for i in range(xd-1, xd+2): # verifica as posições adjacentes
    for j in range(yd-1, yd+2):
      if ((0 <= i < lins) and (0 <= j < cols)):
        if (tab[i][j] == 1):
          soma1 += 1

  if (soma1 == 1): return True # tá isolado

  else: return False # tem alguém perto


def procura_buracos(tab):

  tab_buracos = []

  for i in range(len(tab)):
    for j in range(len(tab[0])):
      if (tab[i][j] == 0):
        tab_buracos.append([i,j])

  return tab_buracos

def ta_invertido(tab, tab_inicial, tab_buracos): # testa se o tabuleiro foi resolvido

  global PAREDE

  for buraco in tab_buracos: # verifica se tem 1 nos buracos iniciais. Se não tiver, não precisa varrer tudo.
    x, y = buraco
    if (tab[x][y] != 1):
      return False

  for i in range(len(tab)): # se os buracos estão preenchidos, verifica se está tudo invertido.
    for j in range(len(tab[0])):
      if (tab[i][j] != PAREDE):
        if (tab_inicial[i][j] == tab[i][j]): # se achou um igual, então não está invertido e devolve falso
            return False

  return True # se todos foram diferentes, então está tudo invertido e resolveu o problema

#------------------------------------------------------------
# Função pause: use caso desejar

def pause( msg = 'parei aqui' ):
    ''' (str) -> None
    '''
    print(msg)
    input("Tecle Enter para continuar ...")

#------------------------------------------------------------
# Função mostre_tabuleiro(): use caso desejar

def mostre_tabuleiro( tab ):
    ''' (tabuleiro) -> None
    recebe e imprime o tabuleiro em tab
    '''
    nlins = len(tab)
    ncols = len(tab[0])
    # indices
    sep = '     ' + ncols*'---+' + '\n'
    s = '\n      '
    for i in range(ncols):
        s += f' {i}  '
    s += '\n' + sep
    for lin in range(nlins):
        aux = f'{lin} -> |'
        for col in range(ncols):
            aux += f' {tab[lin][col]} |'
        s += aux + '\n' + sep

    print(s)


#------------------------------------------------------------
# chama a função main

if __name__ == '__main__':
    main()