r1 = float(input('Digite o primeiro segmento: '))
r2 = float(input('Digite o segundo segmento: '))
r3 = float(input('Digite o terceiro segmento: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Pode formar o triângulo! e ', end='')
    if r1 == r2 == r3:
        print('É EQUILÁTERO')
    elif r1 != r2 != r3 != r1:
        print('É ESCALENO')
    else:
        print('É ISÓSCELES')
else:
    print('Não forma triângulo!!')