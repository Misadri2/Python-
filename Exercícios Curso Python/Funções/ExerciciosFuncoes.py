# Ex 01
# def saudacao(saudacao, nome):
#     return print(f'{saudacao}, {nome}!!')
#
#
# saudacao('Oi', 'Mis')

# Ex 02
# def soma(a, b, c):
#     return print(a + b + c)
#
#
# soma(1, 1, 2)

# Ex 03
# def percentual(a, b):
#     return print(a + (a * (b / 100)))
#
#
# percentual(500, 10)

# Ex 04
def fizzBuzz(number):
    if number % 3 == 0 and number % 5 == 0:
        return 'FizzBuzz'
    if number % 3 == 0:
        return 'Buzz'
    if number % 5 == 0:
        return 'Fizz'
    print(number)

#Para gerar números aleatórios entre 0 e 100 chamando a função fizzBuzz
from random import randint

for i in range(100):
    aleatorio = randint(0, 100)
    print(fizzBuzz(aleatorio))
