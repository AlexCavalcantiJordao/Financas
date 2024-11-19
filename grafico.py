from matplotlib import pyplot as plt
from matplotlib.lines import lineStyles

eixo_x_dias = [1, 5, 10, 15, 20, 25, 30]
eixo_y_temp_max = [28, 29,25, 32, 34, 36, 31]
eixo_y_temp_min = [17, 20, 21, 22, 23, 24, 24]

plt.title("Temperatura máximas e mínimas")
plt.xlabel("Data")
plt.ylabel("Temperatura")


#plt.plot(eixo_x_dias, eixo_y_temp_max, linestyle="--", marker="o")
#plt.plot(eixo_x_dias, eixo_y_temp_min, linestyle="--", marker="o")

#plt.legend(["Temperatura Máxima.", "Temperatura Mínima."])
#plt.grid(True or False)
#plt.axis([1, 31, 5, 45])
#plt.xlim([1, 31])
#plt.ylim([-5, 50])
#print(plt.axis())
#plt.savefig("meu_grafico.png")

# Plotar gráfico de uma função, como f(x) = x³ + 1
x = range(1, 11, 1)
plt.plot(x, [(val ** 3 + 1) for val in x])
plt.show()