print('Gerador de PA')
print('-=' * 12)
primeiro = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão da PA: '))
termo = primeiro
cont = 1
total = 0
mais = 10
while mais != 0:
    total += mais
    while cont <= total:
        print('{} → '.format(termo), end='')
        termo += razao
        cont += 1
    print('PAUSA!')
    mais = int(input('Quantos termos quer agora? '))
print('Progressão finalizada com {} termos mostrados'.format(total))