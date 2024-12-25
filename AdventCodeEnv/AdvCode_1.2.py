import pandas as pd

list = pd.read_csv('entrada.csv')

lista1_ordenada = sorted(list['Lista1'])
lista2_ordenada = sorted(list['Lista2'])

print(lista1_ordenada)
print(lista2_ordenada)  

puntaje = 0

for x in range(len(lista1_ordenada)):
    for y in range(len(lista2_ordenada)):
        if lista1_ordenada[x] == lista2_ordenada[y]:
            puntaje = puntaje + lista1_ordenada[x] 

print(puntaje)