numero = input('Digite um número?')
c2 = 11
resultado = 0
c = 0
letra = numero.isalpha()
inteiro = numero.isdigit()
if inteiro == True:
    numero = int(numero)
else:
    while True:
        print('=-'*30)
        print('Tente novamente só pode ser um número inteiro')
        print('=-'*30)
        numero = input('Digite um número? ')
        inteiro = numero.isdigit()
        if inteiro == True:
            break
    numero = int(numero)
for c in range(c, c2, 1):
    resultado = (numero * c)
    print('{} x {} = {}'.format(c, numero, resultado))