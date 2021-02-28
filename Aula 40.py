print('\033[31m{:~^100}'.format('\033[33mSequência de Fibonacci\033[31m'))
n = int(input('\033[mQuantos termos quer que mostre? '))
t1 = 0
t2 = 1
print('\033[33m~\033[m'*100)
print('{} → {}'.format(t1, t2), end='')
cont = 3
while cont <= n:
    t3 = t1 + t2
    print(' → {}'.format(t3),end='')
    t1 = t2
    t2 = t3
    cont += 1
print(' → FIM!!!')
print('\033[33m~\033[m'*100)
