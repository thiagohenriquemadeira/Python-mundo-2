print('=-'*20)
print('Vamos descobrir o fatorial')
print('=-'*20)
n = int(input('Digite um número para fazer o fatorial:'))
c = n
soma = n
while c != 0:
    c -= 1
    if c == 0:
        soma = soma
    else:
        soma = soma * c  
print('O fatorial de [{}!] é {} '.format(n, soma))