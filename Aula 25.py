casa = float(input('Digite o valor da casa: R$ '))
salario = float(input('Digite o seu salário: R$ '))
anos = int(input('Digite em quantos anos irá pagar: '))
prestação = casa/(anos*12)
minimo = salario*(30/100)
print('Para uma casa de R${:.2f} em {} anos terá uma prestação de R${:.2f}'.format(casa, anos, prestação))
if prestação >= minimo:
    print('Emprestimo Negado!')
else:
    print('Emprestimo Aceito!')