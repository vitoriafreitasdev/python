import hashlib

def calcular_hash(valor):
    """
    Retorna o hash SHA-256 em hexadecimal do texto recebido.
    """
    return hashlib.sha256(valor.encode('utf-8')).hexdigest()

def construir_arvore_merkle(transacoes):
    """
    Constrói a Merkle Tree a partir da lista de transações.
    Retorna a lista de níveis, onde o nível 0 são os hashes das folhas,
    e o último nível contém apenas o Merkle Root.
    """
    niveis = [[calcular_hash(tx) for tx in transacoes]]
    while len(niveis[-1]) > 1:
        nivel_atual = niveis[-1]
        proximo_nivel = []
        for i in range(0, len(nivel_atual), 2):
            esquerda = nivel_atual[i]
            direita = nivel_atual[i+1] if i+1 < len(nivel_atual) else esquerda
            combinado = calcular_hash(esquerda + direita)
            proximo_nivel.append(combinado)
        niveis.append(proximo_nivel)
    return niveis

def obter_raiz_merkle(niveis):
    """
    Retorna o Merkle Root, que é o único elemento do último nível.
    """
    return niveis[-1][0]

def gerar_prova_inclusao(niveis, indice):
    """
    Gera a prova de inclusão para a transação no índice informado.
    Retorna uma lista de tuplas (hash_irmão, lado) desde o nível 0 até um nível
    antes da raiz.
    'lado' é 'esquerda' se o irmão estiver antes, ou 'direita' caso contrário.
    """
    prova = []
    for nivel in niveis[:-1]:
        tamanho = len(nivel)
        if indice % 2 == 0:  # par, irmão é o próximo
            irmao_idx = indice+1 if indice+1 < tamanho else indice
            lado = 'direita'
        else:  # ímpar, irmão é o anterior
            irmao_idx = indice-1
            lado = 'esquerda'
        prova.append((nivel[irmao_idx], lado))
        indice //= 2
    return prova

def verificar_prova_inclusao(hash_tx, prova, raiz_esperada):
    """
    Verifica a prova de inclusão. Recalcula hashes seguindo o caminho da prova
    e compara o resultado final com o Merkle Root esperado.
    """
    hash_atual = hash_tx
    for irmao_hash, lado in prova:
        if lado == 'direita':
            hash_atual = calcular_hash(hash_atual + irmao_hash)
        else:
            hash_atual = calcular_hash(irmao_hash + hash_atual)
    return hash_atual == raiz_esperada

def principal():
    transacoes = [
        "pedido#1001:10 resistores",
        "pedido#1002:5 capacitores",
        "pedido#1003:2 microcontroladores",
        "pedido#1004:20 LEDs",
        "pedido#1005:1 placa-mae"
    ]
    niveis = construir_arvore_merkle(transacoes)
    raiz = obter_raiz_merkle(niveis)
    print(f"Merkle Root: {raiz}\n")
    
    # Escolhe uma transação para gerar e verificar prova
    idx = 2
    hash_alvo = calcular_hash(transacoes[idx])
    prova = gerar_prova_inclusao(niveis, idx)
    valido = verificar_prova_inclusao(hash_alvo, prova, raiz)
    print(f"Prova para transação '{transacoes[idx]}' é válida? {valido}")
    
    # Simula adulteração de uma transação
    transacoes_tampered = transacoes.copy()
    transacoes_tampered[idx] = "pedido#1003:99 microcontroladores"
    niveis_tampered = construir_arvore_merkle(transacoes_tampered)
    raiz_tampered = obter_raiz_merkle(niveis_tampered)
    valido_tampered = verificar_prova_inclusao(hash_alvo, prova, raiz_tampered)
    print(f"Após adulteração, prova continua válida? {valido_tampered}")

if __name__ == "__main__":
    principal()