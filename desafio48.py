c = 1
soma = 0
for c in range(c, 501, 1+1):
    if (c % 3) == 0 :
        soma += c
    print('contador {}'.format(c))
print(soma)