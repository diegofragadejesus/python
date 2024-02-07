import PySimpleGUI as sg

layout = [
    [sg.Input(size=(20, 1), key="-DISPLAY-", justification="right")],
    *[
        [
            sg.Button(str(i), size=(3, 1))
            for i in range(j * 3 + 1, j * 3 + 4)
        ]
        for j in range(3)
    ],
    [sg.Button("0", size=(3, 1)), sg.Button("+", size=(3, 1))],
    [sg.Button("C", size=(3, 1)), sg.Button("-", size=(3, 1))],
    [sg.Button("*", size=(3, 1)), sg.Button("/", size=(3, 1))],
    [sg.Button("=", size=(6, 1))]
]

window = sg.Window("Calculadora", layout, return_keyboard_events=True)

display_elem = window["-DISPLAY-"]

equation = ""
while True:
    event, values = window.read()

    if event == sg.WINDOW_CLOSED:
        break

    if event == "=":
        try:
            result = eval(equation)
            display_elem.update(value=result)
        except:
            display_elem.update(value="Erro")
        equation = ""

    elif event in "1234567890+-*/":
        equation += event
        display_elem.update(value=equation)

    elif event == "C":
        equation = ""
        display_elem.update(value="")

window.close()
