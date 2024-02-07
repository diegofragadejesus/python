import PySimpleGUI as py
def criar_janela_inicial():
    py.theme('LightPurple')
    linha =[
         [py.Checkbox(''),py.Input('')]
    ]
    layout =[
        [ py.Frame('Tarefas',layout=linha,key='containe')],
        [py.Button('Nova tarefa'), py.Button('Resetar'),py.Button('Criar Arquivo') ]
    ]
    return py.Window('Toda lista',layout=layout,finalize=True)
#criando a janela
janela =criar_janela_inicial()
while True:
    event,value = janela.read()
    if event == py.WIN_CLOSED:
        break
    elif event == 'Nova tarefa':
        janela.extend_layout(janela['containe'], [[py.Checkbox(''),py.Input('')]])
    elif event == 'Resetar':
        janela.close()
        janela = criar_janela_inicial()
    