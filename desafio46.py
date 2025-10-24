import time
c = 10
c2 = -1
print('=-'*20)
print('CONTAGEM REGRESSIVA')
print('=-'*20)

for c in range(c, c2, -1):
    if c == 0:
        time.sleep(1)
        print('Hora de estourar os fogos!!!')
    else:
        time.sleep(1)
        print('faltam {} segundos para o estourar dos fogos!'.format(c))