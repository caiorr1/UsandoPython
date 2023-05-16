import adivinhação
import forca


def escolhe_jogo():
    print('*********************************')
    print('*******Escolha o seu jogo!*******')
    print('*********************************')

    print('(1) Forca (2) Adivinhação')
    jogo = int(input('Qual o jogo?\n')) 

    if jogo == 1:
        print('Carregando Jogo da Forca......')
        forca.jogo_forca()
    elif jogo == 2:
        print('Carregando Jogo da Adivinhação......')
        adivinhação.jogo_adivinhacao()

if (__name__ == '__main__'):
    escolhe_jogo()