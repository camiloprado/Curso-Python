def aumentar(n=0, p=100, format=False):
    """
    -> Aumento do valor de acordo com a porcentagem
    :param n: Valor inserido a ser calculado
    :param p: Porcentagem a ser calculada
    :param format: Formato se quer ou não com cifrão
    :return: O valor com acrescimo da porcentagem
    """
    porcentagem = p/100
    a = n + (porcentagem * n)
    return a if format is False else moeda(n)


def diminuir(n=0, p=100, format=False):
    """
    -> Diminuição do valor de acordo com a porcentagem
    :param n: Valor inserido a ser calculado
    :param p: Porcentagem a ser calculada
    :param format: Formato se quer ou não com cifrão
    :return: O valor com decrescimo da porcentagem
    """
    porcentagem = p/100
    d = n - (porcentagem * n)
    return d if format is False else moeda(n)


def dobro(n=0, format=False):
    """
    -> Gera o dobro do valor inserido
    :param n: Valor a ser calculado
    :param format: Formato se quer ou não com cifrão
    :return: O dobro do Valor
    """
    r = n * 2
    return r if format is False else moeda(n)


def metade(n=0, format=False):
    """
    -> Gera a metade do valor inserido
    :param n: Valor a ser calculado
    :param format: Formato se quer ou não com cifrão
    :return: Metade do valor
    """
    r = n / 2
    return r if format is False else moeda(n)


def moeda(n=0, moeda='R$'):
    """
    -> Formata o valor para o tipo Moeda
    :param n: Valor a ser formatado
    :param moeda: Tipo da moeda
    :return: O valor formato em moeda
    """
    r = f'{moeda}{n:>8.2f}'.replace('.', ',')
    return r


def resumo(n=0, au=100, red=100, format=False):
    """
    -> Gera um resumo para o dobro, metade, aumento e redução de uma valor
    :param n: Valor a ser inserido
    :param au: Porcentagem para ser acrescentado ao valor
    :param red: Porcentagem para ser reduzido ao valor
    :param m: Tipo da moeda
    :return: Resumo
    """
    print('-'*40)
    print(f'{"RESUMO DO VALOR":^40}')
    print('-'*40)
    print(f'Preço analisado:       \t{moeda(n)}')
    print(f'Dobro do preço:        \t{dobro(n, format)}')
    print(f'Metade do preço:       \t{metade(n, format)}')
    print(f'Com {au}% de aumento:  \t{aumentar(n, au, format)}')
    print(f'Com {red}% de redução: \t{diminuir(n, red, format)}')
    print('-'*40)
