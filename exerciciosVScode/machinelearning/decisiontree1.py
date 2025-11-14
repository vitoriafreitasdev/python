

import pandas as pd
import os
from sklearn.preprocessing import LabelEncoder
from sklearn import tree 

#ML so entende numero, nao entendi letras

# Obter o diretório atual do script
current_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(current_dir, "salaries.csv")

df = pd.read_csv(file_path)
df.head()

inputs = df.drop('salary_more_then_100k', axis='columns')

target = df['salary_more_then_100k']

# esse aqui serve para transformar o que era string em numeros
le_company = LabelEncoder()
le_job = LabelEncoder()
le_degree = LabelEncoder()

inputs['company_n'] = le_company.fit_transform(inputs['company'])
inputs['job_n'] = le_job.fit_transform(inputs['job'])
inputs['degree_n'] = le_degree.fit_transform(inputs['degree'])
#para pegar os valores apenas com numeros
inputs_n = inputs.drop(['company', 'job', 'degree'], axis='columns')


model = tree.DecisionTreeClassifier()
# treina a maquina
model.fit(inputs_n,target)
# porcentagem de acerto de 0 a 1
model.score(inputs_n, target)

print(model.predict([[2, 0, 1]]))


company = "google"
job = "computer programmer"
degree = "masters"
#0
if company == "google" and job == "sales executive" and degree == "bachelors":
    n1, n2, n3 = 0, 2, 0
#1
if company == "google" and job == "sales executive" and degree == "masters":
    n1, n2, n3 = 0, 2, 1
#2
if company == "google" and job == "business manager" and degree == "bachelors":
    n1, n2, n3 = 0, 0, 0
#3
if company == "google" and job == "business manager" and degree == "masters":
    n1, n2, n3 = 0, 0, 1
#4
if company == "google" and job == "computer programmer" and degree == "bachelors":
    n1, n2, n3 = 0, 1, 0
#5
if company == "google" and job == "computer programmer" and degree == "masters":
    n1, n2, n3 = 0, 1, 1

results = model.predict([[n1, n2, n3]])
if results == 1:
    print("Ganha mais de 100k")
else:
    print("Não ganha")
