import random
A1 =input('Qual é o nome do 1º aluno ? :')
A2 =input('Qual é o nome do 2º aluno ? :')
A3 =input('Qual é o nome do 3º aluno ? :')
lista = [A1, A2 , A3]
escolhido = random.choice(lista)
print(f'o aluno escollhido foi {escolhido}')