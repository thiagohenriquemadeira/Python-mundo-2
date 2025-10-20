idade = int(input('Digite sua idade? '))
contador = 0
idademenor = idade
if idade < 18:
    while idademenor < 18:
        idademenor += 1
    idademenor = idademenor - idade
    if idademenor == 1:
        print('Você vai ter que ser alistar quando você tiver 18 anos! você tem {} anos e faltam {} ano para se alistar.'.format(idade, idademenor))
    else:
        print('Você vai ter que ser alistar quando você tiver 18 anos! você tem {} anos e faltam {} anos para se alistar.'.format(idade, idademenor))
elif idade == 18:
    print('Chegou a hora de se alistar!')
else:
    while idademenor > 18:
        idademenor -= 1
        contador += 1         
    print('Já passou o tempo de sé alistar! isso foi {} ano(s) atrás.'.format(contador))
    