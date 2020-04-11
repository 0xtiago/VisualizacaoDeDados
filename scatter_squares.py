import matplotlib.pyplot as plt

plt.scatter(2,4, s=200)

#Define o titulo do grafico e nomeia os eixos
plt.title("Raiz Quadrada", fontsize=24)
plt.xlabel("Valor", fontsize=14)
plt.ylabel("Raiz quadrada do valor", fontsize=14)

#Define o tamanho dos rótulos das marcações
plt.tick_params(axis='both', which='major', labelsize=14)

plt.show()

