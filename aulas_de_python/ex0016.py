import PySimpleGUI as sg

class telaPythom:
    def __init__(self):
        #layout
        layout = [
            [sg.Text('nome'),sg.Input()],
            [sg.Text('Idade'),sg.Input()],
            [sg.Button('Enviar informação')]
        ]
        #janela
        janela = sg.Window('Dodos do Usuario').layout(layout)
        #Extraindo os dados da tela
        self.button,self.values = janela.Read()

    def Iniciar(self):
        print(self.values)

tela =telaPythom()
tela.Iniciar
