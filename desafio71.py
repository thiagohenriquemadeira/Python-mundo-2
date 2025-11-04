print('=' * 30)
print('     BANCO CEV     ')
print('=' * 30)
n = float(input("Que valor você quer sacar? R$"))
centena = 50
con50 = 1
sobra = 0
cont20 = 0
cont10 = 0
cont5 = 0
cont1 = 0
while True:
    if n == centena:
        break
    elif centena > n and centena >= 100:
        sobra =  centena - n
        con50 -= 1
        sobra -= 50
        sobra = sobra * -1
        break
    elif centena > n:
        sobra = n
        con50 -= 1
        break
    centena += 50
    con50 += 1
if sobra >= 20:
    cont20 += 1
    sobra -= 20
if sobra >= 20:
    cont20 += 1
    sobra -= 20
if sobra >= 10:
    cont10 += 1
    sobra -= 10
if sobra >= 5:
    cont5 += 1
    sobra -= 5
if sobra != 0:
    while True:
        if sobra == 0:
            break
        cont1 +=1
        sobra -=1

if con50 >= 1:
    print('Total de {} cédulas de R$50'.format(con50))
if cont20 >= 1:
    print('Total de {} células de R$20'.format(cont20))
if cont10 >= 1:
    print('Total de {} células de R$10'.format(cont10))
if cont5 >= 1:
    print('Total de {} células de R$5'.format(cont5))
if cont1 >= 1:
    print('Total de {} células de R$1'.format(cont1))
print('='*30)
print('Volte sempre ao BANCO CEV! Tenha um bom dia!')