n = 0
resultado = 0
print('PROGRAMA TABUADA ENCERRADA')
while True:
    print('~~' * 20)
    n = int(input('Você quer ver a tabuada de qual valor[Sé quiser encerrar o programa digite um número negativo]?'))
    print('~~' * 20)
    if n < 0:
        print('PROGRAMA TABUADA ENCERRADO. Volte sempre!')
        break
    else:
        for c in range(1, 11, 1):
            resultado = n * c
            print('{} x {} = {}'.format(n, c, resultado))
    