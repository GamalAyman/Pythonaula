#usando a biblioteca math / ou só o metodo hypot

#from math import hypot
import math
co = float(input("Digite o comprimento do cateto oposto: "))
ca = float(input("Digite o comprimento do cateto adjacente: "))

h = math.hypot(co, ca)

print("O comprimento do cateto oposto é {} e do cateto adjacente é {} então a hipotenusa é igual a {:.2f}: ".format(co, ca, h))

'''usaando o calculo matemático
co = float(input("Comprimento do cateto oposto: "))
ca = float(input("Comprimento do cateto adjacente: "))
hi = (co ** 2 + ca**2) ** (1/2)
print("a Hipotenusa vai medir {:.2f}".format(hi))'''    