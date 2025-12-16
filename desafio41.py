from datetime import date
ano =int(input('Que ano você nasceu? '))
hoje = date.today().year
idade = ( hoje - ano )
if idade <= 9:
    print(' Você tem {} anos e um atleta MIRIM'.format(idade))  
elif idade <= 14 and idade  > 9:
    print('Você tem {} anos e um atleta INFANTIL'.format(idade))
elif idade <= 19 and idade > 14:
    print('Você tem {} anos e um atleta JUNIOR'.format(idade))
elif idade <= 20 and idade > 19:
    print('Você tem {} anos e um atleta SÊNIOR'.format(idade))
else:
    print('Você tem {} anos e um atleta MASTER'.format(idade))
