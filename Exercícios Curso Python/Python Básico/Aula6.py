"""Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""
num = input("Digite um número inteiro: ")

if num.isdigit():
    num = int(num)
    if num % 2 == 0:
        print("Esse número é par!")
    else:
        print("Esse número é impar")

else:
    print("Isso não é um número inteiro")



