idade = []
idade.append(0)
c = 0
sexo = ['']
sexo.append('s')
continuar = 'g'
mais18 = 0
hcadastrados = 0
feeminino20 = 0
while True:
    print('-' *30)
    print('  CADASTRE UMA PESSOA  ')
    print('-' * 30)
    while True:
        idade[c] = int(input('Idade: '))
        if idade[c] > 0:
            idade.append(-5)
            if idade[c] > 18:
                mais18 += 1
            break
    while True:
        sexo[c] = str(input('Sexo: [M/F] ').upper())
        if sexo[c] == 'M' or sexo[c] == 'F':
            sexo.append('g')
            if sexo[c] == 'M':
                hcadastrados += 1 
            break
    print('-' * 20)
    while continuar != 'S' and continuar != 'N':
        continuar = str(input('Quer continuar ? [S/N] ').upper())
    if sexo[c] == 'F' and idade[c] < 20:
        feeminino20 += 1
    if continuar == 'N':
        break
    c += 1
    continuar = 'f'
print('====== FIM FO PROGRAMA =====')
print('Total de pessoas com mais de 18 anos: {}'.format(mais18))
print('Ao todo temos {} homens cadastrados'.format(hcadastrados))
print('E temos {} mulheres com menos de 20 anos '.format(feeminino20))