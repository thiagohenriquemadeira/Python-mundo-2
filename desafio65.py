n = []
c = 0
resposta = 'Não'
maior = 0
media = 0
cont = 0
while True:
    n.append(int(input('Digite um número:')))
    resposta = str(input('Digite se quer constinuar: [S/N]').upper())
    media = media + n[c]
    if n[c] > maior:
        maior = n[c]
    if c == 0:
        menor = n[c]
    elif n[c] < menor:
        menor = n[c]        
    c += 1
    cont += 1
    if resposta == 'N':
        break
print('Você digitou {} números e a média foi {}'.format(c, media / c))
print('O maior valor foi {} e o menor foi {}'.format(maior, menor))