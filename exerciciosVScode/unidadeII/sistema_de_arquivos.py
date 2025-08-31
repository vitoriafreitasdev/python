class NoArquivo:
    def __init__(self, nome, tipo):
        self.nome = nome  # Nome do diretório ou arquivo
        self.tipo = tipo  # "diretorio" ou "arquivo"
        self.filhos = []  # Lista de nós filhos
    
    def adicionar_filho(self, filho):
        self.filhos.append(filho)
        return self

def construir_arvore(caminhos):
    raiz = NoArquivo("root", "diretorio")
    for caminho in caminhos:
        partes = caminho.strip("/").split("/")
        atual = raiz
        for parte in partes:
            # verifica se já existe um nó com esse nome
            encontrado = next((n for n in atual.filhos if n.nome == parte), None)
            if not encontrado:
                tipo = "diretorio" if parte.find(".") < 0 else "arquivo"
                encontrado = NoArquivo(parte, tipo)
                atual.adicionar_filho(encontrado)
            atual = encontrado
    return raiz

def pre_ordem(no, resultado=None):
    if resultado is None:
        resultado = []
    resultado.append(f"{no.tipo}:{no.nome}")
    for filho in no.filhos:
        pre_ordem(filho, resultado)
    return resultado

def em_ordem(no, resultado=None):
    if resultado is None:
        resultado = []
    m = len(no.filhos) // 2
    for filho in no.filhos[:m]: # pega do inicio ate m-1
        em_ordem(filho, resultado)
    resultado.append(f"{no.tipo}:{no.nome}")
    for filho in no.filhos[m:]: # do m ate o final
        em_ordem(filho, resultado)
    return resultado

def pos_ordem(no, resultado=None):
    if resultado is None:
        resultado = []
    for filho in no.filhos:
        pos_ordem(filho, resultado)
    resultado.append(f"{no.tipo}:{no.nome}")
    return resultado

def buscar_arquivo(no, nome_alvo, caminho=None):
    if caminho is None:
        caminho = []
    caminho_atual = caminho + [no.nome]
    if no.tipo == "arquivo" and no.nome == nome_alvo:
        return "/".join(caminho_atual)
    for filho in no.filhos:
        achado = buscar_arquivo(filho, nome_alvo, caminho_atual)
        if achado:
            return achado
    return None

def principal():
    caminhos = [
        "docs/manual.pdf",
        "docs/guia/instalacao.txt",
        "imagens/logo.png",
        "imagens/festas/ano_novo.jpg",
        "backup/2025/janeiro/data.bak"
    ]
    arvore = construir_arvore(caminhos)
    
    print("Travessia pré-ordem:")
    print(pre_ordem(arvore))
    
    print("\nTravessia em-ordem:")
    print(em_ordem(arvore))
    
    print("\nTravessia pós-ordem:")
    print(pos_ordem(arvore))
    
    arquivo_busca = "data.bak"
    caminho_encontrado = buscar_arquivo(arvore, arquivo_busca)
    print(f"\nCaminho do arquivo '{arquivo_busca}': {caminho_encontrado}")

if __name__ == "__main__":
    principal()