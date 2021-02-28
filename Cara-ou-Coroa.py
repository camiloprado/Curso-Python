import random, time
cont = 0
jogador = 0
while True:
    escolha = str(input('Quer jogar cara ou coroa [S/N]? ')).strip().lower()[0]
    if escolha == 's':
        cont += 1
        print('Flip')
        time.sleep(0.5)
        print('Flip')
        time.sleep(0.5)
        print('Flip')
        time.sleep(0.5)
        print('Tap!')
        time.sleep(0.5)
        moeda = random.randint(1, 2)
        while jogador not in (1 ,2):
            jogador = int(input('Escolha entre:\n'
                      '[ 1 ] Cara\n'
                      '[ 2 ] Coroa\n'
                      'Então? '))
            if jogador > 2:
                print('Digite novamente!')
        print(f'Deu {moeda}')
        if jogador == moeda:
            print(f'Parabéns você ganhou! Com {cont} tentativas.')
            break
        else:
            print('Perdeu, mas não se desanime!')
            time.sleep(1)
    else:
        print('É uma pena...')
        break
