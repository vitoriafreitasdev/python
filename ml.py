
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
import networkx as nx
import matplotlib.pyplot as plt

# -----------------------------
# 1) Dados fictícios de remédios
# -----------------------------
dados = pd.DataFrame({
    "seguro": [1, 1, 1, 0, 1, 0],
    "efeito_colateral": [0, 1, 2, 2, 1, 2],
    "eficaz": [1, 1, 1, 0, 0, 0],
    "status": ["Passou", "Passou", "Precisa de ajuste", "Nao passou", "Nao passou", "Nao passou"]
})

X = dados[["seguro", "efeito_colateral", "eficaz"]]
y = dados["status"]

# -----------------------------
# 2) Treinando a Árvore de Decisão
# -----------------------------
modelo = DecisionTreeClassifier(max_depth=3, random_state=42)
modelo.fit(X, y)

# -----------------------------
# 3) Novos remédios para prever
# -----------------------------
novos_remedios = pd.DataFrame([
    {"nome": "Remedio_A", "seguro": 1, "efeito_colateral": 0, "eficaz": 1},
    {"nome": "Remedio_B", "seguro": 1, "efeito_colateral": 2, "eficaz": 1},
    {"nome": "Remedio_C", "seguro": 0, "efeito_colateral": 2, "eficaz": 0},
    {"nome": "Remedio_D", "seguro": 1, "efeito_colateral": 1, "eficaz": 0},
])

novos_remedios["status_previsto"] = modelo.predict(novos_remedios[["seguro", "efeito_colateral", "eficaz"]])

print("📊 Previsões:")
print(novos_remedios)

# -----------------------------
# 4) Construindo o Grafo
# -----------------------------
G = nx.Graph()

# Adiciona cada remédio como nó com atributos
for _, row in novos_remedios.iterrows():
    G.add_node(row["nome"], 
               seguro=row["seguro"], 
               efeito_colateral=row["efeito_colateral"], 
               eficaz=row["eficaz"], 
               status=row["status_previsto"])

# Exemplo de relações (apenas ilustrativo)
G.add_edge("Remedio_A", "Remedio_B", relacao="semelhante")
G.add_edge("Remedio_B", "Remedio_C", relacao="mesma_classe")

# -----------------------------
# 5) Consultas
# -----------------------------
# de no em no dentro dos grafos(seus atributos) se o status é passou
passaram = [n for n, d in G.nodes(data=True) if d["status"] == "Passou"]
nao_passaram = [n for n, d in G.nodes(data=True) if d["status"] == "Nao passou"]
ajuste = [n for n, d in G.nodes(data=True) if d["status"] == "Precisa de ajuste"]

print("\n✅ Passaram:", passaram)
print("❌ Nao passaram:", nao_passaram)
print("⚠️ Precisam de ajuste:", ajuste)

# -----------------------------
# 6) Visualizar Grafo
# -----------------------------
cores = []
# descarta o nome pega so os atributos com _,
for _, d in G.nodes(data=True):
    if d["status"] == "Passou":
        cores.append("green")
    elif d["status"] == "Nao passou":
        cores.append("red")
    else:
        cores.append("orange")

nx.draw(G, with_labels=True, node_color=cores, node_size=1500, font_size=10, font_color="white")
plt.show()
