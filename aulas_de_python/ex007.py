import random
seu_nome = input('qual é o seu nome ? :')

lista_alunos = ['ana','matheus','bruno','filipe','marcos','jumior','vanessa','pedro','alesandra', seu_nome]

random.shuffle(lista_alunos)



for i in range(1 ,11):
    nome_aleatorio = lista_alunos[i - 1]
    print(f' Numero : {i} / aluno : {nome_aleatorio}')

