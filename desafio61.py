primeirotermo = input('Digite o primeiro termo?')
razao = input('Digite o segundo termo?')
def eh_real(s):
    try:
        float(s)
        return True
    except ValueError:
        return False
while True:
    if eh_real(primeirotermo) == True and eh_real(razao) == True:
        break
    else:
        print('=-'*20)
        print('O primeiro e o segundo termo não são números reais')
        print('=-'*20)
        primeirotermo = input('Digite o primeiro termo?')
        razao = input('Digite o segundo termo?')
primeirotermo = float(primeirotermo)
razao = float(razao) 
cont = 1 
termo = primeirotermo  
c = 10
soma = 10 
c1 = 0
while cont <= c or c != 0:
    print('{} '.format(termo), end='')
    termo += razao
    cont += 1
    if cont == c:
        print('{} '.format(termo), end='')
        print('PAUSA')
        c1 = int(input('Quantos termos você quer mostrar (ou digite 0 para parar):'))
        c += c1
        soma = c
        if c1 == 0:
            c = 0
print('Progressão finalizada com {} termos mostrados.'.format(soma))