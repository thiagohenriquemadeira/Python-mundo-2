n = []
c = cont = 0
soma = 0
while True:
    n.append(int(input('Digite um valor (999 para parar):')))
    if n[c] == 999:
        break
    soma += n[c]
    c += 1
    cont += 1
print(f'A soma dos ({cont}) valores foi {soma}!')
