from time import sleep
dados = list()
registro = list()
while True:
    opcao = ' '
    while opcao not in (1, 2, 3, 4):
        print('\033[33m{:-^80}\033[m'.format('Menu'))
        opcao = int(input('Escolha uma das opções:\n'
                          '[ 1 ] Cadastro\n'
                          '[ 2 ] Exclusão\n'
                          '[ 3 ] Lista dos Cadastrados\n'
                          '[ 4 ] Sair\n'
                          'Escolha: '))
    print('\033[33m-\033[m' * 80)
    if opcao == 1:
        while True:
            nome = str(input('Digite o nome completo: ')).strip().upper()
            cpf = int(input('Digite o CPF: '))
            idade = int(input('Digite a idade: '))
            print('Seu nome é: {}.'
                  ' Com o seguinte CPF: {}.'
                  ' E tem {} anos.'.format(nome.upper(), cpf, idade))
            sleep(0.5)
            afirmação = ' '
            while afirmação not in 'sn':
                afirmação = str(input('Correto? ')).strip().lower()[0]
            if afirmação == 's':
                dados.append(nome)
                dados.append(cpf)
                dados.append(idade)
                registro.append(dados[:])
                dados.clear()
                print('\033[32mEsta salvo!\033[m')
                sleep(1)
                break
            elif afirmação == 'n':
                print('Digite novamente!')
                sleep(0.5)
    if opcao == 2:
        while True:
            apagar = str(input('Qual nome deseja apagar? ')).upper().strip()
            if apagar in registro[:][0]:
                registro.pop(registro.index(apagar))
                print('Apagado!')
                break
            else:
                print('Digite novamente!')
    if opcao == 3:
        print('|{:^20}|{:^20}|{:^20}|'.format('Nome', 'CPF', 'Idade'))
        print('-' * 64)
        for pos in registro:
            print(f'|{pos[0]:^20}|{pos[1]:^20}|{pos[2]:^20}|')
            print('-' * 64)
    if opcao == 4:
        print('Finalizando o programa! Espere um momento.')
        sleep(0.5)
        print('\033[33m.')
        sleep(0.5)
        print('.')
        sleep(0.5)
        print('.')
        sleep(1)
        print('\033[31mFinalizado!!!\033[m')
        break
