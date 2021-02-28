from time import sleep
while True:
    print('-----------------{}-----------------'.format('Calculadora'))
    operação = int(input('Escolha o tipo de operação:\n'
                         '[ 1 ] Soma\n'
                         '[ 2 ] Subtração\n'                        
                         '[ 3 ] Multiplicação\n'
                         '[ 4 ] Divisão\n'                         
                         '[ 5 ] Sair do programa\n'
                         'Qual a sua escolha: '))
    if (operação == 1):
        print('Você escolheu a soma!')
        n1 = int(input('Digite o valor 1:'))
        n2 = int(input('Digite o valor 2:'))
        resultado = n1 + n2
        print('Resultado da soma de {} e {} = {}'.format(n1, n2, resultado))
        sair = str(input('Quer sair do programa [S/N]? ')).strip().upper()[0]
        if sair == 'S':
            print('Finalizando o programa...')
            sleep(1)
            print('Até mais!!!')
            break
    elif(operação == 2):
        print('Você escolheu a subtração!')
        n1 = int(input('Digite o valor 1:'))
        n2 = int(input('Digite o valor 2:'))
        resultado = n1 - n2
        print('Resultado da subtração de {} e {} = {}'.format(n1, n2, resultado))
        sair = str(input('Quer sair do programa [S/N]? ')).strip().upper()[0]
        if sair == 'S':
            print('Finalizando o programa...')
            sleep(1)
            print('Até mais!!!')
            break
    elif (operação == 3):
        print('Você escolheu a multiplicação!')
        n1 = int(input('Digite o valor 1:'))
        n2 = int(input('Digite o valor 2:'))
        resultado = n1 * n2
        print('Resultado da multiplicação de {} e {} = {}'.format(n1, n2, resultado))
        sair = str(input('Quer sair do programa [S/N]? ')).strip().upper()[0]
        if sair == 'S':
            print('Finalizando o programa...')
            sleep(1)
            print('Até mais!!!')
            break
    elif (operação == 4):
        print('Você escolheu a divisão!')
        n1 = int(input('Digite o valor 1:'))
        n2 = int(input('Digite o valor 2:'))
        resultado = n1 / n2
        print('Resultado da divisão de {} e {} = {}'.format(n1, n2, resultado))
        sair = str(input('Quer sair do programa [S/N]? ')).strip().upper()[0]
        if sair == 'S':
            print('Finalizando o programa...')
            sleep(1)
            print('Até mais!!!')
            break
    elif (operação == 5):
        print('Finalizando o programa...')
        sleep (1)
        print('Até mais!!!')
        break
    else:
        print('Não existe essa operação!')
        sleep(1)
