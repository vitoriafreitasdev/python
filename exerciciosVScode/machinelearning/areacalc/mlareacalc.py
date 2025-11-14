
import os
import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 
from sklearn import linear_model
import numpy as np 

current_dir = os.path.dirname(os.path.abspath(__file__))
file_path_home_price = os.path.join(current_dir, "./csv/homeprices.csv")
file_path_area = os.path.join(current_dir, "./csv/areas.csv")
df = pd.read_csv(file_path_home_price)
d = pd.read_csv(file_path_area)



reg = linear_model.LinearRegression()
reg.fit(df[['area']], df.price)
area_pred = np.array([[5090]])
preco_predito = reg.predict(area_pred)
# print(reg.coef_)
# print(reg.intercept_)
print(preco_predito)

# Criar o scatter plot
plt.title('Preço vs Área')
plt.xlabel('Área (sq ft)')
plt.ylabel('Preço (US$)')
plt.scatter(df.area, df.price, color='red', marker='+')
plt.plot(df.area, reg.predict(df[['area']]), color="blue", marker="+")
plt.grid(True)

#plt.show()

# 135 é o valor que da se fazemos reg.coef => o coeficiente, 180 é valor do intercept que da se fazer reg.intercept_, ele pega esses dados do csv, 3300 é valor da area
#formula => y = m*x+b
# calc = 135.78767123*5090+180616.43835616432
# print(calc)

p = reg.predict(d)
d['prices'] = p 
print("Testes")
print(d)
# output_path = os.path.join(current_dir, "prediction.csv")
# d.to_csv(output_path, index=False)