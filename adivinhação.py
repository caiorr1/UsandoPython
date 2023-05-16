import random

print('*********************************')
print('Bem vindo ao Jogo de Adivinhação!')
print('*********************************')

tentativas = 3
num_secreto = random.randrange(1,101) 


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
        print("Parabéns! Você acertou!")
        break
    else:
        if(maior):
            print("O seu chute foi maior do que o número secreto!")
        elif(menor):
            print("O seu chute foi menor do que o número secreto!")

print("Fim do jogo")