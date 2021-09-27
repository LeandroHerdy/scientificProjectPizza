import matplotlib.pyplot as plt
import numpy as np

from sklearn.linear_model import LinearRegression


# Diametros = (cm)
Diametros = [[7], [10], [15], [30], [45]]

# Preço (R$)
Precos = [[8], [11], [16], [38.5], [52]]


# Visualização dos dados
plt.figure()
plt.xlabel('Diâmetro(cm)')
plt.ylabel('Preço (R$)')
plt.title('Diâmetro X Preço')
plt.plot(Diametros, Precos, 'k.')
plt.axis([0, 60, 0, 60])
plt.grid(True)
plt.show()


x = [[7], [10], [15], [30], [45]]

y = [[8], [11], [16], [38.5], [52]]

modelo = LinearRegression()

type(modelo)

modelo.fit(x, y)

# print("Uma pizza de 20 cm de diâmetro deve custar: R$ {.2f}".format(modelo.predict([20], [0])))

plt.scatter(x, y, color='black')
plt.plot(x, modelo.predict(x), color='blue', linewidth=3)
plt.xlabel('x')
plt.ylabel('y')
plt.xticks(())
plt.yticks(())
plt.show()
