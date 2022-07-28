# palavra secreta -  jogo

secret_word = 'cachorro'   #palavra que terá que ser adivinhada
digitadas = []             #lista com as letras que o usuário irá digitar
chances = 5                #Número de chances que o usuário terá

while True:
    if chances <= 0:       #Enquanto as chances forem maiores que zero o usuário poderá continuar digitando letras
        print('Você perdeu!!')
        break
    letra = input('Digite uma letra: ')
    print()

    if len(letra) > 1:     #Se for digitado mais de uma letra não irá prosseguir
        print('Digite apenas uma letra!!!')
        continue

    digitadas.append(letra) #Adiciona a letra digitada na lista digitadas

    if letra in secret_word: #Se a letra existe na palavra secreta
        print(f'Show!!..A letra "{letra}" existe na palavra secreta!')
    else:                    #Se a letra NÃO existe na palavra secreta
        print(f'A letra "{letra}" não existe na palavra secreta')
        digitadas.pop()      #Exclui a última letra digitada
        chances -= 1         #Exclui uma chance
        print(f'Você ainda tem {chances} chances.')

    secret_temp = ''
    for letra in secret_word:  #para letra na palavra secreta
        if letra in digitadas: #se a letra existir em digitadas
            secret_temp += letra
        else:
            secret_temp += '*' #coloca asterisco no lugar das letras que ainda não foram descobertas

    if secret_temp == secret_word: #quando a palavra temporário for igual a palavra secreta
        print(f'Que legal!! Você acertou... a palavra era {secret_word}!!!!')
        break
    else:
        print(f'A palavra secreta está assim: {secret_temp}')
        print()
