frase = str(input('Digite uma frase: ')).upper().strip()
print('A letra "A" aparece no total de {}'.format(frase.count('A')))
print('Sua primeira aparição foi na posição {}'.format(frase.find('A') + 1))
print('Sua ultima aparição foi na posição {}'.format(frase.rfind('A') + 1))