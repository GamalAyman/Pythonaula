produto = float(input("Digite o valor do produto: R$"))

d = produto - produto * 0.05

print("O valor do produto é {:.2f}, mas com desconto de 5% fica {:.2f}".format(produto, d))

#valor * porcentagem / 100  (d = produto - produto * 5 /100)