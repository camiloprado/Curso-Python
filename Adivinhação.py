from random import randint
from time import sleep
computador = randint(0 , 10)
print('-o-' * 20)
print('Pense em um numero de 0 a 10')
print('-o-' * 20)
jogador = int(input('Qual o numero sortido? '))
print('Espere meu consagrado...')
sleep(3)
if jogador >= 11 or jogador<= -1:
    print('Jogue o jogo direito!!!')
else:
    if jogador == computador:
        print('Parabens você adivinhou!')
    else:
        print('Buuuu você falhou!\nA resposta era {}'.format(computador))