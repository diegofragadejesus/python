import random

seu_nome = input('Qual é o seu nome? ')

lista_alunos = ['Ana', 'Matheus', 'Bruno', 'Filipe', 'Marcos', 'Junior', 'Vanessa', 'Pedro', 'Alessandra', seu_nome]

random.shuffle(lista_alunos)

print(f'\nBem-vindo(a), {seu_nome}!\n')

for numero, nome_aleatorio in enumerate(lista_alunos, start=1):
    print(f'Número: {numero} / Aluno: {nome_aleatorio}')
