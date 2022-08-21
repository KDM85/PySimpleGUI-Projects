import matplotlib
import matplotlib.pyplot as plt
import PySimpleGUI as sg
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

tableContent = []


def setTheme(mode):
    match mode:
        case "Dark Mode":
            theme = "DarkGrey15"
            plt.style.use("dark_background")
        case "Light Mode":
            theme = "LightGrey1"
            plt.style.use("default")
    sg.theme(theme)
    sg.set_options(font="Arial 10")

    layout = [
        [
            sg.Table(
                headings=["id", "Result"],
                values=tableContent,
                expand_x=True,
                hide_vertical_scroll=True,
                key="Table",
                enable_events=True,
                right_click_menu=themes,
            )
        ],
        [
            sg.Input(key="Input", expand_x=True, enable_events=True),
            sg.Button("Submit", bind_return_key=True),
        ],
        [sg.Canvas(key="Canvas")],
    ]

    return sg.Window("SimpleGraph", layout, element_justification="c", finalize=True)


themes = ["Select Theme", ["Dark Mode", "Light Mode"]]
mode = "Dark Mode"
window = setTheme(mode)


def updateFigure(data):
    axes = figure.axes
    x = [i[0] for i in data]
    y = [int(i[1]) for i in data]
    axes[0].plot(x, y, color="white" if mode == "Dark Mode" else "black")
    figureCanvasAgg.draw()
    figureCanvasAgg.get_tk_widget().pack()


figure = matplotlib.figure.Figure(figsize=(5, 4))
figure.add_subplot(111).plot([], [])
figureCanvasAgg = FigureCanvasTkAgg(figure, window["Canvas"].TKCanvas)
figureCanvasAgg.draw()
figureCanvasAgg.get_tk_widget().pack()

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break

    if event in themes[1]:
        window.close()
        window = setTheme(event)
        figure = matplotlib.figure.Figure(figsize=(5, 4))
        figure.add_subplot(111).plot([], [])
        figureCanvasAgg = FigureCanvasTkAgg(figure, window["Canvas"].TKCanvas)
        figureCanvasAgg.draw()
        figureCanvasAgg.get_tk_widget().pack()

    if (
        event == "Input"
        and values["Input"]
        and values["Input"][-1] not in ("0123456789.")
    ):
        window["Input"].update(values["Input"][:-1])

    if event == "Submit" and values["Input"]:
        newValue = values["Input"]
        tableContent.append([len(tableContent) + 1, float(newValue)])
        window["Table"].update(tableContent)
        window["Input"].update("")
        updateFigure(tableContent)

window.close()
