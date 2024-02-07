from random import shuffle
a1 = input('Nome do aluno 1º :')
a2 = input('Nome do aluno 2º :')
a3 = input('Nome do aluno 3º :')
lista = [a1 ,a2, a3]
shuffle(lista)
print(f'A orden de apresentação vai ser : {lista}')