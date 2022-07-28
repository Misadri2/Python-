"""
For/Else em Python
"""

# variavel = ['Mislaine', 'Marcio', 'Bruce', 'Mary']
#
# for valor in variavel:
#     if valor.startswith('P'):
#         print(valor)
#         continue
# else:  #Else não é muito utilizado em laço for, mas existe a possibilidade
#     print('Nenhum nome começa com a letra indicada')

"""
Split(dividir uma string em lista), Join(Juntar uma lista), Enumerate (enumerar elementos de uma lista 'iteráveis')
"""
#
#Split
string = 'O Brasil é quente, O Brasil tem praias'
lista1 = string.split(' ') #tranformou a frase em string em uma lista usando os espaços
lista2 = string.split(',') #tranformou a frase em string em uma lista usando vírgulas
print(lista1)
print(lista2)

palavra = ''
contagem = 0
for valor in lista1:
    print(f'A palavra {valor} apareceu {lista1.count(valor)}')









