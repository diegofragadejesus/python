import PySimpleGUI as sg

def criar_janela():
    # Definir o layout da janela
    layout = [
        [sg.Input(size=(20, 1), key='-DISPLAY-', justification='right')],
        [sg.Button('1'), sg.Button('2'), sg.Button('3'), sg.Button('+')],
        [sg.Button('4'), sg.Button('5'), sg.Button('6'), sg.Button('-')],
        [sg.Button('7'), sg.Button('8'), sg.Button('9'), sg.Button('*')],
        [sg.Button('0'), sg.Button('C'), sg.Button('='), sg.Button('/')]
    ]

    # Criar a janela
    janela = sg.Window('Calculadora', layout, return_keyboard_events=True)

    return janela

def main():
    janela = criar_janela()
    expressao = ''

    while True:
        event, values = janela.read()

        if event in (sg.WIN_CLOSED, 'Exit'):
            break
        elif event == 'C':
            expressao = ''
        elif event == '=':
            try:
                expressao = str(eval(expressao))
            except:
                expressao = 'Erro'
        else:
            expressao += event

        # Atualizar o visor com a expressão
        janela['-DISPLAY-'].update(expressao)

    janela.close()

if __name__ == '__main__':
    main()
