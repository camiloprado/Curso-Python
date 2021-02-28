escolha = str(input('Quer começar [S/N]? ')).strip().lower()[0]
if escolha == 's':
    i = 0
    sexo = str(input('Por favor digite o seu sexo [M/F]: ')).strip().upper()
    while sexo not in 'MF':
        sexo = str(input('Por favor, informe o seu sexo [M/F]: ')).strip().upper()
        i += 1
        if i == 4:
            sexo = str(input('Por favor!!!!!!!!!!!!!!!!!!, informe o seu sexo [M/F]: ')).strip().upper()
    print('Obrigado por informar!')
print('\033[33m-\033[m'*200)
escolha = str(input('Quer começar [S/N]? ')).strip().lower()[0]
if escolha == 's':
    n = int(input('Digite um número para calcular o seu fatorial: '))
    c = n
    f = 1
    print('Calculando {}! = '.format(n),end='')
    while c > 0:
        print('{}'.format(c), end='')
        print(' x ' if c > 1 else ' = ', end='')
        f *= c
        c -= 1
    print('{}'.format(f))
print('\033[33m-\033[m'*200)
escolha = str(input('Quer começar [S/N]? ')).strip().lower()[0]
if escolha == 's':
    n = cont = soma = 0
    while True:
        n = int(input('Digite um número [999 para parar]: '))
        if n == 999:
            break
        cont += 1
        soma += n
    print('Você digitou {} com um total de {}!'.format(cont, soma))
print('\033[33m-\033[m'*200)
n = cont = soma = escolha = maior = menor = 0
escolha = str(input('Quer começar [S/N]: ')).strip().lower()[0]
if escolha == 's':
    while escolha in 's':
        n = int(input('Digite um número: '))
        cont += 1
        soma += n
        if cont == 1:
            maior = menor = n
        else:
            if n >= maior:
                maior = n
            if n <= menor:
                menor = n
        escolha = str(input('Quer continuar [S/N]: ')).strip().lower()[0]
if escolha == 'n':
    print('Obrigado!')
print('Você digitou {} com um total de {} e média de {:.2f}!'.format(cont, soma, (soma / 2)))
print('O maior número é {} e o menor {}.'.format(maior, menor))
print('\033[33m-\033[m'*200)
contidade = 0
conth = 0
contm = 0
conttotal = 0
escolha = str(input('Quer começar [S/N]? ')).strip().lower()[0]
if escolha == 's':
    while True:
        print('~' * 200)
        sexo = ' '
        pergunta = ' '
        nome = str(input('Digite seu nome:')).strip().upper()[0]
        idade = int(input('Digite sua idade: '))
        if idade >= 18:
            contidade += 1
        while sexo not in 'mfn':
            sexo = str(input('Digite seu sexo [M/F/NÃO ESPECIFICAR]: ')).strip().lower()[0]
        if sexo == 'm':
            conth += 1
        if sexo == 'f' and idade <= 20:
            contm += 1
        conttotal += 1
        print('Cadastrado!')
        while pergunta not in 'sn':
            pergunta = str(input('Quer continuar [S/N]? ')).strip().lower()[0]
        if pergunta == 'n':
            print(f'Foi cadastrado {conttotal} pessoas! Entre os {conttotal} tem:\n'
                      f'{contidade} maiores de 18 anos.\n'
                      f'{conth} homens.\n'
                      f'{contm} mulheres com menos de 20 anos.')
            break
else:
    print('Entendido!')
print('\033[33m-\033[m'*200)
escolha = str(input('Quer começar [S/N]? ')).strip().lower()[0]
if escolha == 's':
    total = maiorq = cont = mpreco = 0
    barato = ' '
    while True:
        nome = str(input('Digite o nome do produto: ')).strip().upper()
        preco = float(input('Digite o preço do produto: '))
        total += preco
        cont += 1
        if preco > 1000:
            maiorq += 1
        if cont == 1 or preco < mpreco:
            mpreco = preco
            barato = nome
        pergunta = ' '
        while pergunta not in 'sn':
            pergunta = str(input('Quer continuar [S/N]? ')).strip().lower()[0]
        if pergunta == 'n':
            break
    print(f'O total das compras foi de \033[33mR${total:.2f}\033[m')
    print(f'\033[33m{maiorq}\033[m custam mais de R$1000.00')
    print(f'O produto mais barato é o/a \033[33m{barato}\033[m que custa \033[33mR${mpreco:.2f}\033[m')
