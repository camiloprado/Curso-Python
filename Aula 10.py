salario = float(input('Digite o sálario do funcionário: R$'))
aumento = float(input('Digite a % do aumento do sálario:'))
print('Do sálario de R${:.2f} com {:.0f}% foi para R${:.2f}'.format(salario, aumento, salario+(salario*aumento/100)))