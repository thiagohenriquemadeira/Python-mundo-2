import math
n = input('Digite um numero inteiro?')
def eh_real(s):
    try:
        int(s)
        return True
    except ValueError:
        return False
while True:
    if eh_real(n) == True:
        break
    else:
        print('=-'*20)
        print('Você não digitou um número inteiro!!!')
        print('=-'*20)
        n = input('Digite um número inteiro?')
n = int(n) 
def is_primo(number):
    if number < 2:
        return False
    for i in range(2, int(math.sqrt(number)) + 1):
        if number % i == 0:
            return False
    return True
if is_primo(n):
    print(f"{n} é um número primo")
else:
    print(f"{n} não é um número primo")