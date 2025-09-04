class No:
    def __init__(self, valor):
        self.valor = valor
        self.esquerda = None
        self.direita = None
        self.altura = 1

class ArvoreAVL:
    def __init__(self):
        self.raiz = None
    
    def altura(self, no):
        return no.altura if no else 0
    
    def balanceamento(self, no):
        return self.altura(no.esquerda) - self.altura(no.direita) if no else 0
    
    def rotacao_esquerda(self, z):
        y = z.direita
        T2 = y.esquerda
        
        y.esquerda = z
        z.direita = T2
        # max pega o maior entre os valores
        z.altura = 1 + max(self.altura(z.esquerda), self.altura(z.direita))
        y.altura = 1 + max(self.altura(y.esquerda), self.altura(y.direita))
        
        return y
    
    def rotacao_direita(self, z):
        y = z.esquerda
        T3 = y.direita
        
        y.direita = z
        z.esquerda = T3
        
        z.altura = 1 + max(self.altura(z.esquerda), self.altura(z.direita))
        y.altura = 1 + max(self.altura(y.esquerda), self.altura(y.direita))
        
        return y
    
    def inserir(self, no, valor):
        if not no:
            return No(valor)
        
        if valor < no.valor:
            no.esquerda = self.inserir(no.esquerda, valor)
        else:
            no.direita = self.inserir(no.direita, valor)
        
        no.altura = 1 + max(self.altura(no.esquerda), self.altura(no.direita))
        
        balance = self.balanceamento(no)
        
        # CASO 1: Pesado à esquerda com inserção à esquerda-esquerda
        if balance > 1 and valor < no.esquerda.valor:
            return self.rotacao_direita(no) # ✅ Simples à direita
        # CASO 2: Pesado à direita com inserção à direita-direita  
        if balance < -1 and valor > no.direita.valor:
            return self.rotacao_esquerda(no) # ✅ Simples à esquerda
        # CASO 3: Pesado à esquerda com inserção à esquerda-direita
        if balance > 1 and valor > no.esquerda.valor:
            no.esquerda = self.rotacao_esquerda(no.esquerda) # ✅ Primeiro esquerda no filho
            return self.rotacao_direita(no) # ✅ Depois direita no pai
        # CASO 4: Pesado à direita com inserção à direita-esquerda
        if balance < -1 and valor < no.direita.valor:
            no.direita = self.rotacao_direita(no.direita) # ✅ Primeiro direita no filho
            return self.rotacao_esquerda(no) # ✅ Depois esquerda no pai
        """
            CASO 1: 
            Pai → Filho Esquerdo → Neto Esquerdo
            → Rotação simples direita

            CASO 2:
            Pai → Filho Direito → Neto Direito  
            → Rotação simples esquerda

            CASO 3:
            Pai → Filho Esquerdo → Neto Direito
            → Primeiro arruma filho, depois arruma pai

            CASO 4:
            Pai → Filho Direito → Neto Esquerdo
            → Primeiro arruma filho, depois arruma pai
        """
    def inserir_valor(self, valor):
        self.raiz = self.inserir(self.raiz, valor)
    
    def em_ordem(self, no):
        if no:
            self.em_ordem(no.esquerda)
            print(no.valor, end=" ")
            self.em_ordem(no.direita)

# Exemplo de uso
arvore = ArvoreAVL()

# Inserindo valores em ordem (que causaria problema em árvore normal)
valores = [10, 20, 30, 40, 50, 25]

print("Inserindo valores:", valores)
for valor in valores:
    arvore.inserir_valor(valor)

print("Árvore em ordem (balanceada):")
arvore.em_ordem(arvore.raiz)
print("\nAltura da árvore:", arvore.altura(arvore.raiz))