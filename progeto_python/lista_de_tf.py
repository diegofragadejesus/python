import PySimpleGUI as sg

class Tarefa:
    def __init__(self, checkbox, texto):
        self.checkbox = checkbox
        self.texto = texto

def criar_arquivo(nome_arquivo, tarefas):
    with open(nome_arquivo, 'w') as arquivo:
        for tarefa in tarefas:
            arquivo.write(f"{'X' if tarefa.checkbox else ' '}\t{tarefa.texto}\n")

def criar_janela_inicial():
    sg.theme('LightPurple')
    layout = [
        [sg.Frame('Tarefas', layout=[[sg.Checkbox(''), sg.Input('')]], key='containe')],
        [sg.Button('Nova tarefa'), sg.Button('Resetar'), sg.Button('Criar Arquivo')]
    ]
    return sg.Window('Toda lista', layout=layout, finalize=True)

# Criando a janela
janela = criar_janela_inicial()

while True:
    event, values = janela.read()

    if event == sg.WIN_CLOSED:
        break
    elif event == 'Nova tarefa':
        janela.extend_layout(janela['containe'], [[sg.Checkbox(''), sg.Input('')]])
    elif event == 'Criar Arquivo':
        nome_arquivo = sg.popup_get_file('Escolha um nome para o arquivo', save_as=True, file_types=(("Text Files", "*.txt"),))
        if nome_arquivo:
            tarefas = [Tarefa(checkbox=element[0], texto=element[1]) for element in janela['containe'].Rows]
            criar_arquivo(nome_arquivo, tarefas)
            sg.popup(f'Arquivo {nome_arquivo} criado com sucesso!')
    elif event == 'Resetar':
        janela.close()
        janela = criar_janela_inicial()


    