# Juros Simples....

import matplotlib.pyplot as plt

def jurosCompostos(VP, i, n):
    VF = VP * (1 + i) ** n
    return VF

def jurosSimples(VP, i, n):
    VF = VP * (1 + i * n)
    return VF

# Lista de anos
anos = list(range(15))

# Valor em cada ano....
VP = 100
i = 0.09

# Valor em cada ano com juros compostos....
VF_compostos = [jurosCompostos(VP, i, n) for n in anos]

# Valor em cada ano com juros simples....
VF_simples = [jurosSimples(VP, i, n) for n in anos]


# Criar gráfico da evolução dos valores....
plt.plot(anos, VF_compostos, label='Juros Compostos.')
plt.plot(anos, VF_simples, label='Juros Simples.')
plt.xlabel("Ano")
plt.ylabel("Valor")
plt.title("Comparação entre Juros Simples e Compostos.")
plt.legend()
plt.show()