import random
print("-="*30)
print('Jokenpô')
print('escolha (1) para tesoura')
print('escolha (2) para papel')
print('escolha (3) para pedra')
escolha = str(input('Digite o número que representa sua escolha? '))
escolhaletra = escolha.isalpha()
escolhaint = escolha.isdigit()
if escolha == '1' or escolha == '2' or escolha == '3':
    escolha = int(escolha)
else:
    while escolhaletra == True and escolhaint == False:
        print('=-'*30)
        print('Tente novamente só pode ser 1,2 ou 3')
        print('=-'*30)
        print('escolha (1) para tesoura')
        print('escolha (2) para papel')
        print('escolha (3) para pedra')
        escolha = input('Digite o número que representa sua escolha? ')
        escolhaletra = escolha.isalpha()
        escolhaint = escolha.isdigit()
    escolha = int(escolha)
numeroescolhido = random.randint(1, 3)
if numeroescolhido == 1:
    print('O algoritimo escolheu tesoura!')

