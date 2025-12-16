from datetime import date
ano = int(input('Digite o ano que você naceu:'))
contador = 0
hoje = date.today().year
idade = (hoje - ano)  
idade2 = idade
print('Quem nsceu em {} tem {} em 2025'.format(ano, idade))
while True:
    if idade2 > 18:
        idade2 -= 1
        contador += 1
    if idade2 == 18:
        break
    if idade2 < 18:
        idade2 += 1
        contador += 1
if idade > 18:
    print('Você já deveria ter se alistado há {} anos.'.format(contador))
    print('Seu alistamento foi em {}'.format(hoje - contador))
elif idade == 18:
    print('Você tem que se alistar IMEDIATAMENTE!')
else:
    print('Ainda faltam {} anos para o alistamento'.format(contador))
    print('Seu alistamento será em {}'.format(hoje + contador))