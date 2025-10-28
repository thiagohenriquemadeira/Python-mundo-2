nome = []
idade = []
sexo = []
for c in range(0, 4, 1):
    nome.append(str(input('Digite um nome:')))
    idade.append(int(input('Digite a idade do(a) {} :'.format(nome[c]))))
    sexo.append(str(input('Digite o sexo da(o) {} :'.format(nome[c]))))
media = 0
maisvelho = 0
nomemaisvelho = ''
menosde20 = 0
for c in range(0, 4, 1):
    media = media + idade[c]
    if idade[c] > maisvelho:
            if sexo[c] == 'masculino' or sexo[c] == 'Masculino' or sexo[c] == 'MASCULINO':
                nomemaisvelho =  nome[c]
                maisvelho = idade[c]
    if idade[c] < 20:
        if sexo[c] == 'feminino' or sexo[c] == 'Feminino' or sexo[c] == 'FEMININO':
            menosde20 += 1
media = media / 4
print('A media dá idade e {} e o mais velho e o {} e a quantidade de mulheres menores de 20 anos são {}.'.format(media, nomemaisvelho, menosde20))
