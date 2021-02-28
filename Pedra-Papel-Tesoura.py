from random import randint
from time import sleep
escolhas = ('Pedra', 'Papel', 'Tesoura')
compputador = randint(0, 2)
print('\033[33m{:=^40}'.format('JOKENPO!!'))
print('\033[mEscolha o que quer jogar:\n'
                    '[ 0 ] Pedra\n'
                    '[ 1 ] Papel\n'
                    '[ 2 ] Tesoura')
jogador = int(input('Opção: '))
print('\033[31mJO')
sleep(1)
print('KEN!')
sleep(0.5)
print('PO!!!')
print('\033[35m~\033[m'*40)
print('Jogador escolheu {}\nComputador escolheu {}'.format(escolhas[jogador],escolhas[compputador]))
print('\033[35m~\033[m'*40)
if jogador == 0:
    if compputador == 0:
        print('EMPATE!!!!')
    elif compputador == 1:
        print('Jogador Ganhou!!!')
    elif compputador == 2:
        print('Computador Ganhou!!!')
    else:
        print('\033[43mJOGADA INVÁLIDA!!!\033[m')
elif jogador == 1:
    if compputador == 0:
        print('EMPATE!!!!')
    elif compputador == 1:
        print('Jogador Ganhou!!!')
    elif compputador == 2:
        print('Computador Ganhou!!!')
    else:
        print('\033[43mJOGADA INVÁLIDA!!!\033[m')
elif jogador == 2:
    if compputador == 0:
        print('EMPATE!!!!')
    elif compputador == 1:
        print('Jogador Ganhou!!!')
    elif compputador == 2:
        print('Computador Ganhou!!!')
    else:
        print('\033[43mJOGADA INVÁLIDA!!!\033[m')
else:
    print('\033[43mJOGADA INVÁLIDA!!!\033[m')