import math
a = int(input("Digite um angulo: "))

sen = math.sin(a)
cos = math.cos(a)
t = math.tan(a)
print("O seno de {} é {:.2f}".format(a,sen))
print("O cossento de {} é {:.2f}".format(a, cos))
print("A tangente de {} é {:.2f}".format(a, t))

