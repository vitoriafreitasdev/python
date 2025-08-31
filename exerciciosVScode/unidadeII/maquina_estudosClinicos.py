
# Versão simplificada para entender o conceito
class ArvoreDecisaoML:
    def __init__(self):
        self.regras_aprendidas = []
        
    def aprender(self, dados, resultados):
        """Simula o aprendizado de regras baseado nos dados históricos"""
        print("⏳ Aprendendo regras a partir dos dados...")
        
        # Análise dos dados para aprender padrões
        # (Em ML real, isso seria feito por algoritmos como ID3, C4.5, etc.)
        
        # Regra 1: Medicamentos seguros, sem efeitos colaterais e eficazes
        if any(d[0] == 1 and d[1] == 0 and d[2] == 1 and r == "ALTA" 
               for d, r in zip(dados, resultados)):
            self.regras_aprendidas.append(("seguro == 1 and efeito_colateral == 0 and eficaz == 1", "ALTA"))
        
        # Regra 2: Medicamentos seguros, com efeitos suportáveis e eficazes
        if any(d[0] == 1 and d[1] == 1 and d[2] == 1 and r == "MEDIA" 
               for d, r in zip(dados, resultados)):
            self.regras_aprendidas.append(("seguro == 1 and efeito_colateral == 1 and eficaz == 1", "MEDIA"))
        
        # Regra 3: Medicamentos seguros, com efeitos altos mas eficazes
        if any(d[0] == 1 and d[1] == 2 and d[2] == 1 and r == "BAIXA" 
               for d, r in zip(dados, resultados)):
            self.regras_aprendidas.append(("seguro == 1 and efeito_colateral == 2 and eficaz == 1", "BAIXA"))
        
        # Regra 4: Medicamentos não seguros ou não eficazes
        if any((d[0] == 0 or d[2] == 0) and r == "REJEITADO" 
               for d, r in zip(dados, resultados)):
            self.regras_aprendidas.append(("seguro == 0 or eficaz == 0", "REJEITADO"))
        
        print("✅ Regras aprendidas com sucesso!")
        self.mostrar_regras()
    
    def mostrar_regras(self):
        """Mostra as regras que o modelo aprendeu"""
        print("\n📋 REGRAS APRENDIDAS:")
        for i, (condicao, resultado) in enumerate(self.regras_aprendidas, 1):
            print(f"{i}. SE {condicao} ENTÃO {resultado}")
    
    def prever(self, seguro, efeito_colateral, eficaz):
        """Faz previsão baseada nas regras aprendidas"""
        print(f"\n🔍 Analisando medicamento: seguro={seguro}, efeito={efeito_colateral}, eficaz={eficaz}")
        
        for condicao, resultado in self.regras_aprendidas:
            if eval(condicao):
                print(f"   ✅ Regra aplicada: {condicao}")
                return resultado
        
        return "INDETERMINADO"
    
    def avaliar_desempenho(self, dados_teste, resultados_teste):
        """Avalia o desempenho do modelo com dados de teste"""
        print("\n📊 AVALIANDO DESEMPENHO DO MODELO:")
        
        acertos = 0
        total = len(dados_teste)
        
        for i, (dado, resultado_real) in enumerate(zip(dados_teste, resultados_teste), 1):
            seguro, efeito, eficaz = dado
            previsao = self.prever(seguro, efeito, eficaz)
            
            if previsao == resultado_real:
                acertos += 1
                print(f"   ✅ Caso {i}: CORRETO (previsto: {previsao}, real: {resultado_real})")
            else:
                print(f"   ❌ Caso {i}: ERRADO (previsto: {previsao}, real: {resultado_real})")
        
        accuracy = acertos / total
        print(f"\n🎯 Accuracy: {accuracy:.2f} ({acertos}/{total} acertos)")
        return accuracy

# Dados de treinamento (histórico de estudos clínicos)
dados_treinamento = [
    # [seguro, efeito_colateral, eficaz]
    # efeito_colateral: 0 = nenhum, 1 = suportável, 2 = alto
    [1, 0, 1],  # seguro, sem efeito, eficaz
    [1, 1, 1],  # seguro, efeito suportável, eficaz
    [1, 2, 1],  # seguro, efeito alto, eficaz
    [0, 2, 0],  # não seguro, efeito alto, não eficaz
    [1, 0, 1],  # seguro, sem efeito, eficaz
    [1, 1, 0],  # seguro, efeito suportável, não eficaz
    [0, 2, 1],  # não seguro, efeito alto, eficaz
    [1, 1, 1],  # seguro, efeito suportável, eficaz
    [1, 2, 0],  # seguro, efeito alto, não eficaz
    [1, 0, 1]   # seguro, sem efeito, eficaz
]

resultados_treinamento = [
    "ALTA",      # caso 1
    "MEDIA",     # caso 2
    "BAIXA",     # caso 3
    "REJEITADO", # caso 4
    "ALTA",      # caso 5
    "REJEITADO", # caso 6
    "REJEITADO", # caso 7
    "MEDIA",     # caso 8
    "REJEITADO", # caso 9
    "ALTA"       # caso 10
]

# Dados de teste (novos casos para avaliar o modelo)
dados_teste = [
    [1, 0, 1],  # Deve prever ALTA
    [1, 2, 1],  # Deve prever BAIXA
    [0, 1, 0],  # Deve prever REJEITADO
    [1, 1, 1]   # Deve prever MEDIA
]

resultados_teste = [
    "ALTA",      # resultado esperado 1
    "BAIXA",     # resultado esperado 2
    "REJEITADO", # resultado esperado 3
    "MEDIA"      # resultado esperado 4
]

# Criar e treinar o modelo
print("🧠 SISTEMA DE APRENDIZADO DE MÁQUINA PARA ESTUDOS CLÍNICOS")
print("=" * 60)

modelo = ArvoreDecisaoML()

# Fase de treinamento (aprendizado)
print("\n🎯 FASE DE TREINAMENTO:")
modelo.aprender(dados_treinamento, resultados_treinamento)

# Fase de teste (avaliação)
print("\n🧪 FASE DE TESTE:")
modelo.avaliar_desempenho(dados_teste, resultados_teste)

# Fase de previsão (uso real)
print("\n🔮 FASE DE PREVISÃO - NOVOS MEDICAMENTOS:")
novos_medicamentos = [
    (1, 0, 1, "Medicamento A - Esperado: ALTA"),
    (1, 2, 1, "Medicamento B - Esperado: BAIXA"),
    (0, 1, 1, "Medicamento C - Esperado: REJEITADO"),
    (1, 1, 1, "Medicamento D - Esperado: MEDIA"),
    (1, 0, 0, "Medicamento E - Esperado: REJEITADO")
]

for seguro, efeito, eficaz, descricao in novos_medicamentos:
    resultado = modelo.prever(seguro, efeito, eficaz)
    print(f"   {descricao}")
    print(f"   📍 Resultado previsto: {resultado}")
    print()

# Mostrar árvore de decisão visual
print("\n🌳 ÁRVORE DE DECISÃO APRENDIDA:")
print("""
            [seguro == 1?]
           /             \\
          SIM             NÃO → REJEITADO
          /               \\
   [efeito_colateral]   [eficaz == 1?]
     /      |     \\           \\
    0       1      2           NÃO → REJEITADO
    |       |      |           \\
 ALTA   [eficaz == 1?]   [eficaz == 1?]
           /             \\
         SIM             NÃO → REJEITADO
         /               \\
      MEDIA            REJEITADO
""")