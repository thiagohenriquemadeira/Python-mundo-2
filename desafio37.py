import math
numero1 = str(input('Escreva um número inteiro? '))
contador = 0
final = len(numero1) 
naobinario = [False] * final
naooctal = [False]  * final
naohexa = [False] * final
while contador < final :
    if numero1[contador] == '0' or numero1[contador] == '1':
       naobinario[contador] = True 
    if numero1[contador] == '0' or numero1[contador] == '1' or numero1[contador] == '2' or numero1[contador] == '3' or numero1[contador] == '4' or numero1[contador] == '5' or numero1[contador] == '6' or numero1[contador] == '7':
        naooctal[contador] = True
    if numero1[contador] == '0' or numero1[contador] == '1' or numero1[contador] == '2' or numero1[contador] == '3' or numero1[contador] == '4' or numero1[contador] == '5' or numero1[contador] == '6' or numero1[contador] == '7' or numero1[contador] == '8' or numero1[contador] == '9':
       naohexa[contador] = True
    contador += 1
if all(naooctal):
    print('E um número Octal!')
else:
    print('Não e um número Octal!')
if all(naobinario):
    print('E um número Binário!')
else:
    print('Não e um número Binário!')
if all(naohexa):
    print('E um número Hexadecimal!')
else:
    print('Não e um número Hexadecimal!')