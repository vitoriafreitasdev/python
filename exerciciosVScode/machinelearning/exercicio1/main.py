
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

target = transformacao.fit_transform(df['especie'])

# print("Inputs")
# print(inputs)
# print("Target")
# print(target)

X_train, X_test, y_train, y_test = train_test_split(inputs, target, test_size=0.2, random_state=42)

model = tree.DecisionTreeClassifier()
model.fit(X_train, y_train)

train_score = model.score(X_train, y_train)
test_score = model.score(X_test, y_test)

print(f"train score: {train_score:.4f}")
print(f"test score: {test_score:.4f}")

comprimento_sepala  = float(input("Coloque o comprimento da sepala: "))
largura_sepala  = float(input("Coloque a largura da sepala: "))
comprimento_petala  = float(input("Coloque o comprimento da petala: "))
largura_petala  = float(input("Coloque a largura da petala: "))

predict = model.predict([[comprimento_sepala, largura_sepala, comprimento_petala, largura_petala]])



if(predict == [0]):
    print("Modelo: setosa.")
elif(predict == [1]):
    print("Modelo: versicolor.")
elif(predict == [2]):
    print("Modelo: virginica.")
else: 
    print("Nenhum modelo encontrado.")