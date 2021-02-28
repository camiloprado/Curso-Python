print('-'* 80)
print('{:' '^80}'.format('CAIXA ELETRÔNICO'))
print('-'* 80)
valor = int(input('Quanto quer sacar? R$'))
total = valor
nota = i = 100
totalnota = 0
while True:
    if total >= nota:
        total -= nota
        totalnota += 1
    else:
        if totalnota != 0:
            print(f'Total de {totalnota} notas de R${nota}')
        if nota == 100:
            nota = 50
        elif nota == 50:
            nota = 20
        elif nota == 20:
            nota = 10
        elif nota == 10:
            nota = 5
        elif nota == 5:
            nota = 1
        totalnota = 0
        if total == 0:
            print('Volte Sempre!')
            print('-' * 80)
            break
