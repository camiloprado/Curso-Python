dias = int(input('Quantos dia foram alugados? '))
quilometros = float(input('Quantos Km foram rodados?'))
total = (dias*60)+(quilometros*0.15)
print('O valor a ser pago do aluguel é de R${:.2f}'.format(total))