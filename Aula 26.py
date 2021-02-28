num = int(input('Digite um valor inteiro:\n'))
print('Escolha entre essas 3 opções de transformação:\n'
      '[ 1 ] Binário\n'
      '[ 2 ] Octal\n'
      '[ 3 ] Hexadecimal')
escolha = int(input('Digite sua escolha: '))
if escolha == 1:
    print('O numero {} para BINÁRIO é {}'.format(num,bin(num)[2:]))
elif escolha == 2:
    print('O numero {} para OCTAL é {}'.format(num, oct(num)[2:]))
elif escolha == 3:
    print('O numero {} para HEXADECIMAL é {}'.format(num,hex(num)[2:]))
else:
    print('Fora das opções!!!')