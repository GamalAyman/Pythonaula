m = float(input("Digite quantos metros: "))
c = m * 100
ml = m * 1000
km = m / 1000
hm = m / 100
dam = m / 10
dm = m / 0.1


print("O valor em metros é {}, em centimetros é {:.0f} e em milimetros é {:.0f} :".format(m, c, ml))
print("{} metros é igual a {} KM".format(m, km))
print("{} metros é igual a {} hectômetro".format(m, hm))
print("{} metros é igual a {} decâmetro".format(m, dam))
print("{} metros é igual a {} decímetro".format(m, dm))