print('*********************************')
print('Bem vindo ao Jogo de Adivinhação!')
print('*********************************')

num_secreto = '13'
num_user = input('Digite o seu número: ')

print(f'Você digitou {num_user}')

if num_user == num_secreto:
    print('-----------------------')
    print('PARABENSSSSSSSSSSSSSSSS')
    print('-----------------------')
    print('Você acertou o número!')
else:
    while num_user != num_secreto:
        print('Você errou, tente novamente')
        num_user = input('Digite o seu número: ')
        if num_user == num_secreto:
            print('-----------------------')
            print('PARABENSSSSSSSSSSSSSSSS')
            print('-----------------------')
            print('Você acertou o número!')
        else:
            ('Errou')
        
