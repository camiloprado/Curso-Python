def leiadinheiro(msg):
    ok = False
    while not ok:
        n = str(input(msg)).replace(',', '.').strip()
        if n.isalpha() or n == '':
            print(cor(2))
            print(f'ERRO! \"{n}\" não é um preço válido.')
            print(cor(0))
        else:
            ok = True
            return float(n)


def leiafloat(num):
        while True:
            try:
                n = str(input(num)).strip().replace(',', '.')
                n = float(n)
            except (ValueError, TypeError):
                cor(2)
                print('Tivemos um pequeno problema com os tipos de dados que você digitou!')
                cor(0)
                continue
            except ZeroDivisionError:
                cor(2)
                print('Não é possivel a divisão por 0')
                cor(0)
                continue
            except Exception as erro:
                cor(2)
                print(f'Foi encontrado o seguinte erro: {erro}')
                cor(0)
                continue
            except KeyboardInterrupt:
                cor(2)
                print('O usuário preferiu não digitar o número!')
                cor(0)
                return 0
            else:
                return n


def leiaint(num):
        while True:
            try:
                n = str(input(num)).strip().replace(',','.')
                n = int(n)
            except (ValueError, TypeError):
                cor(2)
                print('ERRO! Tivemos um pequeno problema com os tipos de dados que você digitou!')
                cor(0)
                continue
            except ZeroDivisionError:
                cor(2)
                print('Não é possivel a divisão por 0')
                cor(0)
                continue
            except Exception as erro:
                cor(2)
                print(f'Foi encontrado o seguinte erro: {erro}')
                cor(0)
                continue
            except KeyboardInterrupt:
                cor(2)
                print('O usuário preferiu não digitar o número!')
                cor(0)
            else:
                return n


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
         '\033[m'  ,  # 7 - Sem Cor
         #Fundo
         '\033[40m',  # 8 - preto
         '\033[41m',  # 9 - vermelho
         '\033[42m',  # 10 - verde
         '\033[43m',  # 11 - amarelo
         '\033[44m',  # 12 - azul
         '\033[45m',  # 13 - roxo
         '\033[7m'  # 14 - Inverte a cor da letra com a do fundo
         )
    return print(c[lista], end='')

