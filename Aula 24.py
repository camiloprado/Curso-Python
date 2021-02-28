salario = float(input('Digite o seu sálario: R$'))
if (salario <= 947):
    sf = salario * 0.15 + salario
    print('O salário atual é de R${:.2f}'.format(sf))
elif (salario > 947 and salario <= 2000):
    sf = salario * 0.1 + salario
    print('O salário atual é de R${:.2f}'.format(sf))
elif (salario > 2000 and salario <= 5000):
    sf = salario * 0.05 + salario
    print('O salário atual é de R${:.2f}'.format(sf))
elif (salario > 5000):
    print('O sálario continuara sendo R${:.2f}'.format(salario))
