n = []
cs = 1
for c in range(0, 5, 1):
    n.append(float(input('Digite o peso da pessoa numero ({}) :'.format(cs))))
    cs += 1
maior = 0
menor = n[0]
for c in range(0, 5, 1):
    if n[c] > maior:
        maior =  n[c]
    if n[c] < menor:
        menor = n[c]
print('O maior peso foi {} e o menor foi {}.'.format(maior, menor))