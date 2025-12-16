valorcasa = float(input('valor da casa? '))
salario = float(input('valor do seu salario? '))
tempo = int(input('quantos anos você quer parcelar? '))
meses = tempo * 12
imprestimo = valorcasa / meses
n30 = (30 / 100) * salario
if imprestimo < n30:
    print('Foi aprovado o imprestimo você pagara R${:.2f} ao mês por {} anos.'. format(imprestimo, tempo))
else:
    print('imfelizmente não foi aprovado')