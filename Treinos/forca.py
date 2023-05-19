
def jogo_forca():
    print('\n*********************************')
    print('Bem vindo ao Jogo de Forca!')
    print('*********************************')

    palavra_secreta = 'banana'
    enforcou = False
    acertou = False

    while not enforcou and not acertou:
        
        chute = input('Qual letra?\n').lower()

        posicao = 0
        for letra in palavra_secreta:
            if chute == letra:
                print(f'Encontrei a letra {letra} na posição {posicao}')
            posicao += 1
        print('jogando...')

    print('Fim do jogo!')



if (__name__ == '__main__'):
    jogo_forca()