informação = input('Digite algo:')
print('Valor primitivo é ',type(informação))
print('É alfanumérico?',informação.isalnum())
print('É alpha?',informação.isalpha())
print('É numérico?',informação.isnumeric())
print('É apenas espaços?',informação.isspace())