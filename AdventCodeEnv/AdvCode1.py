import pandas as pd

list = pd.read_csv('entrada.csv')

""" Ordenamos de mayor a menor cada lista con su columna respectiva 
    y usando el argumento reverse=True 
"""
lista1_ordenada = sorted(list['Lista1'], reverse=True)
lista2_ordenada = sorted(list['Lista2'], reverse=True)

#print(lista1_ordenada[0])
#print(lista2_ordenada[0])

total = 0

for i in range(len(lista1_ordenada)):
    total = total + abs(lista1_ordenada[i] - lista2_ordenada[i])

print(total)