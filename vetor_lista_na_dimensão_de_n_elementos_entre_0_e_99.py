

import random
from statistics import median
# Lista de dimensão de n elementos

valores_aleatorios = []
desvio_padrao = 0
variancia = 0
n = int(input("Digite o numero: "))
def linha():
    print("-"*70)
for i in range(0,n):
    valores_aleatorios.append(random.randint(0,99))


print(valores_aleatorios)
#obtendo a média da lista
media = sum(valores_aleatorios)/len(valores_aleatorios)
print("Média da lista:")
print("%1.f"%media)

#Mediana dos valores aleatorios 
mediana_valores_aleatorios = median(valores_aleatorios)
print("Mediana:")
print("%1.f"%mediana_valores_aleatorios)
#Variância
for i in range(0,n):
    variancia = variancia + ((valores_aleatorios[i]- media)**2)
    linha()
    print("%1.f"%variancia)
print("_"*60)
variancia_2 = variancia/(n-1)
print("variancia: %1.f"%variancia_2)
# Desvio padrão
desvio_padrao = variancia_2**(1/2)
print("Desvio padrão: %1.f "%desvio_padrao)
