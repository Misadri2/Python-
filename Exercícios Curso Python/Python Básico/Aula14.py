# Listas em Python
"""
fatiamento
append, insert, pop, del, clear, extend, +
min, max
range
"""

texto = 'Valor'
lista1 = [1, 2, 3, 4, 5, 6, 7]
lista2 = [8, 9, 10, 11, 12]
l3 = lista2 + lista1
"""
lista[2] = 'Três'
print(lista[2])
print(lista[0:5]) #mostrará desde o primeiro num até o quarto num da lista
print(lista[0]) #primeiro item da lista
print(lista[-1]) #último item da lista
print(lista[::2]) #pular de dois em dois
print(lista[::-1]) #invertendo a lista
print(l3) #somando as duas listas
"""

#Funções
lista1.append(lista2)  #incrementa a lista2 ao final da lista1
lista1.insert(0, 0)  #adicionou o valor 0 na posição indicada, no caso na posição zero
print(lista1)
del(lista1[0])
print(lista1)

l2 = [1, 2, 3, 4, 5, 6, 7, 8, 9] #funções abaixo mostram valor mínimo e máximo da lista
print(max(l2))
print(min(l2))

l3 = list(range(10, 50, 10))  #imprime o range da lista conforme indicado
print(l3)