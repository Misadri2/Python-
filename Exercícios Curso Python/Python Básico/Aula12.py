#Iterando strings com laço while
from itertools import count

frase = 'O rato roeu a roupa do rei de Roma'
tamanho_frase = len(frase)
contador = 0
letra_escolhida = 'r'
nova_string = ''

# while contador < tamanho_frase:
#     print(frase[contador], contador)
#     contador += 1

# Procura a letra escolhida e troca pela letra M
while contador < tamanho_frase:
    letra = frase[contador]
    if letra == letra_escolhida:
        nova_string += 'M'
    else:
        nova_string += letra
    contador += 1
print(nova_string)


