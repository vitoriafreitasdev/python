import pandas as pd
import os 
from sklearn.preprocessing import LabelEncoder
from sklearn import tree 
from sklearn.model_selection import train_test_split

diretorio_atual = os.path.dirname(os.path.abspath(__file__))
arquivo_caminho = os.path.join(diretorio_atual, "./csv/flores.csv")

df = pd.read_csv(arquivo_caminho)

inputs = df.drop("especie", axis="columns")
#verificar se p target esta feito da maneira correta
transformacao = LabelEncoder()
#target = df['especie']
target = transformacao.fit_transform(df['especie'])
print("Inputs")
print(inputs)
print("Target")
print(target)

