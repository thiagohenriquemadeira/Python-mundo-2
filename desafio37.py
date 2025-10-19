import math
numero1 = str(input('Escreva um número inteiro? '))
contador = 0
final = len(numero1) 
naobinario = [False] * final
naooctal = [False]  * final
while contador < final :
    print(contador)
    if numero1[contador] == '0' or numero1[contador] == '1':
       naobinario[contador] = True 
    contador += 1
print(naobinario)
if all(naobinario):
    print('e um número Binário!')
else:
    print('Não e um número Binário')