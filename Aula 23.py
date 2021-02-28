from datetime import date
print('Para analisar o ano atual digite "0".')
ano = int(input('Digite o ano para ser analisado: '))
if ano == '0':
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano {} é BISSEXTO'.format(ano))
else:
    print('O ano {} NÃO é BISSEXTO'.format(ano))