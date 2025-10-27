n = []
c1 = 1
for c in range(0, 7, 1):
    n.append(input('Digite o no que a pesssoa número ({}) nasceu.'.format(c1)))
    c1 += 1
def eh_real(n):
    try:
        for item in n:
            int(item)
        return True
    except (ValueError, TypeError):
        return False
while True:
    if eh_real(n) == True:
        break
    else:
        print('=-'*20)
        print('Você não digitou um números validos (somente números inteiros)!!!')
        print('=-'*20)
        for c in range(0, 7, 1):
            n[c] = input('Digite um número inteiro?')
c = 0
for c in range(0, 7, 1):   
    n[c] = int(n[c]) 
c1 = 1
somamaiores = 0
somamenores = 0
for c in range(0, 7, 1):
    if n[c] > 2004: 
        somamenores += 1
        print('já o data de nacimento número ({}) não tem mais do que 21 anos e nasceu no ano {}.'.format(c1, n[c]))
    if n[c] <= 2004:
        somamaiores +=1
        print('Tem 21 anos ou mais data de nacimento número ({}) e nasceu  no ano  {}.'.format(c1, n[c]))
    c1 += 1
print('=-'*20)
print('A todo tivemos {} pessoas maiores de 21 anos'.format(somamaiores))
print('E também tivemos {} pessoas menores de 21 anos.'.format(somamenores))