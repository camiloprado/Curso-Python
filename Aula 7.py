t = int(input('Digite o numero para ver a tabuada: '))
print('-'* 12)
print('{} x {:2} = {}'.format(t, 1, t*1))
print('{} x {:2} = {}'.format(t, 2, t*2))
print('{} x {:2} = {}'.format(t, 3, t*3))
print('{} x {:2} = {}'.format(t, 4, t*4))
print('{} x {:2} = {}'.format(t, 5, t*5))
print('{} x {:2} = {}'.format(t, 6, t*6))
print('{} x {:2} = {}'.format(t, 7, t*7))
print('{} x {:2} = {}'.format(t, 8, t*8))
print('{} x {:2} = {}'.format(t, 9, t*9))
print('{} x {:2} = {}'.format(t, 10, t*10))
print('-'* 12)
for i in range(1,11):
    print('{} x {:2} = {}'.format(t, i, t*i))
print('-'*12)
while True:
    t = int(input('Digite o numero para ver a tabuada: '))
    if t < 0:
        break
    for c in range(1,11):
        print('{} x {:2} = {}'.format(t, c, t * c))
    print('-' * 12)
print('Tabuada não encontrada!')
