
import pandas as pd
import os
current_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(current_dir, "titanic.csv")

df = pd.read_csv(file_path)
df.head()

df.drop(['PassengerId','Name','SibSp','Parch','Ticket','Cabin','Embarked'],axis='columns',inplace=True)
df.head()

inputs = df.drop('Survived',axis='columns')
target = df.Survived

inputs.Sex = inputs.Sex.map({'male': 1, 'female': 2})
inputs.Age[:10]
inputs.Age = inputs.Age.fillna(inputs.Age.mean())
inputs.head()

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(inputs,target,test_size=0.2)
len(X_train)
len(X_test)

from sklearn import tree
model = tree.DecisionTreeClassifier()
model.fit(X_train,y_train)
print(model.score(X_test,y_test))
print(model.predict([[2, 1, 28, 18]]))