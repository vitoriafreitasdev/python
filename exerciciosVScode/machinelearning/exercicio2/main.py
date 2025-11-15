import os
import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt
from sklearn import linear_model
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error

diretorio_atual = os.path.dirname(os.path.abspath(__file__))
caminho1 = os.path.join(diretorio_atual, "./csv/experience.csv")
caminho2 = os.path.join(diretorio_atual, "./csv/new.csv")
df = pd.read_csv(caminho1)
d = pd.read_csv(caminho2)

X_train, X_test, y_train, y_test = train_test_split(df[['experience']], df['salary'], test_size=0.2, random_state=42)

reg = linear_model.LinearRegression()
reg.fit(X_train, y_train)

train_score = reg.score(X_train, y_train)
test_score = reg.score(X_test, y_test)

print(f"Treino: {train_score:.4f}")
print(f"Teste: {test_score:.4f}")


predicts = reg.predict(d)
for i in range(len(predicts)):
    d['salary'] = f"{predicts[i]:.2f}"


print(d)

output_path = os.path.join(diretorio_atual, "./csv/prediction.csv")
d.to_csv(output_path, index=False)