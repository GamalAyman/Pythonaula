'''import random
n1 = input("Digite o nome do primeiro aluno: ")
n2 = input("Digite o nome do segundo aluno: ")
n3 = input("Digite o nome do terceiro aluno: ")
n4 = input("Digite o nome do quarto aluno: ")

s = [n1, n2, n3, n4]
random.shuffle(s)
print(s)   '''

from random import shuffle
n1 = str(input("Primeiro aluno: "))
n2 = str(input("Segundo aluno: "))
n3 = str(input("Terceiro aluno: "))
n4 = str(input("Quarto aluno"))

lista = [n1, n2, n3, n4]

shuffle(lista)
print("A ordem de apresentação será ")
print(lista)