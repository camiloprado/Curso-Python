def leiadinheiro(msg):
    ok = False
    while not ok:
        n = str(input(msg)).replace(',', '.').strip()
        if n.isalpha() or n == '':
            print(f'\033[31mERRO! \"{n}\" não é um preço válido.\033[m')
        else:
            ok = True
            return float(n)


def leiaint(num):
    ok = False
    valor = 0
    while True:
        num = input(num)
        if num.isnumeric():
            valor = int(num)
            ok = True
        else:
            print('\033[31mERRO! DIGITE UM NÚMERO!\033[m')
        if ok:
            break
    return valor

def cor(lista):
    """
    -> Código de cores
    :param lista: Número denomiado para cada cor
    :return: Cor
    """
    c = ('\033[m',  # 0 - Sem cor
         #letra
         '\033[30m',  # 1 - preto
         '\033[31m',  # 2 - vermelho
         '\033[32m',  # 3 - verde
         '\033[33m',  # 4 - amarelo
         '\033[34m',  # 5 - azul
         '\033[35m',  # 6 - roxo
         #Fundo
         '\033[40m',  # 7 - preto
         '\033[41m',  # 8 - vermelho
         '\033[42m',  # 9 - verde
         '\033[43m',  # 10 - amarelo
         '\033[44m',  # 11 - azul
         '\033[45m',  # 12 - roxo
         '\033[7m'  # 13 - Inverte a cor da letra com a do fundo
         )
    return c[lista]
