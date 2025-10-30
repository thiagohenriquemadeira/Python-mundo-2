print('='*20)
print('Sequência de Fibonacci')
print('='*20)
n = int(input('Quantos termos você quer mostrar?'))
c =  0
c1 =  0
fibo = 0
cont = 0
nlista =[]
nlista.append(0)
nlista1 = []
nlista1.append(1)
print('=' * 30)
while True:
    print('{} => '.format(nlista[c]), end='')
    nlista.append(nlista[c] + nlista1[c])
    cont += 1
    if cont == n:
        break
    print('{} => '.format(nlista1[c]), end='')
    nlista1.append(nlista[c+1] + nlista1[c])
    c += 1
    cont += 1
    if cont == n:
        break
print('FIM')
print('=' * 30)
