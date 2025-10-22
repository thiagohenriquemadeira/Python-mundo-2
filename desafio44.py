print('-='*20)
print('Analizador de compras')
print('-='*20)
preconormal = float(input('Escreva um preço de um produto? '))
precofinal = preconormal
print('='*20)
print('digite (1) para pagar a vista/dinheiro ou cheque  com 10% de desconto')
print('digite (2) a vista no cartão com 5% de desconto')
print('digite (3) em até 2x no cartão preço normal')
print('digite (4) 3x ou mais no cartão 20% de juros')
escolha = str(input('Digite o número de sua escolha: '))
escolhaparcela = 0
escolhatrue = escolha.isalpha()
escolhaint = escolha.isdigit()
if escolha == '1' or escolha == '2'or escolha == '3' or escolha == '4':
    escolha = int(escolha)
if escolhatrue == True:
    while  escolhatrue == True and escolhaint == False:
        print('=-'*20)
        print('Você escolheu uma opção que não temos')
        print('=-'*20)
        print('digite (1) para pagar a vista/dinheiro ou cheque  com 10% de des conto')
        print('digite (2) a vista no cartão com 5% de desconto')
        print('digite (3) em até 2x no cartão preço normal')
        print('digite (4) 3x ou mais no cartão 20% de juros')
        escolha = input('Digite o número de sua escolha: ')
        escolhatrue = escolha.isalpha()
        escolhaint = escolha.isdigit()
if escolha == '1' or escolha == '2'or escolha == '3' or escolha == '4':
    escolha = int(escolha)
if escolha > 4:
    while escolha > 4:
        print('=-'*20)
        print('Você escolheu uma opção que não temos')
        print('=-'*20)
        print('digite (1) para pagar a vista/dinheiro ou cheque  com 10% de des conto')
        print('digite (2) a vista no cartão com 5% de desconto')
        print('digite (3) em até 2x no cartão preço normal')
        print('digite (4) 3x ou mais no cartão 20% de juros')
        escolha = input('Digite o número de sua escolha: ')
if escolha == 1:
    precofinal = preconormal - (precofinal * (10 / 100)) 
    print('Você vai pagar R${:.2f}'.format(precofinal))
elif escolha == 2:
    precofinal = preconormal - (precofinal * (5 /100))
    print('Você vai pagar R${:.2f}'.format((precofinal)))
elif escolha == 3:
    precofinal = precofinal / 2
    print('Você vai pagar R${:.2f} 2x no cartão de com parcelas custando R${:.2f}'.format(preconormal, precofinal))
elif escolha == 4:
    precofinal = preconormal + (precofinal * (20 / 100 ))
    escolhaparcela = int(input('Quantas parcelas exatamente? '))
    if escolhaparcela < 3:
        while escolhaparcela < 3:
            print('='*20)
            print('Escolha novamente já que tem que ser 3 parcelas ou mais o número de parcelas!')
            escolhaparcela = int(input('Quantas parcelas exatamente? '))
    preconormal = precofinal / escolhaparcela
    print('Você vai pagar R${:.2f} {}x no cartão de com parcelas custando R${:.2f}'.format(precofinal, escolhaparcela, preconormal))
