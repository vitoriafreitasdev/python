import pandas as pd
import os
from sklearn.preprocessing import LabelEncoder
from sklearn import tree
from sklearn.model_selection import train_test_split

# Caminho do arquivo
current_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(current_dir, "titanic.csv")

# Carregar os dados
df = pd.read_csv(file_path)

# Separar inputs e target
inputs = df.drop(['PassengerId', 'Survived', 'Name', 'SibSp', 'Parch', 'Ticket', 'Cabin', 'Embarked'], axis='columns')
target = df['Survived']

# Encoders
le_pclass = LabelEncoder()
le_sex = LabelEncoder()

# Age e Fare são numéricos → não precisam de LabelEncoder, só tratar NaN
inputs['Pclass_n'] = le_pclass.fit_transform(inputs['Pclass'])
inputs['Sex_n'] = le_sex.fit_transform(inputs['Sex'])
inputs['Age'] = inputs['Age'].fillna(inputs['Age'].mean())   # substitui NaN pela média
inputs['Fare'] = inputs['Fare'].fillna(inputs['Fare'].mean())

# Agora só ficamos com as colunas numéricas
inputs_n = inputs[['Pclass_n', 'Sex_n', 'Age', 'Fare']]

# Separar treino e teste (80/20)
X_train, X_test, y_train, y_test = train_test_split(inputs_n, target, test_size=0.2, random_state=42)

# Criar e treinar modelo
model = tree.DecisionTreeClassifier()
model.fit(X_train, y_train)

# Avaliar
print("Acurácia no treino:", model.score(X_train, y_train))
print("Acurácia no teste :", model.score(X_test, y_test))

# Fazer uma previsão
print(model.predict([[2, 1, 28, 18]]))
