print('-' * 30)
print('     LOJA SUPER BARATÃO    ')
print('-' * 30)
n = []
n.append(0)
produto = ['']
produto.append(' ')
continuar ='f'
c = 0
soma = 0
mil = 0
while True:
    produto[c] = str(input('Nome do Produto: '))
    produto.append(' ')
    while True:
        n[c] = float(input('Preço: R$'))
        if n[c] > 0:
            n.append(0)
            soma += n[c]
            if c == 0:
                nomemenor = produto[0]
                precomenor = n[0]
            elif n[c] < precomenor:
                precomenor = n[c]
                nomemenor = produto[c]
            if n[c] > 1000:
                mil += 1    
            break
    while continuar != 'S' and continuar != 'N':
        continuar = str(input('Quer continuar ? [S/N] ').upper())
    if continuar == 'N':
        break
    c += 1
    continuar = 'f'
print('-' * 10 ,end='')
print(' FIM DO PROGRAMA ',end='')
print('-' * 10)
print('O total da compra foi R${:.2f}'.format(soma))
print('Temos {} produtos custando mais de R$1000.00'.format(mil))
print('O produto mais barato foi {} que custa R${:.2f}'.format(nomemenor, precomenor))