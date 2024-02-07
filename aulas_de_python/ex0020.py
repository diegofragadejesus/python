import os


def adisionar():
    fucao =input('escreva uma função :')
    with open('função.txt', 'a') as arquivo:
      arquivo.write(fucao + '\n')
      print('função a dicionada com sucesso !')
def visualizar_tarefas():
    if os.path.exists('função.txt'):
        with open('função.txt', 'r') as arquivo:
            tarefas = arquivo.readlines()
            if tarefas:
                print("\n=== Tarefas ===")
                for idx, tarefa in enumerate(tarefas, start=1):
                    print(f"{idx}. {tarefa.strip()}")
            else:
                print("Não há tarefas cadastradas.")
    else:
        print("Não há tarefas cadastradas.")


while True:
      escolha =int(input('[1]para adicionar \n [2]pra visualisar'))
      if escolha == 1:
         adisionar()
      elif escolha == 2:
          visualizar_tarefas()