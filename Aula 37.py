cont = 0
mulheres = 0
nvelho = 'Não encontrado'
fvelho = 'Não encontrado'
somaridade = 0
velho = 0
velha = 0
for i in range (1,5):
    print('-----------{}° Pessoa-----------'.format(i))
    nome = str(input('Digite o nome: ')).strip()
    idade = int(input('Digite a idade: '))
    sexo = str(input('Digite o sexo (M/F/I): ')).lower().strip()
    cont += 1
    somaridade += idade
    if sexo == "f" and idade <= 20:
        mulheres += 1
    if i == 1 and sexo == 'm':
        velho = idade
        nvelho = nome
    if i == 1 and sexo == 'f':
        velha = idade
        fvelho = nome
    else:
        if idade > velho and sexo == 'm':
            velho = idade
            nvelho = nome
        if idade > velha and sexo == 'f':
            velha = idade
            fvelho = nome
print('A média das idades é: \033[33m{:.0f}\033[m'.format(somaridade/cont))
print('O mais velho é o \033[33m{}\033[m e tem \033[33m{}\033[m anos.'.format(nvelho, velho))
print('A mais velha é a \033[33m{}\033[m e tem \033[33m{}\033[m anos'.format(fvelho, velha))
print('Tem \033[33m{}\033[m mulheres com 20 ou menos anos.'.format(mulheres))