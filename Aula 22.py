num = int(input('Digite um numero: '))
numero = num % 2
if numero == 0:
    print('O numero {} é PAR'.format(num))
else:
    print('O numero {} é IMPAR'.format(num))