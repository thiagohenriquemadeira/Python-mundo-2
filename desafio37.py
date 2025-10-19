numero1 = str(input('Escreva um número inteiro? '))
contador = 0
final = len(numero1) 
naonumero = final -1
nao = [False] * final
while contador < final :
    print(contador)
    if numero1[contador] == '0' or numero1[contador] == '1':
       nao[contador] = True 
    contador += 1
print(nao)