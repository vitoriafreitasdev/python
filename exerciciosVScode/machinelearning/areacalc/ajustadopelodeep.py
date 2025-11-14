import os
import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 
from sklearn import linear_model
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, r2_score

current_dir = os.path.dirname(os.path.abspath(__file__))
file_path_home_price = os.path.join(current_dir, "./csv/homeprices.csv")
file_path_area = os.path.join(current_dir, "./csv/areas.csv")

df = pd.read_csv(file_path_home_price)
d = pd.read_csv(file_path_area)

print("Dataset original:")
print(df.head())
print(f"Tamanho do dataset: {len(df)}")
print("\n")

# DIVISÃO EM TREINO E TESTE
X = df[['area']]  # Features
y = df['price']    # Target

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

print(f"Tamanho do treino: {len(X_train)}")
print(f"Tamanho do teste: {len(X_test)}")
print("\n")

# Criar e treinar o modelo
reg = linear_model.LinearRegression()
reg.fit(X_train, y_train)  # Treinar APENAS com dados de treino

# Avaliar o modelo
train_score = reg.score(X_train, y_train)
test_score = reg.score(X_test, y_test)

print(f"R² Score no Treino: {train_score:.4f}")
print(f"R² Score no Teste: {test_score:.4f}")
print(f"Coeficiente: {reg.coef_[0]:.2f}")
print(f"Intercept: {reg.intercept_:.2f}")
print("\n")

# Fazer previsões no conjunto de teste para métricas
y_pred = reg.predict(X_test)
mae = mean_absolute_error(y_test, y_pred)
print(f"Erro Médio Absoluto (MAE): ${mae:.2f}")

# Prever um novo valor
area_pred = np.array([[5090]])
preco_predito = reg.predict(area_pred)
print(f"Preço previsto para 5090 sq ft: ${preco_predito[0]:.2f}")

# Criar o scatter plot
plt.figure(figsize=(12, 5))

plt.subplot(1, 2, 1)
plt.title('Preço vs Área - Treino e Teste')
plt.xlabel('Área (sq ft)')
plt.ylabel('Preço (US$)')
# Plotar pontos de treino
plt.scatter(X_train, y_train, color='red', marker='+', label='Dados Treino')
# Plotar pontos de teste
plt.scatter(X_test, y_test, color='green', marker='o', label='Dados Teste')
# Plotar linha de regressão
x_line = np.linspace(df.area.min(), df.area.max(), 100).reshape(-1, 1)
plt.plot(x_line, reg.predict(x_line), color="blue", label='Linha Regressão')
plt.legend()
plt.grid(True)

plt.subplot(1, 2, 2)
# Prever para o arquivo areas.csv
p = reg.predict(d)
d['prices'] = p

plt.title('Previsões para Novas Áreas')
plt.xlabel('Área (sq ft)')
plt.ylabel('Preço Previsto (US$)')
plt.scatter(d['area'], d['prices'], color='purple', marker='s')
plt.grid(True)

plt.tight_layout()
#plt.show()

print("\nPrevisões para areas.csv:")
print(d)