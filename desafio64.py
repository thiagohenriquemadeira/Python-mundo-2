n = []
c = 0
soma = 0
while True:
    n.append(int(input('Digite um número [999 para parar]:')))
    if n[c] == 999:
        break
    else:
        soma = soma + n[c]
        c += 1
print('=-' * 20)
print('Foram Digitados ({}) números  e a soma é {}.'.format(c, soma))