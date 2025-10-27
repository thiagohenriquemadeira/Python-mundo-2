frase = input('Digite uma frase? ')
frase1 = frase.replace(" ","")
nletras = len(frase1) -1
fraseinvertida = ''
for c in range(nletras, -1, -1):
    fraseinvertida = fraseinvertida + frase1[c]
print('A frase invertida sem espacos ficou "{}" e a original  sem espacos (para a melhor avalicao) ficou "{}"'.format(fraseinvertida, frase1))
if fraseinvertida == frase1:
    print('A frase "{}" e um palindromo!'.format(frase))
else:
    print('A frase "{}" não e um polindromo!'.format(frase))