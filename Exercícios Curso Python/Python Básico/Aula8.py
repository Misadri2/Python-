"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande".
"""
user_name = input('Type your first name: ')
if len(user_name) <= 4:
    print('Your name is too short')
elif len(user_name) <= 6 or len(user_name) >= 5:
    print('Your name is normal')
else:
    print('Your name is too long')