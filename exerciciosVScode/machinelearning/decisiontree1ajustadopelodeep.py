import pandas as pd
import os
from sklearn.preprocessing import LabelEncoder
from sklearn import tree 
from sklearn.model_selection import train_test_split

# Obter o diretório atual do script
current_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(current_dir, "salaries.csv")

df = pd.read_csv(file_path)
print("Primeiras linhas do dataset:")
print(df.head())
print("\n")

# Preparar features (X) e target (y)
inputs = df.drop('salary_more_then_100k', axis='columns')
target = df['salary_more_then_100k']

print("Inputs originais:")
print(inputs.head())
print("\n")

print("Target:")
print(target.head())
print("\n")

# Transformar strings em números usando LabelEncoder
le_company = LabelEncoder()
le_job = LabelEncoder()
le_degree = LabelEncoder()

inputs['company_n'] = le_company.fit_transform(inputs['company'])
inputs['job_n'] = le_job.fit_transform(inputs['job'])
inputs['degree_n'] = le_degree.fit_transform(inputs['degree'])

print("Inputs após transformação:")
print(inputs.head())
print("\n")

# Pegar apenas as colunas numéricas
inputs_n = inputs.drop(['company', 'job', 'degree'], axis='columns')

print("Inputs finais (apenas números):")
print(inputs_n.head())
print("\n")

# DIVISÃO CORRETA: Separar em dados de treino e teste
X_train, X_test, y_train, y_test = train_test_split(inputs_n, target, test_size=0.2, random_state=42)

print(f"Tamanho do dataset completo: {len(inputs_n)}")
print(f"Tamanho do treino: {len(X_train)}")
print(f"Tamanho do teste: {len(X_test)}")
print("\n")

# Criar e treinar o modelo
model = tree.DecisionTreeClassifier()

# Treinar APENAS com dados de treino
model.fit(X_train, y_train)

# Avaliar a performance com dados de teste (NÃO VISTOS)
train_score = model.score(X_train, y_train)
test_score = model.score(X_test, y_test)

print(f"Acurácia nos dados de TREINO: {train_score:.4f}")
print(f"Acurácia nos dados de TESTE: {test_score:.4f}")
print("\n")

# Fazer previsões
print("Exemplos de previsões:")
print("Input [2, 0, 1]:", model.predict([[2, 0, 1]]))
print("Input [1, 2, 0]:", model.predict([[1, 2, 0]]))

# Mostrar algumas previsões vs valores reais do conjunto de teste
print("\nAlgumas previsões no conjunto de teste:")
print("Valores reais vs Previstos:")
for i in range(min(5, len(X_test))):
    real = y_test.iloc[i]
    pred = model.predict([X_test.iloc[i]])[0]
    print(f"Real: {real}, Previsto: {pred}")

# Opcional: mostrar a importância das features
print("\nImportância das features:")
feature_names = inputs_n.columns
for name, importance in zip(feature_names, model.feature_importances_):
    print(f"{name}: {importance:.4f}")