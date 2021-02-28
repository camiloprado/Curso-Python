import utilidades.dados


def linha(tam=40):
    print('-' * tam)


def cabecalho(txt='MENU'):
    linha()
    print(txt.center(40))
    linha()


def menu(list):
    cabecalho('MENU PRINCIPAL')
    for i, v in enumerate(list):
        utilidades.dados.cor(4)
        print(f'{i + 1} - ', end='')
        utilidades.dados.cor(5)
        print(v)
        utilidades.dados.cor(0)
    linha()
    utilidades.dados.cor(3)
    opc = utilidades.dados.leiaint('Sua opção: ')
    utilidades.dados.cor(0)
    return opc


def despedida():
    """
    -> Frase "Até Logo" letra por letra
    :return: Letra por letra
    """
    from time import sleep
    teste = ['Até Logo!']
    for i, k in enumerate(teste[0]):
        if i == 1:
            utilidades.dados.cor(3)
        elif 2 <= i <= 6:
            utilidades.dados.cor(i)
        else:
            utilidades.dados.cor(0)

        print(k, end='')
        sleep(0.3)
    utilidades.dados.cor(0)
    print()

