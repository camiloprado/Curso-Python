altura = float(input('Digite sua altura (m): '))
peso = float(input('Digite seu peso (Kg): '))
imc = float(peso / (altura ** 2 ))
print('Seu IMC é {:.2f}. '.format(imc))
if imc <= 18.5:
    print('Está pessoa está ABIAXO DO PESO!')
elif imc > 18.5 and imc<= 25:
    print('Está pessoa está no PESO IDEAL!')
elif imc > 25 and imc <= 30:
    print('Está pessoa está no SOBREPESO!')
elif imc > 30 and imc <= 40:
    print('Está pessoa está na OBESIDADE!')
elif imc > 40:
    print('Está pessoa está na OBESIDADE MÓRBIDA!')
else:
    print('Não funcionou!')

