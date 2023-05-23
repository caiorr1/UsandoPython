def jogo_forca():
    print('\n*********************************')
    print('Bem vindo ao Jogo de Forca!')
    print('*********************************')

    palavra_secreta = 'banana'
    letras_acertadas = ['_', '_', '_', '_', '_', '_']
    enforcou = False
    acertou = False

    while not enforcou and not acertou:
        
        chute = input('Qual letra?\n').upper()
        chute = chute.strip()

        index = 0
        for letra in palavra_secreta:
            if chute == letra.upper():
                letras_acertadas[index] = letra
            index += 1

        print(letras_acertadas)

    print('Fim do jogo!')
