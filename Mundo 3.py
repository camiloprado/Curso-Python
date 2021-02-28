def desafio():
    print('\033[33m{:-^90}\033[m'.format('\033[31mDESAFIOS\033[33m'))


def linha():
    print('-' * 80)


print(f'{"COMEÇOU":-^80}')
tupla = ' '
while tupla not in 'sn':
    tupla = str(input('Quer começar a TUPLA [S/N]? ')).strip().lower()[0]
    if tupla == 's':
        teoria = ' '
        while teoria not in 'sn':
            teoria = str(input('Quer começar a teoria [S/N]? ')).strip().lower()[0]
            if teoria == 's':
                #TUPLAS SÃO IMUTÁVEIS E SÃO DENOMINADAS POR ()
                lanche = ('Hamburguer', 'Suco', 'Pizza', 'Pudim')
                print(lanche)
                print(lanche[0])
                print(lanche[1])
                print(lanche[2])
                print(lanche[3])
                print(lanche[-1])
                print(lanche[-2])
                print(lanche[-3])
                print(lanche[-4])
                for comida in lanche:
                    print(f'Eu estou com vontade de comer \033[33m{comida}\033[m')
                print('Pouca coisa!')
                for comida in range (0, len(lanche)):
                    print(f'Eu estou com vontade de comer \033[33m{lanche[comida]}\033[m na posição {comida}')
                print('Pouca coisa!')
                for pos, comida in enumerate(lanche):
                    print(f'Eu estou com vontade de comer \033[33m{comida}\033[m na posição {pos}')
                a = (1, 2, 3, 4)
                b = (5, 6, 7, 8, 9, 10)
                c = a + b
                d = a, b
                print(c)
                print(d)
        desafio()
        escolha = ' '
        while escolha not in 'sn':
            escolha = str(input('Quer começar [S/N]: ')).strip().lower()[0]
            if escolha == 's':
                num = ('ZERO', 'UM', 'DOIS', 'TRÊS', 'QUATRO', 'CINCO', 'SEIS', 'SETE', 'OITO', 'NOVE', 'DEZ', 'ONZE', 'DOZE', 'TREZE'
                       , 'QUATORZE', 'QUINZE', 'DEZESSEIS', 'DEZESSETE', 'DEZOITO', 'DEZENOVE', 'VINTE')
                while True:
                    numero = int(input('Digite um número de 0 a 20: '))
                    if 0<= numero <= 20:
                        print(f'Você digitou o número {num[numero]}')
                    continuar = ' '
                    while continuar not in 'sn':
                        continuar = str(input('Quer continuar [S/N]: ')).strip().lower()
                    if continuar == 'n':
                        break
        escolha = ' '
        while escolha not in 'sn':
            escolha = str(input('Quer começar [S/N]: ')).strip().lower()[0]
            if escolha == 's':
                times = ('Internacional', 'Flamengo', 'São Paulo', 'Atlético-MG', 'Palmeiras', 'Grêmio', 'Fluminense', 'Ceará', 'Corinthias', 'Santos', 'Bragantino', 'Athletico-PR', 'Atlético-GO', 'Vasco', 'Sport', 'Bahia', 'Fortaleza', 'Goiás', 'Coritiba', 'Botafogo')
                print('{: ^100}'.format('TIMES DO BRASILEIRÂO - 30/01/2021'))
                print('-=' * 50)
                print(f'Times classificados: {times}')
                print('-=' * 50)
                print(f'Os 5 primeiros colocados são {times[0:5]}')
                print('-=' * 50)
                print(f'Os 4 ultimos colocados são {times[-4:]}')
                print('-=' * 50)
                print(f'Os times em ordem Alfabética: {sorted(times)}')
                print('-=' * 50)
                print('O São Paulo está em {}° colocado.'.format(times.index('São Paulo')+1))
        escolha = ' '
        while escolha not in 'sn':
            escolha = str(input('Quer começar [S/N]: ')).strip().lower()[0]
            import random
            if escolha == 's':
                A = random.randint(1, 10)
                B = random.randint(1, 10)
                C = random.randint(1, 10)
                D = random.randint(1, 10)
                E = random.randint(1, 10)
                num = (A, B, C, D, E)
                maior = max(num)
                menor = min(num)
                if A > B >= C >= D >= E > maior:
                    maior = A
                elif B > B > C > D > E > maior:
                    maior = B
                print(f'Os seguintes numero foram sorteados : {num}')
                print(f'O maior número é {maior}')
                print(f'O menor número é {menor}')
        escolha = ' '
        while escolha not in 'sn':
            escolha = str(input('Quer começar [S/N]: ')).strip().lower()[0]
        if escolha == 's':
            a = int(input('Digite o 1° valor: '))
            b = int(input('Digite o 2° valor: '))
            c = int(input('Digite o 3° valor: '))
            d = int(input('Digite o 4° valor: '))
            num = (a, b, c, d)
            print(f'Você digitou os seguintes números: {num}')
            if num.count(9) == 1:
                print(f'O número 9 aparece 1 vez')
            elif num.count(9) > 1:
                print(f'O número 9 aparece {num.count(9)} vezes')
            if 3 in num:
                print(f'O número 3 aparece na {num.index(3) + 1}° posição')
            else:
                print('O valor 3 não foi digitado!')
            print('Os números pares foram ', end='')
            for n in num:
                if n % 2 == 0:
                    print(n, end = ' ')
                print('!')
        escolha = ' '
        while escolha not in 'sn':
            escolha = str(input('Quer começar [S/N]: ')).strip().lower()[0]
        if escolha == 's':
            lista = ('Lápis', 1.75, 'Borracha', 2.00, 'Caderno', 15.90, 'Estojo', 25.00, 'Transferidor', 4.20, 'Compasso', 9.99
                     , 'Mochila', 120.32, 'Caneta', 22.30, 'Livro', 34.90)
            print(f'|{"-" * 69}|')
            print('|{:' '^69}|'.format('LISTA DE PRODUTOS'))
            print(f'|{"-" * 69}|')
            for pos in range(0, len(lista)):
                if pos % 2 == 0:
                    print(f'|{lista[pos]:.<60}', end='')
                else:
                    print(f'R${lista[pos]:>7.2f}|')
            print(f'|{"-" * 69}|')
        escolha = ' '
        while escolha not in 'sn':
            escolha = str(input('Quer começar [S/N]: ')).strip().lower()[0]
        if escolha == 's':
            palavras = ('APRENDER', 'ESTUDAR', 'PROGRAMAR', 'COZINHAR', 'JOGAR', 'CORRER', 'ONIBUS')
            for i in palavras:
                print(f'\nNa palavra {i.upper()} tem', end= ' ')
                for vogais in i:
                    if vogais.lower() in 'aeiou':
                        print(vogais.lower(), end=' ')
linha()
listas = ' '
while listas not in 'sn':
    listas = str(input('Quer começar a LISTAS [S/N]? ')).strip().lower()[0]
    if listas == 's':
        teoria = ' '
        while teoria not in 'sn':
            teoria = str(input('Quer começar a teoria [S/N]? ')).strip().lower()[0]
            if teoria == 's':
                num = [2, 3, 9, 1]
                print(num)
                num[2] = 6
                print(num)
                num.append(7)
                print(num)
                num.sort()
                print(num)
                num.sort(reverse=True)
                print(num)
                num.insert(2, 6)
                print(num)
                num.pop(2) #Se deixar sem nada, elimina o ultimo elemento.
                print(num)
                if 5 in num: #Se não tiver o número dentro ira dar erro!!!
                    num.remove(5)
                else:
                    print('Não existe o número 5')
                print(num)
                print(f'Essa lista tem {len(num)} elementos.')
                valores = list() #Ou valores = []
                valor = list()
                valores.append(4)
                valores.append(7)
                valores.append(1)
                for v in valores:
                    print(f'{v}...', end='')
                print('!')
                for c, v in enumerate(valores):
                    print(f'Entrei o valor {v} na posição {c} dentro da lista!')
                print('Cheguei ao final da lista!')
                teste = list()
                teste.append('Camilo')
                teste.append(22)
                galera = list()
                galera.append(teste[:])
                print(galera)
                quer = str(input('Quer? '))
                if quer == 's':
                    for cont in range(0, 5):
                        valor.append(int(input('Digite um valor: ')))
                    print(valor)
                a = [3, 4, 7, 6]
                b = a
                print(f'Valores de A: {a}')
                print(f'Valores de B: {b}')
                b[2] = 5
                print(f'Valores de A: {a}')
                print(f'Valores de B: {b}')
                a = [1, 2, 3, 4, 5]
                b = a[:]
                b[3] = 9
                print(f'Valores de A: {a}')
                print(f'Valores de B: {b}')

        desafio()
        escolha = ' '
        while escolha not in 'sn':
            escolha = str(input('Quer começar [S/N]: ')).strip().lower()[0]
        if escolha == 's':
            listanum = list()
            maior = menor = 0
            for c in range(0, 5):
                listanum.append(int(input(f'Digite um valor para a posição {c}: ')))
                if c == 0:
                    maior = menor = listanum[c]
                else:
                    if listanum[c] > maior:
                        maior = listanum[c]
                    if listanum[c] < menor:
                        menor = listanum[c]
            print('-=' * 40)
            print(f'Você digitou os valores: {listanum}')
            print(f'O maior valor é {maior} nas posições ', end='')
            for i, v in enumerate(listanum):
                if v == maior:
                    print(f'{i}...',end='')
            print(f'\nO menor valor é {menor} nas posições ', end='')
            for i, v in enumerate(listanum):
                if v == menor:
                    print(f'{i}...',end='')
            print()
        escolha = ' '
        while escolha not in 'sn':
            escolha = str(input('Quer começar [S/N]: ')).strip().lower()[0]
        if escolha == 's':
            n = list()
            while True:
                c = int(input(f'Digite um número: '))
                if c not in n:
                    n.append(c)
                    print('Número adicionado')
                else:
                    print('Número já existente, não adicionado!')
                opcao = ' '
                while opcao not in 'sn':
                    opcao = str(input('Quer continuar [S/N]? ')).strip().lower()[0]
                if opcao == 'n':
                    break
            n.sort()
            print(f'Você digitou os seguintes números {n}')
        escolha = ' '
        while escolha not in 'sn':
            escolha = str(input('Quer começar [S/N]: ')).strip().lower()[0]
        if escolha == 's':
            valor = list()
            for c in range (0, 5):
                n = int(input('Digite um valor: '))
                if c == 0 or n > valor[-1]:
                    valor.append(n)
                    print('Inserido no final da lista!')
                else:
                    pos = 0
                    while pos < len(valor):
                        if n <= valor[pos]:
                            valor.insert(pos, n)
                            print(f'Adicionado na posição {pos}')
                            break
                        pos += 1
            print('~' * 80)
            print(f'Os valores digitados são: {valor}')
        escolha = ' '
        while escolha not in 'sn':
            escolha = str(input('Quer começar [S/N]: ')).strip().lower()[0]
        if escolha == 's':
            n = list()
            while True:
                n.append(int(input('Digite um valor: ')))
                opcao = ' '
                while opcao not in 'sn':
                    opcao = str(input('Quer continuar [S/N]? ')).lower().strip()[0]
                if opcao == 'n':
                        break
            print(f'Foram digitados {len(n)} valores')
            n.sort(reverse=True)
            print(f'Com os seguintes valores digitados {n}')
            if 5 in n:
                print(f'O valor 5 foi digitado e está na {n.index(5)+1}° posição ')
            else:
                print('O valor 5 não foi digitado!')
        escolha = ' '
        while escolha not in 'sn':
            escolha = str(input('Quer começar [S/N]: ')).strip().lower()[0]
        if escolha == 's':
            lista = list()
            pares = list()
            impares = list()
            while True:
                lista.append(int(input('Digite um valor: ')))
                opcao = ' '
                while opcao not in 'sn':
                    opcao = str(input('Quer continuar [S/N]? ')).lower().strip()[0]
                if opcao == 'n':
                    break
            for c in lista:
                if c % 2 == 0:
                    pares.append(c)
                else:
                    impares.append(c)
            print('-=' * 80)
            print(f'Os valores da lista é {lista}')
            if len(pares) == 0:
                print('Foram digitado 0 valores pares!')
            else:
                print(f'Os valores pares da lista é ', end='')
                for d in pares:
                    print(f'{d}', end='...')
            if len(impares) == 0:
                print('\nForam digitado 0 valores impares!')
            else:
                print(f'\nOs valores impares da lista é ',end='')
                for e in impares:
                    print(f'{e}', end='...')
        escolha = ' '
        while escolha not in 'sn':
            escolha = str(input('Quer começar [S/N]: ')).strip().lower()[0]
        if escolha == 's':
            plano = list()
            expresao = str(input('Digite uma expressão matemática: '))
            for parentese in expresao:
                if parentese == '(':
                    plano.append('(')
                elif parentese == ')':
                    if len(plano) > 0:
                        plano.pop()
                    else:
                        plano.append(')')
                        break
            if len(plano) == 0:
                print('Expressão Aceita!')
            else:
                print('Expressão Inválida')
        escolha = ' '
        while escolha not in 'sn':
            escolha = str(input('Quer começar [S/N]: ')).strip().lower()[0]
        if escolha == 's':
            maior = menor = 0
            temporario = list()
            principal = list()
            while True:
                temporario.append(str(input('Digite o nome: ')).strip().upper())
                temporario.append(float(input('Digite o peso: ')))
                if len(principal) == 0:
                    maior = menor = temporario[1]
                else:
                    if temporario[1] > maior:
                        maior = temporario[1]
                    if temporario[1] < menor:
                        menor = temporario [1]
                principal.append(temporario[:])
                temporario.clear()
                opcao = ' '
                while opcao not in 'sn':
                    opcao = str(input('Quer continuar [S/N]? '))
                if opcao == 'n':
                    break
            print(f'Foram cadastradas o total de {len(principal)} pessoas')
            print(f'O maior peso foi de {maior:.2f}Kg. Pertence à ', end='')
            for pessoa in principal:
                if pessoa[1] == maior:
                    print(f'[{pessoa[0]}]', end=' ')
            print(f'\nO menor peso foi de {menor:.2f}Kg. Pertence à ', end='')
            for pessoa in principal:
                if pessoa[1] == menor:
                    print(f'[{pessoa[0]}]', end=' ')
            print()
        escolha = ' '
        while escolha not in 'sn':
            escolha = str(input('Quer começar [S/N]: ')).strip().lower()[0]
        if escolha == 's':
            num = list()
            for lista in range(0, 7):
                num.append(int(input(f'Digite o {lista + 1}° valor: ')))
            print(f'Os valores digitados são {num}')
            pares = list()
            impares = list()
            for v in num:
                if v % 2 == 0:
                    pares.append(v)
            pares.sort()
            print(f'Os valores pares são {pares}')
            for c in num:
                if c % 2 == 1:
                    impares.append(c)
            impares.sort()
            print(f'Os valores impares são {impares}')
            #Outra maneira
            #num = [[], []]
            #valor = 0
            #for c in range (1, 8):
                #if valor % 2 == 0:
                    #num[0].append(valor)
                #else:
                    #num[1].append(valor)
            #num[0].sort()
            #num[1].sort()
            #print(f'Os valores pares são {num[0]}')
            #print(f'Os valores impares são {num[1]}')
        escolha = ' '
        while escolha not in 'sn':
            escolha = str(input('Quer começar [S/N]: ')).strip().lower()[0]
        if escolha == 's':
            matriz = list()
            pares = 0
            mvalor = 0
            for i in range (1, 10):
                matriz.append(int(input(f'Digite o {i}° valor: ')))
            print(f'[{matriz[0]:^5}] [{matriz[1]:^5}] [{matriz[2]:^5}]\n'
                  f'[{matriz[3]:^5}] [{matriz[4]:^5}] [{matriz[5]:^5}]\n'
                  f'[{matriz[6]:^5}] [{matriz[7]:^5}] [{matriz[8]:^5}]')
            for p in matriz:
                if p % 2 == 0:
                    pares += p
            print(f'A soma dos valores pares são: {pares}')
            terceira = matriz[2] + matriz[5] + matriz[8]
            print(f'A soma dos valores da 3° COLUNA é: {terceira}')
            if matriz[3] >= matriz [4] and matriz[3] >= matriz [5] :
                mvalor = matriz[3]
            if matriz[4] >= matriz [3] and matriz[4] >= matriz [5] :
                mvalor = matriz[4]
            if matriz[5] >= matriz [4] and matriz[5] >= matriz [3] :
                mvalor = matriz[5]
            print(f'O maior valor da 2° LINHA é {mvalor}')
            #matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
            #spar = mai = scol = 0
            #for l in range(1, 4):
                #for c in range(1, 4):
                    #matriz[l][c] = int(input(f'Digite um valorpara [{l}, {c}]: '))
            #print('-=' * 80)
            #for l in range(1, 4):
                #for c in range(1, 4):
                    #print(f'[{matriz[l][c]:^5}]', end='')
                    #if matriz[l][c] % 2 == 0:
                        #spar += matriz[l][c]
                #print()
            #print('-='* 80)
            #print(f'A soma dos valores pares são: {spar}')
            #for l in range (1, 4):
                #scol += matriz[l][2]
            #print(f'A soma dos valores da 3° COLUNA é: {scol}')
            #for c  in range (1, 4):
                #if c == 0 or matriz[1][c] > mai:
                    #mai = matriz[1][c]:
            #print(f'O maior valor da 2° LINHA é {mai}')
        escolha = ' '
        while escolha not in 'sn':
            escolha = str(input('Quer começar [S/N]: ')).strip().lower()[0]
        if escolha == 's':
            from random import randint
            from time import sleep
            numeros = list()
            print(f'{"JOGO DA MEGASENA":-^50}')
            jogos = int(input('Quantos jogos irá querer jogar na MEGA SENA? '))
            print(f'{f"GERANDO {jogos} jOGOS":-^50}')
            for j in range (0, jogos):
                for i in range (0, 6):
                    numeros.append(randint(1, 60))
                numeros.sort()
                print(f'Jogo {j + 1}: {numeros}')
                numeros.clear()
                sleep(0.5)
            print(f'{"< BOA SORTE >":-^50}')
        escolha = ' '
        while escolha not in 'sn':
            escolha = str(input('Quer começar [S/N]: ')).strip().lower()[0]
        if escolha == 's':
            lista = list()
            while True:
                nome = str(input('Digite o nome do aluno: '))
                n1 = float(input('Digite a 1° Nota: '))
                n2 = float(input('Digite a 2° Nota: '))
                media = (n1 + n2)/2
                lista.append([nome, [n1, n2], media])
                opcao = ' '
                while opcao not in 'sn':
                    opcao = str(input('Quer continuar [S/N]? ')).strip().lower()[0]
                if opcao == 'n':
                    break
            print('-=' * 30)
            print(f'{"No.":<4}{"NOME":<10}{"MÉDIA":>8}')
            print('-' * 26)
            for i, a in enumerate(lista):
                print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')
            while True:
                print('-' * 35)
                opc = int(input('Digite o indice do aluno para ver a nota (999 Para): '))
                if opc == 999:
                    print('FINALIZANDO...')
                    break
                if opc <= len(lista) - 1:
                    print(f'As notas do aluno {lista[opc][0]} são {lista[opc][1]}')
linha()
dicionario = ' '
while dicionario not in 'sn':
    dicionario = str(input('Quer começar o DICIONÁRIO [S/N]? ')).strip().lower()[0]
    if dicionario == 's':
        teoria = ' '
        while teoria not in 'sn':
            teoria = str(input('Quer começar a teoria [S/N]? ')).strip().lower()[0]
            if teoria == 's':
                pessoa = {'nome': 'Camilo', 'idade': 22, 'sexo': 'M'}
                print(pessoa)
                print(pessoa['nome'])
                print(pessoa['idade'])
                print(pessoa['sexo'])
                print(f'A pessoa chamada {pessoa["nome"]} do sexo {pessoa["sexo"]} tem {pessoa["idade"]} anos')
                print(pessoa.keys())
                print(pessoa.values())
                print(pessoa.items())
                for k, v in pessoa.items():
                    print(f'{k} = {v}')
                del pessoa['sexo']
                pessoa['nome'] = 'Pedro'
                pessoa['Peso'] = 66
                for k, v in pessoa.items():
                    print(f'{k} = {v}')
                brasil = list()
                estado1 = {'UF': 'São Paulo', 'Sigla': 'SP'}
                estado2 = {'UF': 'Rio de Janeiro', 'Sigla': 'RJ'}
                brasil.append(estado1)
                brasil.append(estado2)
                print(brasil[0])
                print(brasil[0]['UF'])
                print(brasil[0]['Sigla'])
                print(brasil[1])
                print(brasil[1]['UF'])
                print(brasil[1]['Sigla'])
                estado = dict()
                for c in range(0, 3):
                    estado['UF'] = str(input('Unidade Federativa: '))
                    estado['Sigla'] = str(input('Sigla do Estado: '))
                    brasil.append(estado.copy())
                for e in brasil:
                    for k, v in e.items():
                        print(f'O campo {k} tem valor {v}')
        desafio()
        escolha = ' '
        while escolha not in 'sn':
            escolha = str(input('Quer começar [S/N]: ')).strip().lower()[0]
        if escolha == 's':
            alunos = dict()
            alunos['Nome'] = str(input('Digite o nome do aluno: '))
            alunos['Média'] = float(input(f'Digite a média de {alunos["Nome"]}: '))
            if alunos['Média'] >= 7:
                alunos['Situação'] = '\033[32mAprovado\033[m'
            elif 5 <= alunos['Média'] < 7:
                alunos['Situação'] = '\033[33mRecuperação\033[m'
            else:
                alunos['Situação'] = '\033[31mReprovado\033[m'
            print('-=' * 40)
            for k, v in alunos.items():
                print(f' - {k}: {v}')
        escolha = ' '
        while escolha not in 'sn':
            escolha = str(input('Quer começar [S/N]: ')).strip().lower()[0]
        if escolha == 's':
            from random import randint
            from time import sleep
            from operator import itemgetter
            jogadores = dict()
            vez = list()
            for dado in range (1, 5):
                jogadores[f'Jogador{dado}'] = randint(1, 6)
            print(f'{"JOGANDO OS DADOS":-^80}')
            for k, v in jogadores.items():
                print(f'O {k} tirou {v} no dado.')
                sleep(0.5)
            vez = sorted(jogadores.items(), key=itemgetter(1), reverse=True)
            print('-=' * 40)
            print(f'{"ORDEM DE QUEM COMEÇA":^80}')
            print('-=' * 40)
            for i, v in enumerate(vez):
                print(f'{i+1}° lugar: {v[0]} com {v[1]}.')
                sleep(0.5)
            print('-=' * 40)
        escolha = ' '
        while escolha not in 'sn':
            escolha = str(input('Quer começar [S/N]: ')).strip().lower()[0]
        if escolha == 's':
            import datetime
            cadastro = dict()
            cadastro['Nome'] = str(input('Digite o nome: '))
            ano = int(input('Digite o ano de nascimento: '))
            cadastro['Idade'] = datetime.date.today().year - ano
            cadastro['CTPS'] = int(input('Digite o CTPS (Se não tiver digite 0): '))
            if cadastro['CTPS'] != 0:
                cadastro['Ano de Contratação'] = int(input('Digite o ano de contratação: '))
                cadastro['Salário'] = float(input('Digite o sálario: R$'))
                cadastro['Aposentadoria'] = cadastro['Idade'] + (cadastro['Ano de Contratação'] + 35) - datetime.date.today().year
                print('-=' * 40)
                for k, v in cadastro.items():
                    if k == 'Salário':
                        print(f'{k}: R${v:.2f}')
                    else:
                        if k == 'Idade' or k == 'Aposentadoria':
                            print(f'{k}: {v} anos')
                        else:
                            print(f'{k}: {v}')
            else:
                if cadastro['CTPS'] == 0:
                    cadastro['CTPS'] = 'NÃO TEM'
                print('-=' * 40)
                for k, v in cadastro.items():
                    print(f'{k}: {v}')
        escolha = ' '
        while escolha not in 'sn':
            escolha = str(input('Quer começar [S/N]: ')).strip().lower()[0]
        if escolha == 's':
            jogador = dict()
            gol = list()
            jogador['Nome'] = str(input('Digite o nome do jogador: '))
            jogador['Partidas'] = int(input(f'Quantas partidas {jogador["Nome"]} jogou? '))
            for i in range(0, jogador['Partidas']):
                gol.append(int(input(f'Quantos gols ele fez na {i + 1}° partida: ')))
            jogador['gols'] = gol
            jogador['Total'] = sum(gol)
            print('-=' * 40)
            print(jogador)
            print('-=' * 40)
            for k, v in jogador.items():
                print(f'O campo {k} tem valor {v}')
            print('-=' * 40)
            print(f'O jogador {jogador["Nome"]} jogou {jogador["Partidas"]} partidas.')
            for i, g in enumerate(jogador['gols']):
                print(f'    => Na {i + 1}° partida, fez {g} gols')
            print(f'Um total de {jogador["Total"]} gols')
            print('-=' * 40)
        escolha = ' '
        while escolha not in 'sn':
            escolha = str(input('Quer começar [S/N]: ')).strip().lower()[0]
        if escolha == 's':
            cadastro = dict()
            lista = list()
            soma = media = 0
            while True:
                cadastro.clear()
                cadastro['Nome'] = str(input('Digite o nome: '))
                cadastro['Idade'] = int(input('Digite a Idade: '))
                soma += cadastro['Idade']
                while True:
                    cadastro['Sexo'] = str(input('Digite o sexo [M/F]: ')).upper().strip()
                    if cadastro['Sexo'] in 'MF':
                        break
                    else:
                        print('Digite M ou F, Por favor!')
                lista.append(cadastro.copy())
                while True:
                    opcao = str(input('Quer continuar [S/N]? ')).lower().strip()[0]
                    if opcao in 'sn':
                        break
                    print('Digite S ou N.')
                if opcao == 'n':
                    break
            print('-=' * 40)
            print(f'Foram cadastradas {len(lista)} pessoas.')
            media = soma / len(lista)
            print(f'A média das idades é {media:5.2f} anos')
            print(f'As mulheres são: ', end='')
            for p in lista:
                if p['Sexo'] == 'f':
                    print(f'[{p["Nome"]}] ', end='')
            print()
            print('Pessoas acima da média de idade:')
            for ac in lista:
                if ac['Idade'] >= media:
                    for k, v in ac.items():
                        print(f'{k}: {v}; ', end='')
            print()
        escolha = ' '
        while escolha not in 'sn':
            escolha = str(input('Quer começar [S/N]: ')).strip().lower()[0]
        if escolha == 's':
            jogador = dict()
            gol = list()
            jooj = list()
            while True:
                jogador.clear()
                jogador['Nome'] = str(input('Digite o nome do jogador: '))
                partidas = int(input(f'Quantas partidas {jogador["Nome"]} jogou? '))
                gol.clear()
                for i in range(0, partidas):
                    gol.append(int(input(f'Quantos gols ele fez na {i + 1}° partida: ')))
                jogador['gols'] = gol[:]
                jogador['Total'] = sum(gol)
                jooj.append(jogador.copy())
                while True:
                    opcao = str(input('Quer continuar [S/N]? '))
                    if opcao in 'sn':
                        break
                    print('Digite S ou N.')
                if opcao == 'n':
                    break
            print('-=' * 40)
            print('COD ', end='')
            for i in jogador.keys():
                print(f'{i:<15}', end='')
            print()
            print('-' * 40)
            for c, n in enumerate(jooj):
                print(f'{c:>3} ', end='')
                for d in n.values():
                    print(f'{str(d):<15}', end='')
                print()
            print('-' * 40)
            while True:
                dados = int(input('Quer mostrar os dados de qual jogador (999 para parar)? '))
                if dados == 999:
                    print('-=' * 40)
                    print('Até mais!')
                    break
                if dados >= len(jooj):
                    print('Não existe esse jogador')
                else:
                    print(f'LEVANTAMENTO DO JOGADOR {jooj[dados]["Nome"].upper()}:')
                    for i, g in enumerate(jooj[dados]['gols']):
                        print(f'No jogo {i + 1} fez {g} gols')
                print('-=' * 40)
linha()
while True:
    funcao = str(input('Quer começar a FUNÇÃO [S/N]? ')).strip().lower()[0]
    if funcao in 'sn':
        break
    print('Digite S ou N.')
if funcao == 's':
    while True:
        teoria = str(input('Quer começar a teoria [S/N]? ')).strip().lower()[0]
        if teoria in 'sn':
            break
    if teoria == 's':
        def soma(* n):
            """
            -> Faz a SOMA
            :param n: Recebe n variaveis para somar
            :return:
            """
            s = 0
            for num in n:
                s += num
            print(f'Somando os valores {n} temos {s}')

        help(soma)
        def contador(* num):
            tam = len(num)
            print('Foram digitados: ')
            for valor in num:
                print(f'{valor} ', end='')
            print('FIM!')
            print(f'Foram recebidos {tam} valores')
            linha()


        def dobra(lista):
            pos = 0
            while pos < len(lista):
                lista[pos] *= 2
                pos += 1


        #Programa Principal
        a = 4
        b = 5
        s = a + b
        print(s)
        a = 8
        b = 9
        s = a + b
        print(s)
        a = 2
        b = 1
        s = a + b
        print(s)
        soma(4, 5)
        soma(8, 9)
        soma(2, 1)
        soma(1, 2, 3, 4, 5)
        linha()
        contador(1, 4, 6, 7, 8)
        contador(1, 2)
        contador(1, 2, 3, 4, 5, 6, 7, 8, 9)
        valores = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        print(valores)
        dobra(valores)
        print(valores)


        def funcao():
            global n2
            n2 = 8
            n1 = 4
            print(f'N1 dentro do ESCOPO LOCAL vale {n1}.')
            print(f'N2 dentro do ESCOPO LOCAL vale {n2}.')


        n1 = 2
        n2 = 5
        funcao()
        print(f'N1 fora do ESCOPO LOCAL porem dentro do ESCOPO GLOBAL vale {n1}')
        print(f'N2 fora do ESCOPO LOCAL porem dentro do ESCOPO GLOBAL vale {n2}')

        def somar(a=0, b=0, c=0):
            s = a + b + c
            return s
        r1 = somar(3, 2, 5)
        r2 = somar(5, 2)
        r3 = somar(2)
        print(f'As somas foram: {r1}, {r2}, {r3}')


        def fatorial(num=1):
            f = 1
            for c in range(num, 0, -1):
                f *= c
            return f

        n = int(input('Digite um número: '))
        print(f'O fatorial de n é {fatorial(n)}')
        f1= fatorial(5)
        f2 = fatorial(4)
        f3 = fatorial()
        print(f'Os resultados são {f1} {f2} {f3}')


        def parouimpar(n=0):
            if n%2 == 0:
                return True
            else:
                return False

        num = int(input('Digite um número: '))
        if parouimpar(num):
            print('É par')
        else:
            print('É impar')
    desafio()
    while True:
        escolha = str(input('Quer começar [S/N]? ')).strip().lower()[0]
        if escolha in 'sn':
            break
    if escolha == 's':
        def area(b, h):
            a = b * h
            print(f'A área do terreno {b:.2f}m x {h:.2f}m é {a:.2f}m²')


        linha()
        print(f'{"DIMENSÃO DO TERRENO":^80}')
        linha()
        b = float(input(f'LARGURA (m): '))
        h = float(input(f'COMPRIMENTO (m): '))
        area(b, h)
    while True:
        escolha = str(input('Quer começar [S/N]? ')).strip().lower()[0]
        if escolha in 'sn':
            break
    if escolha == 's':
        def escreva(msg):
            for n in msg:
                tam = len(n) + 8
                print('~' * tam)
                print(f'    {n}')
                print('~' * tam)


        msg = ['Teste', 'Camilo Prado', 'oi']
        escreva(msg)
    while True:
        escolha = str(input('Quer começar [S/N]? ')).strip().lower()[0]
        if escolha in 'sn':
            break
    if escolha == 's':
        from time import sleep


        def contador(i, f, p):
            if p < 0:
                p *= -1
            if p == 0:
                p = 1
            print(f'CONTAGEM DE {i} A {f} DE {p} EM {p}:')
            if i < f:
                cont = i
                while cont <= f:
                    print(f'{cont} -> ', end='', flush=True)
                    cont += p
                    sleep(0.3)
                print('FIM!')
                linha()
            else:
                cont = i
                while cont >= f:
                    print(f'{cont} -> ', end='', flush=True)
                    cont -= p
                    sleep(0.3)
                print('FIM!')
                linha()
        contador(1, 10, 1)
        contador(10, 0, 2)
        inicio = int(input('INICIO: '))
        fim = int(input('FIM: '))
        passo = int(input('PASSO: '))
        contador(inicio, fim, passo)
    while True:
        escolha = str(input('Quer começar [S/N]? ')).strip().lower()[0]
        if escolha in 'sn':
            break
    if escolha == 's':
        def maior(num):
            mai = cont = 0
            linha()
            print('Analisando os valores registrados...')
            for c in num:
                print(f'{c} ', end='', flush=True)
                if cont == 0:
                    mai = c
                else:
                    if c > mai:
                        mai = c
                cont += 1
                sleep(0.3)
            print(f'. Foram digitados {cont} valores.')
            print(f'O maior valor é {mai}')


        from random import randint
        from time import sleep
        numeros = list()
        for i in range(0, 5):
            numeros.clear()
            aleatorio = randint(2, 10)
            for c in range(0, aleatorio):
                numeros.append(randint(1, 10))
            maior(numeros)
        linha()
    while True:
        escolha = str(input('Quer começar [S/N]? ')).strip().lower()[0]
        if escolha in 'sn':
            break
    if escolha == 's':
        def sorteia5(lista):
            import random, time
            for i in range (0 ,5):
                lista.append(random.randint(1, 10))
            print('Os 5 números sorteados foram: ',end='')
            for c in lista:
                print(f'{c} ', end='')
                time.sleep(0.3)
            print()


        def somaPar(v):
            somar = 0
            for n in v:
                if n % 2 == 0:
                    somar += n
            print(f'A soma dos números pares de {v} é {somar}')


        numeros = list()
        linha()
        sorteia5(numeros)
        somaPar(numeros)
        linha()
    while True:
        escolha = str(input('Quer começar [S/N]? ')).strip().lower()[0]
        if escolha in 'sn':
            break
    if escolha == 's':
        def voto(ano):
            import datetime
            idade = datetime.datetime.today().year - ano
            n = ' '
            if 0 < idade < 16:
                return f'Com {idade} anos: NÃO VOTA'
            elif 16 <= idade < 18 or idade > 65:
                return f'Com {idade} anos: VOTO OPCIONAL'
            else:
                return f'Com {idade} anos: VOTO OBRIGÁTORIO'


        linha()
        nasc = int(input('Digite o ano que nasceu: '))
        print(voto(nasc))
        linha()
    while True:
        escolha = str(input('Quer começar [S/N]? ')).strip().lower()[0]
        if escolha in 'sn':
            break
    if escolha == 's':
        def fatorial(n, show=False):
            """
            -> Calcula o Fatorial de um número
            :param n: O número a ser calculado.
            :param show: (opcional) Mostra ou não a conta.
            :return: O valor do Fatorial de um número n.
            """
            f = 1
            for c in range(n, 0, -1):
                if show:
                    print(c, end='')
                    if c > 1:
                        print(f' x ', end='')
                    else:
                        print(' = ', end='')
                f *= c
            if show:
                return f
            else:
                return f'O fatorial de {n} é {f}'


        h = int(input('Digite um número: '))
        while True:
            o = str(input('Quer mostrar o cálculo: ')).lower().strip()[0]
            if o in 'sn':
                break
        if o == 's':
            s = True
        else:
            s = False
        print(fatorial(h, show=s))
    while True:
        escolha = str(input('Quer começar [S/N]? ')).strip().lower()[0]
        if escolha in 'sn':
            break
    if escolha == 's':
        def ficha(nome='<desconhecido>', gols=0):
            return f'O jogador {nome} fez {int(gols)} gol(s) no campeonato.'


        n = str(input('Digite o nome do jogador: '))
        g = str(input('Quantos gols ele fez: '))
        if g.isnumeric():
            g = int(g)
        else:
            g = 0
        if n.strip() == '':
            print(ficha(gols=g))
        else:
            print(ficha(n, g))
    while True:
        escolha = str(input('Quer começar [S/N]? ')).strip().lower()[0]
        if escolha in 'sn':
            break
    if escolha == 's':
        def leiaint(num):
            ok = False
            valor = 0
            while True:
                num = input(num)
                if num.isnumeric():
                    valor = int(num)
                    ok = True
                else:
                    print('\033[31mERRO! DIGITE UM NÚMERO!\033[m')
                if ok:
                    break
            return valor


        linha()
        n = leiaint('Digite um número: ')
        print(f'Você digitou o número: {n}')
        linha()
    while True:
        escolha = str(input('Quer começar [S/N]? ')).strip().lower()[0]
        if escolha in 'sn':
            break
    if escolha == 's':
        def notas(*notas, sit=False):
            """
            -> Função para analisar notas e situações de vários alunos.
            :param notas: Uma ou mais notas dos alunos (aceita várias)
            :param sit: Valor opcional, indicando se deve ou não adicionar a situação.
            :return: Dicionário com várias informações sobre a situação da turma.
            """
            dicionario = dict()
            soma = 0
            situacao = ''
            for c, k in enumerate(notas[0]):
                soma += k
            media = soma/len(notas[0])
            dicionario['Total'] = len(notas[0])
            dicionario['Maior'] = max(notas[0])
            dicionario['Menor'] = min(notas[0])
            dicionario['Média'] = media
            if sit:
                if 0 <= media < 3:
                    situacao = 'PESSIMO'
                if 3 <= media < 5:
                    situacao = 'RUIM'
                if 5 <= media < 7:
                    situacao = 'RAZOAVEL'
                if 7 <= media < 9:
                    situacao = 'BOA'
                if 9 <= media <= 10:
                    situacao = 'INCRIVEL'
                dicionario['Situação'] = situacao
            return dicionario


        n = list()
        n.clear()
        while True:
           n.append(int(input(f'Digite a nota do aluno: ')))
           while True:
               opc = str(input('Quer continuar [S/N]? ')).lower().strip()[0]
               if opc in 'sn':
                   break
           if opc == 'n':
               break
        while True:
           situacao = str(input('Quer mostrar a situação da sala [S/N]? ')).lower().strip()[0]
           if situacao in 'sn':
               break
        if situacao == 's':
            s = True
        else:
            s = False
        resposta = notas(n, sit=s)
        print(resposta)
        linha()
    while True:
        escolha = str(input('Quer começar [S/N]? ')).strip().lower()[0]
        if escolha in 'sn':
            break
    if escolha == 's':
        c =('\033[m',   #0 - Sem cor
            '\033[30m', #1
            '\033[31m', #2
            '\033[32m', #3
            '\033[33m', #4
            '\033[34m', #5
            '\033[35m', #6
            '\033[40m', #7 - preto
            '\033[41m', #8 - vermelho
            '\033[42m', #9 - verde
            '\033[43m', #10 - amarelo
            '\033[44m', #11 - azul
            '\033[45m', #12 - roxo
            '\033[7m'   #13 - branco
            )
        import time


        def ajuda(msg):
            titulo(f'Acessando o Manual do comando \'{msg}\'', 11)
            time.sleep(0.5)
            print(c[13], end='')
            help(msg)
            print(c[0])


        def titulo(m, cor=0):
                tam = len(m) + 4
                print(c[cor], end='')
                print('~' * tam)
                print(f'  {m}')
                print('~' * tam)
                print(c[0], end='')


        while True:
            titulo('Sistema de Ajuda PyHELP', 9)
            time.sleep(0.5)
            terminal = str(input('Função ou Biblioteca > ')).lower().strip()
            if terminal == 'fim':
                break
            else:
                ajuda(terminal)
        titulo('Até Logo', 8)
linha()
while True:
    erro = str(input('Quer começar o TRATAMENTO DE ERRO [S/N]? ')).strip().lower()[0]
    if erro in 'sn':
        break
    print('Digite S ou N.')
if erro == 's':
    while True:
        teoria = str(input('Quer começar a teoria [S/N]? ')).strip().lower()[0]
        if teoria in 'sn':
            break
    if teoria == 's':
        try:
            a = int(input('Numerador: '))
            b = int(input('Denominador: '))
            r = a / b
        except (ValueError, TypeError):
            print('Tivemos um pequeno problema com os tipos de dados que você digitou!')
        except ZeroDivisionError:
            print('Não é possivel a divisão por 0')
        except KeyboardInterrupt:
            print('O usuário preferiu não informar os dados!')
        else:
            print(f'O resultado é {r}')
        finally:
            print('Volte sempre!')
    desafio()
    while True:
        escolha = str(input('Quer começar ex113 [S/N]? ')).strip().lower()[0]
        if escolha in 'sn':
            break
    if escolha == 's':
        from utilidades import dados, moeda
        i = dados.leiaint('Digite um número inteiro: ')
        r = dados.leiafloat('Digite um número real: ')
        print(f'O número inteiro foi {i} e o real {r}')
        linha()
    while True:
        escolha = str(input('Quer começar ex114 [S/N]? ')).strip().lower()[0]
        if escolha in 'sn':
            break
    if escolha == 's':
        import urllib
        import urllib.request
        from utilidades import dados
        try:
            site = urllib.request.urlopen('http://www.pudim.com.br')
        except urllib.error.URLError:
            dados.cor(2)
            print('O site PUDIM está inacesivel no momento. Tente mais tarde!')
            dados.cor(0)
        else:
            dados.cor(3)
            print('O site PUDIM está acessivel no momento!')
            dados.cor(0)
            print(site.read())
    while True:
        escolha = str(input('Quer começar ex115 [S/N]? ')).strip().lower()[0]
        if escolha in 'sn':
            break
    if escolha == 's':
        from utilidades.dados import *
        from utilidades.interface import *
        from utilidades.arquivo import *
        from time import sleep

        arq = 'CursoPython.txt'
        lista = ['Ver pessoas cadastrada', 'Cadastrar nova pessoa', 'Sair do programa']
        if arquivoexiste(arq):
            cor(3)
            print('Arquivo encontrado com sucesso!')
            cor(0)
        else:
            cor(2)
            print('Aquivo não encontrado!')
            cor(0)
            criararquivo(arq)
        while True:
            resposta = menu(lista)
            sleep(1)
            if resposta == 1:
                lerarquivo(arq)
                sleep(1)
            elif resposta == 2:
                cabecalho('NOVO CADASTRO')
                nome = str(input('Nome: '))
                idade = leiaint('Idade: ')
                escreveraquivo(arq, nome, idade)
                sleep(1)
            elif resposta == 3:
                print('Saindo do Programa...')
                despedida()
                break
            else:
                cor(2)
                print('ERRO! Digite uma opção válida')
                cor(0)
                sleep(1)
print(f'{"ACABOU":-^80}')
