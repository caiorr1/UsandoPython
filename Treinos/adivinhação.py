import random

def jogo_adivinhacao():
    print('\n*********************************')
    print('Bem vindo ao Jogo de Adivinhação!')
    print('*********************************')

    tentativas = 0
    num_secreto = random.randrange(1,101)
    pontos = 1000 

    print('Qual o nível de dificuldade?')
    print('(1) Fácil (2) Médio (3) Difícil')

    nivel = int(input('Defina o nível: '))

    if nivel == 1:
        tentativas = 15
    elif nivel == 2:
        tentativas = 10
    else:
        tentativas = 5
        

    for rodada in range (1, tentativas + 1):  
        print(f'Tentativa {rodada} de {tentativas}')
        num_user = input('Digite um número entre 1 e 100: ')
        chute = int(num_user)
        if chute < 0 or chute > 100:
            print('Você deve digitar um número de 1 a 100')
            continue
        
        print(f'Você digitou {num_user}')
        acertou = chute == num_secreto
        maior = chute > num_secreto
        menor = chute < num_secreto

        if(acertou):
            print(f'Parabéns, você acertou e fez {pontos} pontos!')
            break
        else:
            if(maior):
                print("O seu chute foi maior do que o número secreto!")
            elif(menor):
                print("O seu chute foi menor do que o número secreto!")
            pontos_perdidos = abs(num_secreto - chute)
            pontos = pontos - pontos_perdidos

    print("Fim do jogo")

if (__name__ == '__main__'):
    jogo_adivinhacao()