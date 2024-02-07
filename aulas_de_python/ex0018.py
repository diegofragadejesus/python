import os

def exibir_menu():
    print("\n=== Lista de Tarefas ===")
    print("1. Adicionar Tarefa")
    print("2. Visualizar Tarefas")
    print("3. Remover Tarefa")
    print("4. Sair")

def adicionar_tarefa():
    tarefa = input("Digite a nova tarefa: ")
    with open('tarefas.txt', 'a') as arquivo:
        arquivo.write(tarefa + '\n')
    print("Tarefa adicionada com sucesso!")

def visualizar_tarefas():
    if os.path.exists('tarefas.txt'):
        with open('tarefas.txt', 'r') as arquivo:
            tarefas = arquivo.readlines()
            if tarefas:
                print("\n=== Tarefas ===")
                for idx, tarefa in enumerate(tarefas, start=1):
                    print(f"{idx}. {tarefa.strip()}")
            else:
                print("Não há tarefas cadastradas.")
    else:
        print("Não há tarefas cadastradas.")

def remover_tarefa():
    visualizar_tarefas()
    if os.path.exists('tarefas.txt'):
        try:
            numero_tarefa = int(input("Digite o número da tarefa a ser removida: "))
            with open('tarefas.txt', 'r') as arquivo:
                tarefas = arquivo.readlines()
            with open('tarefas.txt', 'w') as arquivo:
                for idx, tarefa in enumerate(tarefas, start=1):
                    if idx != numero_tarefa:
                        arquivo.write(tarefa)
            print("Tarefa removida com sucesso!")
        except ValueError:
            print("Por favor, digite um número válido.")
    else:
        print("Não há tarefas cadastradas.")

def main():
    while True:
        exibir_menu()
        escolha = input("Escolha uma opção (1-4): ")

        if escolha == '1':
            adicionar_tarefa()
        elif escolha == '2':
            visualizar_tarefas()
        elif escolha == '3':
            remover_tarefa()
        elif escolha == '4':
            print("Saindo. Até mais!")
            break
        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")

if __name__ == "__main__":
    main()
