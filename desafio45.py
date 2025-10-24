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
    while True:
        print('=-'*30)
        print('Tente novamente só pode ser 1,2 ou 3')
        print('=-'*30)
        print('escolha (1) para tesoura')
        print('escolha (2) para papel')
        print('escolha (3) para pedra')
        escolha = input('Digite o número que representa sua escolha? ')
        escolhaletra = escolha.isalpha()
        escolhaint = escolha.isdigit()
        if escolha == '1' or escolha == '2' or escolha == '3':
            break
    escolha = int(escolha)
numeroescolhido = random.randint(1, 3)
maquinaescolheu = ''
voceescolheu = ''
print('=-'*20)
if numeroescolhido == 1:
    print('O algoritimo escolheu tesoura!')
    maquinaescolheu = 'TESOURA'
elif numeroescolhido == 2:
    print('O algoritimo escolheu papel!')
    maquinaescolheu = 'PAPEL'
elif numeroescolhido ==  3:
    print('O algoritimo escreveu pedra')
    maquinaescolheu = 'PEDRA'
if escolha == 1:
    voceescolheu = 'TESOURA'
elif escolha == 2:
    voceescolheu = 'PAPEL'
elif escolha == 3:
    voceescolheu = 'PEDRA'
print('=-'*20)
if numeroescolhido == escolha:
    print('Os dois escolheram {} deu Empate!!!'.format(voceescolheu))
elif (numeroescolhido == 1 and escolha == 2) or (numeroescolhido == 2 and escolha == 3) or (numeroescolhido == 3 and escolha == 1):
    print('Você escolheu {} e maquina {} maquina sempre vençe!'.format(voceescolheu, maquinaescolheu))
elif (numeroescolhido == 2 and escolha == 1) or (numeroescolhido == 3 and escolha == 2) or (numeroescolhido == 1 and escolha == 3):
    print('Você escolheu {} e a maquina {}, Então você venceu a maquina!!!'.format(voceescolheu, maquinaescolheu))