import random,time
v = 0
print('{:-^100}'.format('\033[33mJogo\033[m-do-\033[31mPAR\033[m-ou-\033[32mIMPAR\033[m'))
escolha = str(input('Quer jogar par ou impar [S/N]? ')).strip().lower()[0]
if escolha == 's':
    print('Então vamos lá!!!!!')
    time.sleep(1)
    while True:
        jogo = ' '
        n = -1
        while jogo not in 'pi':
            jogo = str(input('Quer impar ou par? ')).strip().lower()[0]
        while n not in range (0, 10):
            n = int(input('Escolha um número de 0 a 10 para jogar: '))
        computador = random.randint(0, 10)
        total = n + computador
        if total % 2 == 0:
            totalpi = '\033[31mPAR\033[m'
        else:
            totalpi = '\033[32mIMPAR\033[m'
        print(f'Você jogou {n} e eu joguei {computador}')
        print(f'Isso deu \033[35m{total}\033[m é {totalpi}')
        if jogo == 'p':
            if total % 2 == 0:
                print('Você GANHOU! Não aceito isso vamos de novo!')
                print('-' * 100)
                v += 1
            else:
                print(f'Você PERDEU! Ganhou de mim {v} vezes!')
                print('-' * 100)
                break
        if jogo == 'i':
            if total % 2 == 0:
                print(f'Você PERDEU! Ganhou de mim {v} vezes!')
                print('-' * 100)
                break
            else:
                print('Você GANHOU! Não aceito isso vamos de novo!')
                print('-' * 100)
                v += 1
else:
    print('É uma pena... | \033[34m;\033[31m-\033[34m; \033[m|\033[34m T\033[31m-\033[34mT\033[m |')
