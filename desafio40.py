nota1 = float(input('Qual foi a nota da primeira prova?'))
nota2 = float(input('Qual foi a nota da segunda prova?'))
media = nota1 + nota2
media = media / 2
if media < 5.0:
    print('REPROVADO')
elif media >= 5 and media <= 6.9:
    print('RECUPERAÇÂO')
else:
    print('APROVADO')