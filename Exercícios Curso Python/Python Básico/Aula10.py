#Estrutura de Repetição - While
'''
while True: #enquanto a condição for verdadeira será executado o que estiver abaixo
    pass
'''


x = 10
while x <= 50:
    print(x)
    x = x + 10

print('Acabou')
print('*****************')

#Exemplo 2
x = 1
while x <= 5:
    if x == 3 or x == 4:
        x = x + 1
        continue  #quando atender a condição do if vai pular para o próximo laço do while
    print(x)
    x = x + 1

print('Acabou')
print('*****************')

#Exemplo 3
x = 1
while x <= 5:
    if x == 2:
        x += 1
        break  #quando atender a condição do if vai encerrar o laço do while
    print(x)
    x = x + 1

print('Acabou')