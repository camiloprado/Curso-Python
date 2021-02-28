peso = float(input('Digite seu peso (KG): '))
altura = float(input('Digite sua altura (m): '))
IMC = float(peso / (altura**2))
print('A pessoa com {}m e {}Kg tem IMC igual a: {:.1f}'.format(altura, peso, IMC))
if IMC <= 18.5:
       print('Está ABAIXO DO PESO!')
elif IMC > 18.5 and IMC <=25:
    print('Está no PESO IDEAL!')
elif IMC > 25 and IMC <= 30:
    print('Está SOBREPESO!')
elif IMC > 30 and IMC <= 40:
    print('Está OBESO!')
elif IMC > 40:
    print('Está com OBESIDADE MORBIDA!')