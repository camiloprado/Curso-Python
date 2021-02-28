termo = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão: '))
decimo = termo +(10 - 1) * razao
for i in range (termo, decimo, razao):
    print('{} '.format(i), end=('→ '))
print('É isso!')
#
num = int(input('Digite um número: '))
tot = 0
for i in range (1, num + 1):
    if num % i == 0:
        print('\033[33m', end='')
        tot += 1
    else:
        print('\033[31m', end='')
    print('{} '.format(i), end='')
print('\n\033[mO número {} é divisivel {}'.format(num, tot))
if tot == 2:
    print('Portanto é PRIMO!')
else:
    print('Portanto \033[31mNÃO\033[m é PRIMO!')
#
frase =str(input('Digite uma frase: ').strip().upper())
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
for i in range(len(junto) - 1, -1, -1):
    inverso += junto[i]
print('Você digitou a seguinte frase:\033[33m\n{}\033[m.'.format(junto))
print('Ela ao contrário é:\033[33m\n{}\033[m.'.format(inverso))
if junto == inverso:
    print('Essa frase é um \033[33mPalíndromo\033[m')
else:
    print('Essa frase \033[31mNÃO\033[m é um \033[31mPalíndromo\033[m')
