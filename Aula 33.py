from time import sleep
escolha = input('Iniciar contagem (S/N)? ')
escolha.lower()
if escolha == 's':
    for i in range(0,11):
        print(i)
        sleep(1)
    print('\033[0;30;46mParabens!!!!!!!!!\033[m')
else:
    print('Poxa!')
esc = input('Iniciar contagem regressiva (S/N)? ')
esc.lower()
if esc == 's':
    for i in range(10,-1, -1):
        print(i)
        sleep(1)
    print('\033[0;30;46mParabens!!!!!!!!!\033[m')
else:
    print('Poxa!')
pares = input('Quer que conte em pares (S/N)? ')
pares.lower()
if pares == 's':
    for i in range (0, 51, 2):
        print(i, end=(' '))
else:
    print('Poxa!')
somatoria = input('Quer que mostre os números impares e multiplus de 3 (S/N)? ')
somatoria.lower()
soma = 0
n = 0
if somatoria == 's':
    for i in range (1, 501, 2):
        if i % 3 == 0:
            soma = soma + i
            n += 1 #Essa nomenclatura é a mesma que n = n + 1
    print('A soma de todos os {} itens é {}'.format(n, soma))
else:
    print('Poxa!')