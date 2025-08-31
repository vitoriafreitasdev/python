

class NoArvore:
    def __init__(self, teste=None, valor=None, filho_esquerdo=None, filho_direito=None):
        self.teste = teste  # Tupla (atributo, limite) para nós internos
        self.valor = valor  # Valor de classificação para nós folhas
        self.filho_esquerdo = filho_esquerdo  # Subárvore para resposta False
        self.filho_direito = filho_direito  # Subárvore para resposta True

def criar_arvore_diabetes():
    # Nós folhas
    folha_baixo = NoArvore(valor="Baixo risco")
    folha_moderado = NoArvore(valor="Risco moderado")
    folha_alto = NoArvore(valor="Alto risco")
    
    # Nó que testa o IMC
    no_imc = NoArvore(teste=("IMC", 30.0), filho_esquerdo=folha_moderado, filho_direito=folha_alto)
    
    # Raiz que testa o nível de glicose
    raiz = NoArvore(teste=("glicose", 130.0), filho_esquerdo=folha_baixo, filho_direito=no_imc)
    
    return raiz

def pre_ordem(no):
    if no is None:
        return []
    
    # Visita nó, em seguida subárvore esquerda e direita
    resultado = [no.teste or no.valor]
    resultado += pre_ordem(no.filho_esquerdo)
    resultado += pre_ordem(no.filho_direito)
    return resultado

def em_ordem(no):
    if no is None:
        return []
    
    # Visita subárvore esquerda, nó, subárvore direita
    resultado = em_ordem(no.filho_esquerdo)
    resultado.append(no.teste or no.valor)
    resultado += em_ordem(no.filho_direito)
    return resultado

def pos_ordem(no):
    if no is None:
        return []
    
    # Visita subárvore esquerda e direita, depois nó
    resultado = pos_ordem(no.filho_esquerdo)
    resultado += pos_ordem(no.filho_direito)
    resultado.append(no.teste or no.valor)
    return resultado

def classificar_paciente(no, paciente):
    while no.teste is not None:
        atributo, limite = no.teste
        if paciente[atributo] < limite:
            no = no.filho_esquerdo
        else:
            no = no.filho_direito
    return no.valor

def principal():
    arvore = criar_arvore_diabetes()
    
    print("Travessia em pré-ordem:")
    print(pre_ordem(arvore))
    
    print("\nTravessia em-ordem:")
    print(em_ordem(arvore))
    
    print("\nTravessia pós-ordem:")
    print(pos_ordem(arvore))
    
    # Exemplo de classificação de pacientes
    pacientes = [
        {"glicose": 120.0, "IMC": 28.0},
        {"glicose": 140.0, "IMC": 32.5},
        {"glicose": 135.0, "IMC": 25.0}
    ]
    
    for i, paciente in enumerate(pacientes, start=1):
        risco = classificar_paciente(arvore, paciente)
        print(f"\nPaciente {i}: glicose={paciente['glicose']} mg/dL, IMC={paciente['IMC']} -> {risco}")

if __name__ == "__main__":
    principal()