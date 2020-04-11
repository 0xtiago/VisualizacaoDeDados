import matplotlib.pyplot as plt

input_values = [1,2,3,4,5]
squares = [1, 4, 9, 16, 25]
plt.plot(input_values, squares, linewidth=5)

#Define o titulo do grafico e nomeia os eixos
plt.title("Raiz Quadrada", fontsize=24)
plt.xlabel("Valor", fontsize=14)
plt.ylabel("Raiz quadrada do Valor", fontsize=14)

#Define o tamanho dos rótulos marcados
plt.tick_params(axis='both', labelsize=14)


plt.show()