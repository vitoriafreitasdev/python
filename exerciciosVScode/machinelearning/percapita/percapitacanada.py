

import os
import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 
from sklearn import linear_model
import numpy as np 

current_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(current_dir, "./csv/canada_per_capita_income.csv")
file_path_years = os.path.join(current_dir, "./csv/years.csv")

target = pd.read_csv(file_path)
target_years = pd.read_csv(file_path_years)

target = target.rename(columns={'per capita income (US$)': 'per_capita_income'})

reg = linear_model.LinearRegression()
reg.fit(target[['year']], target.per_capita_income)
ano = np.array([[2020]])
resposta = reg.predict(ano)
#print(resposta)
plt.scatter(target.year, target.per_capita_income, color="red", marker=".")
plt.plot(target.year, reg.predict(target[['year']]), color="blue")

#plt.show()

anos = reg.predict(target_years)
target_years['per capita income (US$)'] = anos
print(target_years)

path = os.path.join(current_dir, "per_capita_income.csv")
target_years.to_csv(path, index=False)