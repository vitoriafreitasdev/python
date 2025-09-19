VAZIO  = 0
CHEIO  = 1
PAREDE = ' '

TAB_INICIAL = [
    [' ', ' ', 1, 1, 1, ' ', ' '],
    [' ', ' ', 1, 1, 1, ' ', ' '],
    [ 1 ,  1 , 1, 1, 1,  1 ,  1 ],
    [ 1 ,  1 , 1, 0, 1,  1 ,  1 ],
    [ 1 ,  1 , 1, 1, 1,  1 ,  1 ],
    [' ', ' ', 1, 1, 1, ' ', ' '],
    [' ', ' ', 1, 1, 1, ' ', ' '],
]

# ------------------------------------------------------------
# Função para imprimir o tabuleiro
def print_tab(tab):
    for linha in tab:
        print(" ".join(str(x) for x in linha))
    print()

# ------------------------------------------------------------
# Funções principais (backtracking)
def resta_um(tab, sol):
    return resta_umR(tab, sol)

def resta_umR(tab, sol):
    global CHEIO

    if jogo_terminou(tab):
        return True

    for i in range(len(tab)):
        for j in range(len(tab[0])):
            if tab[i][j] == CHEIO:
                encontrou = (
                    tenta_movimento(tab, sol, i, j, i+2, j, i+1, j) or
                    tenta_movimento(tab, sol, i, j, i-2, j, i-1, j) or
                    tenta_movimento(tab, sol, i, j, i, j+2, i, j+1) or
                    tenta_movimento(tab, sol, i, j, i, j-2, i, j-1)
                )
                if encontrou:
                    return True
    return False

def tenta_movimento(tab, sol, xo, yo, xd, yd, xi, yi):
    global CHEIO, VAZIO
    if (xd < 0) or (xd >= len(tab) or (yd < 0) or (yd >= len(tab[0]))):
        return False
    elif (tab[xi][yi] == CHEIO) and (tab[xd][yd] == VAZIO):
        # faz movimento
        tab[xi][yi] = VAZIO
        tab[xo][yo], tab[xd][yd] = tab[xd][yd], tab[xo][yo]

        encontrou = resta_umR(tab, sol)

        if encontrou:
            sol.append([xo, yo, xd, yd])
            return True

        # desfaz movimento
        tab[xi][yi] = CHEIO
        tab[xo][yo], tab[xd][yd] = tab[xd][yd], tab[xo][yo]

    return False

# ------------------------------------------------------------
# Condição de vitória
def jogo_terminou(tab):
    lins, cols = len(tab), len(tab[0])
    count = 0
    pos = None
    for i in range(lins):
        for j in range(cols):
            if tab[i][j] == CHEIO:
                count += 1
                pos = (i, j)
    # Só vence se sobrou 1 peça no centro (3,3)
    return count == 1 and pos == (3, 3)

# ------------------------------------------------------------
# Execução principal
if __name__ == "__main__":
    sol = []
    tab = [linha[:] for linha in TAB_INICIAL]
    possivel = resta_um(tab, sol)

    if possivel:
        print("Solução encontrada!\n")
        tab = [linha[:] for linha in TAB_INICIAL]
        print("Tabuleiro inicial:")
        print_tab(tab)

        for (xo, yo, xd, yd) in sol[::-1]:
            print(f"Movimento: ({xo},{yo}) -> ({xd},{yd})")
            # aplicar jogada no tabuleiro
            xi, yi = ((xo+xd)//2, (yo+yd)//2)
            tab[xi][yi] = VAZIO
            tab[xo][yo], tab[xd][yd] = tab[xd][yd], tab[xo][yo]
            print_tab(tab)

        print("Fim da simulação.")
    else:
        print("Não foi encontrada solução.")
