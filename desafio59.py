n = [0, 0]
resposta = 0
soma = 0
multiplicacao = 0
maior = 0
while resposta != 5:
    for c in range(0, 2, 1):
        n[c] = float(input(' Digite um valor:'))
    print('Opções:')
    print('[1] somar')
    print('[2]mutiplicar')
    print('[3]maior')
    print('[4] novos números')
    print('[5] sair do programa')
    resposta = int(input('Digite uma das opões:'))
    if resposta == 1:
        soma = n[0] + n[1]
        print('A Soma é {}'.format(soma))
        resposta = int(input('Digite [4] para os colher outros números ou [5] para sair:'))
    elif resposta == 2:
        multiplicacao = n[0] * n[1]
        print('A multiplicção é {}'.format(multiplicacao))
        resposta = int(input('Digite [4] para os colher outros números ou [5] para sair:'))
    elif resposta == 3:
        for c in range(0, 2, 1):
            if n[c] > maior:
                maior = n[c]
        print('O MAIOR foi [{}] '.format(maior))
        resposta = int(input('Digite [4] para os colher outros números ou [5] para sair:'))
print('Finalizou!!!')