print('-='*20)
print('Analizador de Triângulo')
print('-='*20)
r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos acima PODEM FORMAR UM TRIÂNGULO!')
else:
    print('Os segmentos acima NÃO PODEM FORMAR UM TRIÂNGULO!')
if r1 == r2 and r2 == r3:
    print('Os segmentos acima PODEM FORMAR UM EQUILÁTERO!')
else:
    print('Os segmentos acima NÃO PODEM FORMAR UM EQUILÁTERO')
if r1 == r2 or r1 == r3 or r2 == r3:
    print('Os segmentos acima PODEM FORMAR UM ISÓSCELES')
else:
    print('Os segmentos acima NÃO PODEM FORMAR UM ISÓSCELES')
if r1 != r2 and r1 != r3 and r2 != r3:
    print('Os segmentos acima PODEM FORMAR UM ESCALENO')
else:
    print('Os segmentos acima NÃO PODEM FORMAR UM ESCALENO')
    