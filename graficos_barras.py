import matplotlib.pyplot as plt

# Temperaturas....
#cidade_a = [32, 30, 27, 28, 29, 24]
#cidade_b = [27, 26, 29, 25, 22, 22]
#cidade_c = [17, 19, 15, 20, 25, 26]

# Homicidios....
cidade_a = [5, 2, 0, 0, 2, 1]
cidade_b = [2, 1, 2, 4, 3, 6]
cidade_c = [8, 5, 2, 0, 2, 6]

data = [5, 10, 15, 20, 25, 30]

# Criar posições distintas para cada cidades....
#posicoes_a = list(range(len(data)))
#posicoes_b = [pos + 0.25 for pos in posicoes_a]
#posicoes_c = [pos + 0.20 for pos in posicoes_a]


plt.bar(data, cidade_a, color = "r", label = "Cidade A.")
plt.bar(data, cidade_b, bottom = cidade_a, color = "g", label = "Cidade B.")
plt.bar(data, cidade_c, bottom = [a + b for a, b in zip(cidade_a, cidade_b)], color = "b", label = "Cidade C.")
plt.legend()
plt.xlabel("Data.")
plt.ylabel("Homicidios.")
plt.title("Homicidios nas Cidades em Dias Determinados.")
#plt.xticks(ticks=posicoes_a, labels=data)
plt.show()