num = int(input('Digite um número inteiro: '))
print('''EScolha uma das bases para conversão:
[1] converter para BINÁRIO
[2] converter para OCTAL
[3] converter para HEXADECIMAL
''')
opcâo = int(input('Sua opção: '))
if opcâo == 1:
    print('{} convertido para BINÁRIO é igual a {}'.format(num, bin(num)[2:]))
elif opcâo == 2:
    print('{} convertido para OCTAL é igual a {}'.format(num, oct(num)[2:]))
elif opcâo == 3:
    print('{} convertido para BINÁRIO é igual a {}'.format(num, hex(num)[2:]))
else:
    print('Opção não existente recomece o programa!')