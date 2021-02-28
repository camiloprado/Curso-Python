import math
angulo = float(input('Digite o ângulo: '))
print('Para os ângulo de {:.0f}°:\nSeno = {:.1f}\nCosseno = {:.1f}\nTangente = {:.1f}'.format(angulo, math.sin(math.radians(angulo)), math.cos(math.radians(angulo)), math.tan(math.radians(angulo))))