print('=-'*19 , end='')
print('=')
print('VAMOS JOGAR PAR OU IMPAR')
print('=-'*19 , end='')
print('=')
cont = 0
import random
while True:
    n = int(input('Digite um valor ?'))
    decisao = str(input('Par ou Impar? [P/I] ').upper())
    m = (random.randint(1, 10))
    soma = n + m
    parouimpar = soma % 2
    if parouimpar == 0:
        resposta = 'PAR'
        print('=' * 20)
        print('Você jogou {} e o computador {}. Total deu {} DEU {}'.format(n,  m, soma, resposta))
    elif parouimpar != 0:
        resposta = 'IMPAR'
        print('=' * 20)
        print('Você jogou {} e o computador {}. Total deu {} DEU {}'.format(n,  m, soma, resposta))
    if decisao == 'P' and resposta == 'PAR':
        print('='* 20)
        print('Você VENCEU!')
        print('Vamos jogar novamente...')
        print('=-' * 20)
        cont +=1
    elif decisao == 'I' and resposta == 'IMPAR':
        print('='* 20)
        print('Você VENCEU!')
        print('Vamos jogar novamente...')
        cont +=1
        print('=-' * 20)
    else:
        print('=' * 20)
        print('Você PERDEU')
        print('=-' * 20)
        print('GAMER OVER! Você venceu {} vezes.'.format(cont))
        break