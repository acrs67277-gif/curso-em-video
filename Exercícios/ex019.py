import random
n1 = str(input('Primeiro aluno: '))
n2 = str(input('segundo aluno: '))
n3 = str(input('Terceiro aluno: '))
n4 = str(input('Quanto aluno: '))
lista = [n1, n2, n3, n4]
escolhido = random.choice(lista)
print('O aluno escolhido foi {} '.format(escolhido))
