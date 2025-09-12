

import pandas as pd
import os
from sklearn.preprocessing import LabelEncoder
from sklearn import tree 

current_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(current_dir, "titanic.csv")

df = pd.read_csv(file_path)
df.head()

inputs = df.drop(['PassengerId', 'Survived', 'Name', 'SibSp', 'Parch', 'Ticket', 'Cabin', 'Embarked'], axis='columns')
target = df['Survived']

#PassengerId,Survived,Pclass,Name,Sex,Age,SibSp,Parch,Ticket,Fare,Cabin,Embarked

le_pclass = LabelEncoder()
le_sex = LabelEncoder()
le_age = LabelEncoder()
le_fare = LabelEncoder()

inputs['Pclass_n'] = le_pclass.fit_transform(inputs['Pclass'])
inputs['Sex_n'] = le_sex.fit_transform(inputs['Sex'])
inputs['Age_n'] = le_age.fit_transform(inputs['Age'])
inputs['Fare_n'] = le_fare.fit_transform(inputs['Fare'])

inputs_n = inputs.drop(['Pclass', 'Sex', 'Age', 'Fare'], axis='columns')
print(df)
print(inputs_n)

model = tree.DecisionTreeClassifier()
model.fit(inputs_n, target)
print(model.score(inputs_n, target))
print(model.predict([[2, 1, 28, 18]]))