primeirotermo = input('Digite o primeiro termo?')
razao = input('Digite o segundo termo?')
def eh_real(s):
    try:
        float(s)
        return True
    except ValueError:
        return False
print(eh_real(primeirotermo))
print(eh_real(razao))
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
print(primeirotermo)
print(razao)    
c = primeirotermo
c2 = razao
termo10 = primeirotermo + (razao * 9)
print(termo10)