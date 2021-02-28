def arquivoexiste(nome):
    try:
        a = open(nome, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criararquivo(nome):
    from utilidades import dados
    from utilidades import interface
    try:
        a = open(nome, 'wt+')
        a.close()
    except:
        dados.cor(2)
        print('Houve um erro na criação de arquivo!')
        dados.cor(0)
    else:
        dados.cor(3)
        print(f'Arquivo {nome} criado com sucesso!')
        dados.cor(0)


def lerarquivo(nome):
    from utilidades import dados
    from utilidades import interface
    try:
        a = open(nome, 'rt')
    except:
        dados.cor(2)
        print(f'ERRO! Não foi possivel ler o arquivo {nome}')
        dados.cor(0)
    else:
        interface.cabecalho('Pessoas cadastradas!'.upper())
        for linha in a:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n', '')
            print(f'{dado[0]:<30}{dado[1]:>3} anos')
    finally:
        a.close()


def escreveraquivo(arquivo, info1='<desconhecido>', info2=0):
    from utilidades import dados
    from utilidades import interface
    try:
        a = open(arquivo, 'at')
    except:
        dados.cor(2)
        print(f'ERRO! Não foi possivel abrir o arquivo {arquivo}')
        dados.cor(0)
    else:
        try:
            a.write(f'{info1};{info2}\n')
        except:
            dados.cor(2)
            print('Houve um erro na hora de escrever os dados!')
            dados.cor(0)
        else:
            dados.cor(3)
            print(f'Cadastrado \033[33m{info1}\033[32m com Sucesso!')
            dados.cor(0)
            a.close()
