import random
print('=-'*20)
print('Acerte o número aleatorio de 0 a 10 que o algoritimo pensou')
print('=-'*20)
ncliente = int(input('Digite um o valor que o algoritimo escolheu: '))
n =random.randint(0, 10)
c = 1
print('o número que o algoritimo escolheu foi esse {}'.format(n))
print('=-'*20)
while n != ncliente:
    c += 1
    n = random.randint(0, 10)
    print('o número que o algoritimo escolheu foi esse {}'.format(n))
    ncliente = int(input('Digite um o valor que o algoritimo escolheu: '))
    print('=-'*20)
print('O número que o algoritimo escolheu foi esse {}'.format(n))
print('Demorou ({}) palpites você escolheu esse {} então você ganhou!!!'.format(c, ncliente))
print('=-'*20)