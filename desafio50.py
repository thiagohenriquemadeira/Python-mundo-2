c = 0
c2 = 6
n = []
for c in range(c, c2, 1):
    n.append(input('Digite um número inteiro?'))
c = 0
c2 = 6
def todos_inteiros(n):
    try:
        for item in n:
            int(item)
        return True
    except (ValueError, TypeError):
        return False
while True:    
    if todos_inteiros(n) == True:
        break
    else:
        print('=-'*20)
        print('Digite um número inteiro você não digitou um númro inteiro!')
        for c in range(c, c2, 1):    
            n[c] = input('Digite um número?')
c = 0
c2 = 6
soma = 0
for c in range(c, c2, 1):    
    n[c] = int(n[c]) 
for numero in n:
    if numero  %  2  == 0:
        soma += numero 
print(' a soma dos números pares é {}'.format(soma)) 