
import os
import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 
from sklearn import linear_model
import numpy as np 

current_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(current_dir, "./csv/homeprices.csv")
df = pd.read_csv(file_path)

# Criar o scatter plot
plt.scatter(df.area, df.price, color='red', marker='+')
plt.title('Preço vs Área')
plt.xlabel('Área (sq ft)')
plt.ylabel('Preço (US$)')
plt.grid(True)

# MOSTRAR O GRÁFICO - Esta linha é essencial!
#plt.show()

reg = linear_model.LinearRegression()
reg.fit(df[['area']], df.price)
area_pred = np.array([[5090]])
preco_predito = reg.predict(area_pred)
print(reg.coef_)
print(reg.intercept_)
print(preco_predito)
# 135 é o valor que da se fazemos reg.coef => o coeficiente, 180 é valor do intercept que da se fazer reg.intercept_, ele pega esses dados do csv, 3300 é valor da area
#formula => y = m*x+b
# calc = 135.78767123*5090+180616.43835616432
# print(calc)