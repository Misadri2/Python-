contador = 1
acumulador = 1
'''
Laço while é usado quando você não tem noção do final, como uma iteração por exemplo
'''
while contador <= 10:
    print(contador, acumulador)
    acumulador = acumulador + contador
    contador += 1
else:
    print('Cheguei ao final do While')