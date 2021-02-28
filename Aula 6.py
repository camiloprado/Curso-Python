operaçao = str(input('Escolha para qual transformação (mm, cm, dm, dam, hm , km): '))
if(operaçao == 'mm'):
    valor = float(input('Digite o valor: '))
    print('O valor em mm é: {}'.format(valor*(pow(10, 3))))
elif(operaçao == 'cm'):
    valor = float(input('Digite o valor: '))
    print('O valor em cm é: {}'.format(valor*(pow(10, 2))))
elif(operaçao == 'dm'):
    valor = float(input('Digite o valor: '))
    print('O valor em dm é: {}'.format(valor*(pow(10, 1))))
elif(operaçao == 'dam'):
    valor = float(input('Digite o valor: '))
    print('O valor em dam é: {}'.format(valor*(pow(10, -1))))
elif(operaçao == 'hm'):
    valor = float(input('Digite o valor: '))
    print('O valor em hm é: {}'.format(valor*(pow(10, -2))))
elif(operaçao == 'km'):
    valor = float(input('Digite o valor: '))
    print('O valor em km é: {}'.format(valor*(pow(10, -3))))
else:
    print('Não existe')