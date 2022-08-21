import PySimpleGUI as sg


def setTheme(mode):
    theme = "DarkGrey15"
    match mode:
        case "Dark Mode":
            theme = "DarkGrey15"
        case "Light Mode":
            theme = "LightGrey1"
    sg.theme(theme)
    sg.set_options(font="Calibri 16")

    layout = [
        [
            sg.Text(
                key="Input",
                font="Calibri 20",
                justification="right",
                expand_x=True,
                right_click_menu=themes,
            )
        ],
        [
            sg.InputText(
                key="Output",
                font="Calibri 28",
                size=(15, 1),
                justification="right",
                enable_events=True,
                expand_x=True,
                right_click_menu=themes,
            )
        ],
        [
            sg.Button(
                "⌫",
                key="Back",
                size=(4, 2),
                button_color=("black" if mode == "Dark Mode" else "white", "orange"),
            ),
            sg.Button("(", key="(", size=(4, 2)),
            sg.Button(")", key=")", size=(4, 2)),
            sg.Button("mod", key="%", size=(4, 2)),
        ],
        [
            sg.Button("7", key="7", size=(4, 2)),
            sg.Button("8", key="8", size=(4, 2)),
            sg.Button("9", key="9", size=(4, 2)),
            sg.Button("÷", key="/", size=(4, 2)),
        ],
        [
            sg.Button("4", key="4", size=(4, 2)),
            sg.Button("5", key="5", size=(4, 2)),
            sg.Button("6", key="6", size=(4, 2)),
            sg.Button("×", key="*", size=(4, 2)),
            sg.Button("xʸ", key="**", size=(4, 2)),
        ],
        [
            sg.Button("1", key="1", size=(4, 2)),
            sg.Button("2", key="2", size=(4, 2)),
            sg.Button("3", key="3", size=(4, 2)),
            sg.Button("-", key="-", size=(4, 2)),
            sg.Button(
                "clr",
                key="Clear",
                size=(4, 2),
                button_color=("black" if mode == "Dark Mode" else "white", "red"),
            ),
        ],
        [
            sg.Button("0", key="0", size=(4, 2)),
            sg.Button(".", key=".", size=(4, 2)),
            sg.Button("%", key="pct", size=(4, 2)),
            sg.Button("+", key="+", size=(4, 2)),
            sg.Button(
                "=",
                key="Equal",
                size=(4, 2),
                button_color=("black" if mode == "Dark Mode" else "white", "green"),
                bind_return_key=True,
            ),
        ],
    ]

    return sg.Window("Calculator", layout)


themes = ["Select Theme", ["Dark Mode", "Light Mode"]]
window = setTheme("Dark Mode")

currentNumber = []
operation = []
overwrite = False

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break

    if event in themes[1]:
        window.close()
        window = setTheme(event)

    if event in ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "."]:
        currentNumber.append(event)
        strNumber = "".join(currentNumber)
        window["Output"].update(strNumber)
        overwrite = False

    if event in ["/", "*", "-", "+", "%", "**"]:
        if overwrite:
            operation = operation[:-1]
            window["Input"].update("".join(operation))
        operation.append("".join(currentNumber))
        currentNumber = []
        operation.append(event)
        window["Output"].update("")
        window["Input"].update("".join(operation))
        overwrite = True

    if event in ["(", ")"]:
        operation.append("".join(currentNumber))
        currentNumber = []
        operation.append(event)
        window["Output"].update("")
        window["Input"].update("".join(operation))
        overwrite = False

    if event == "pct":
        operation.append("".join(currentNumber))
        currentNumber = []
        operation.append("/100")
        window["Output"].update("")
        window["Input"].update("".join(operation))
        overwrite = False

    if event == "Back":
        if values["Output"]:
            window["Output"].update(values["Output"][:-1])
            currentNumber = currentNumber[:-1]
        else:
            operation = operation[:-1]
            window["Input"].update("".join(operation))

    if event == "Equal":
        if not values["Output"]:
            pass
        else:
            if not currentNumber:
                currentNumber.append(values["Output"])
            operation.append("".join(currentNumber))
            try:
                result = eval("".join(operation))
                window["Input"].update("".join(operation))
                window["Output"].update(result)
                currentNumber = []
                operation = []
                currentNumber.append(str(result))
            except Exception as Error:
                sg.popup(str(Error).title(), title="Error")

    if event == "Clear":
        currentNumber = []
        operation = []
        window["Input"].update("")
        window["Output"].update("")

window.close()
