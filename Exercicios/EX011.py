altura = float(input("Digite a altura da parece: "))
largura = float(input("Digite a largura da parede: "))

area = altura * largura
tinta = area / 2
print("Sua parede tem a dimensão de {} x {} e sua área é de {} metros2. Para pintar essa parede, você precisará de {}L de tinta".format(altura, largura, area, tinta))
