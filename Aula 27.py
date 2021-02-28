from datetime import date
nasc = int(input('Digite o seu ano de nascimento: '))
atual = date.today().year
idade = int(atual - nasc)

print('Quem nasceu em {} tem {} anos'.format(nasc,idade))
if idade>18:
    a = 18 - idade
    alistou = atual + a
    print('Essa pessoa se alistou no tiro de guerra em \033[0;33m{}\033[m!'.format(alistou))
elif idade == 18:
    print('\033[0;30;41mEssa pessoa é OBRIGADA A SE ALISTAR!!!!!!!!!\033[m')
else:
    anos = 18 - idade
    ira = atual + anos
    print('Essa pessoa não pode se alistar!\nEla tem que esperar \033[0;33m{}\033[m anos para se alistar.'.format(anos))
    print('Será no ano de \033[0;33m{}\033[m!'.format(ira))