from random import randint
jogador = ''
tentativas = 0
print('Olá! Sou o Pensador.\nQuer jogar?')
escolha = str(input('Sim ou Não? ')).strip().lower()
if escolha == 'sim' or escolha == 's':
    print('Vamos começar então!')
    computador = randint(0, 10)
    print('Pensei em um número de 0 à 10.')
    jogador = int(input('Qual número você acha que é?'))
    while jogador != computador:
        tentativas += 1
        if jogador > computador:
            jogador = int(input('Está quente, tente um número menor: '))
        else:
            jogador = int(input('Está quente, tente um número maior: '))
else:
    print('Entendo! É uma pena...')
if tentativas == 0:
    print('Você é um gênio por acaso!?')
elif tentativas == 1:
    print('Parabéns!!!!! Você acertou com {} tentativa'.format(tentativas))
else:
    print('Parabéns!!!!! Você acertou com {} tentativas'.format(tentativas))
