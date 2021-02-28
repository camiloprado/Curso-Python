soma = 0
s = 0
c = 0
cont = 0
for i in range(1, 7):
    n = int(input('Digite o {} numero: '.format(i)))
    if n % 2 == 0:
        soma += n
        cont += 1
    else:
        s += n
        c += 1
print('Existem {} numeros impares totalizando {}'.format(c, s))
print('Existem {} numeros pares totalizando {}'.format(cont, soma))