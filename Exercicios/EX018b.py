    '''import math
angulo = float(input("Digite o valor de um angulo: "))

s = math.sin(math.radians(angulo))
print("O ângulo de {} tem o SENO de {:.2f}".format(angulo, s))
c = math.cos(math.radians(angulo))
print("O ângulo de {} tem o COSSENO de {:.2f}".format(angulo, c))
t = math.tan(math.radians(angulo))
print("O ângulo de {} tem a TANGENTE de {:.2f}".format(angulo, t))'''

from math import radians, sin, cos, tan
angulo = float(input("Digite o valor de um angulo: "))

s = sin(radians(angulo))
print("O ângulo de {} tem o SENO de {:.2f}".format(angulo, s))
c = cos(radians(angulo))
print("O ângulo de {} tem o COSSENO de {:.2f}".format(angulo, c))
t = tan(radians(angulo))
print("O ângulo de {} tem a TANGENTE de {:.2f}".format(angulo, t))

