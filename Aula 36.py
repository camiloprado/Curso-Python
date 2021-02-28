from datetime import date
contm = 0
contM = 0
maior = 0
menor = 0
for i in range(1, 8):
    n = int(input('Digite o ano de nascimento da {}° pessoa: '.format(i)))
    idade = date.today().year - n
    peso = float(input('Digite o peso da {}° pessoa: '.format(i)))
    if idade >= 18:
        contM += 1
    else:
        contm += 1
    if i == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso

print('Tem {} maiores de idade!'.format(contM))
print('    {} menores de idade!'.format(contm))
print('O maior peso é {}Kg!'.format(maior))
print('O menor peso é {}Kg!'.format(menor))
