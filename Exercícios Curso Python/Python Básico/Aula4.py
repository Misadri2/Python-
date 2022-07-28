#Condições If, Elif e Else
# '=' estou afirmando que é igual
# '==' estou perguntando se é igual
'''
if 2 != 4:
    print('Verdadeiro')
    print('Projeto Demorado')
else:
    print('False')
'''


nome = input('Por favor,digite seu nome: ')
idade = int(input('Digite sua idade: '))

idade_limite_inferior = 18
idade_limite_superior = 70

if idade < idade_limite_inferior or idade > idade_limite_superior:
    print(f'{nome} Não tem limite de crédito')
else:
    print(f'{nome} Tem limite de crédito')



