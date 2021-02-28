from utiliades import moeda, dados
while True:
    escolha = str(input('Quer começar a teoria [S/N]? ')).strip().lower()[0]
    if escolha in 'sn':
        break
if escolha == 's':
    print('Inutilizei os módulos dessa parte!')
    #from utiliades import moeda
    #num = int(input('Digite um valor: '))
    #fat = numeros.fatorial(num)
    #print(f'O fatorial de {num} é {fat}')
    #print(f'O dobro de {num} é {numeros.dobro(num)}')
    #print(f'O triplo de {num} é {numeros.triplo(num)}')
    for f in range(0, 14):
        print(dados.cor(f))
        print('Teste')
        print(dados.cor(0))
while True:
    ex107 = str(input('Quer começar o ex107 [S/N]? ')).strip().lower()[0]
    if ex107 in 'sn':
        break
if ex107 == 's':
    while True:
        form = str(input('Quer formatado [S/N]? ')).strip().lower()[0]
        if form in 'sn':
            break
    if form == 's':
        mo = format=True
    else:
        mo = format=False
    p = dados.leiadinheiro('Digite o preço: ')
    au = int(input('Qual a porcentagem a ser aumentado? '))
    re = int(input('Qual a porcentagem a ser reduzido? '))
    moeda.resumo(p, au, re, mo)
