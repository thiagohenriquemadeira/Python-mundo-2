peso = float(input('Digite seu peso? '))
altura = float(input('Digite sua altura? '))
imc = peso / (altura * altura)
print('{:.2f}'.format(imc))
if imc < 18.5:
    print('Você esta abaixo do peso e seu imc é {:.2f}'.format(imc))
elif imc >= 18.5 and imc < 25:
    print('Peso ideal é seu imc é {:.2f}'.format(imc)) 
elif imc >= 25 and imc < 30:
    print('Sobrepeso é seu imc é {:.2f}'.format(imc))
elif imc >= 30 and imc <= 40:
    print('Obesidade é seu imc é {:.2f}'.format(imc))
else:
    print('Obesidade mórbida é seu imc {:.2f}'.format(imc))