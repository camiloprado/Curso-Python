l = float(input('Informe a largura em m: '))
h = float(input('Informe a altura em m: '))
print('Sua parede tem a seguinte dimensão:\n{:.2f} x {:.2f} metros'.format(l, h))
a = l*h
print('Portanto a área é: {:.2f}mm²'.format(a))
print('Para pintar a parede gastará: {:.2f}l de tinta'.format(a/2))