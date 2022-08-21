from time import time

import PySimpleGUI as sg


def setTheme(mode):
    theme = "DarkGrey15"
    match mode:
        case "Dark Mode":
            theme = "DarkGrey15"
        case "Light Mode":
            theme = "LightGrey1"
    sg.theme(theme)
    sg.set_options(font="Arial 16")

    layout = [
        [
            sg.Push(),
            sg.Button(
                "X",
                image_subsample=None,
                border_width=None,
                size=(None, None),
                font=("Arial 10"),
                key="btnClose",
                pad=0,
                button_color=("black" if mode == "Dark Mode" else "white", "red"),
                enable_events=True,
            ),
        ],
        [sg.VPush()],
        [
            sg.Text(
                "00:00",
                key="Time",
                font=("Arial_Black 40"),
                enable_events=True,
                right_click_menu=themes,
            )
        ],
        [
            sg.Button(
                "Start",
                key="btnStartStop",
                button_color=("black" if mode == "Dark Mode" else "white", "green"),
            ),
            sg.Button(
                "Lap",
                key="btnLap",
                visible=False,
                button_color=("black" if mode == "Dark Mode" else "white", "red"),
            ),
        ],
        [sg.Column([[]], key="colLaps")],
        [sg.VPush()],
    ]

    return sg.Window(
        "Stopwatch",
        layout,
        no_titlebar=True,
        size=(250, 500),
        element_justification="c",
    )


themes = ["Select Theme", ["Dark Mode", "Light Mode"]]
mode = "Dark Mode"
window = setTheme(mode)
bIsActive = False
startTime = 0
intLap = 0

while True:
    event, values = window.read(timeout=10)
    if event in (sg.WIN_CLOSED, "btnClose"):
        break

    if event in themes[1]:
        if not bIsActive:
            window.close()
            window = setTheme(event)
            mode = event

    if event == "btnStartStop":
        if bIsActive:
            window["btnStartStop"].update(
                "Reset",
                button_color=("black" if mode == "Dark Mode" else "white", "green"),
            )
            window["btnLap"].update(visible=False)
            bIsActive = False
        else:
            if startTime > 0:
                window.close()
                window = setTheme(mode)
                startTime = 0
                intLap = 0
            else:
                window["btnStartStop"].update(
                    "Stop",
                    button_color=("black" if mode == "Dark Mode" else "white", "red"),
                )
                window["btnLap"].update(visible=True)
                bIsActive = True
                startTime = time()

    if bIsActive:
        elapsedTime = round(time() - startTime, 0)
        intMinutes = int(elapsedTime / 60)
        intSeconds = int(elapsedTime - intMinutes * 60)

        if intMinutes >= 10:
            strMinutes = str(intMinutes)
        else:
            strMinutes = "0" + str(intMinutes)

        if intSeconds >= 10:
            strSeconds = str(intSeconds)
        else:
            strSeconds = "0" + str(intSeconds)

        strTime = strMinutes + ":" + strSeconds
        window["Time"].update(strTime)

    if event == "btnLap":
        intLap += 1
        window.extend_layout(
            window["colLaps"],
            [[sg.Text("Lap " + str(intLap) + ": " + strTime)]],
        )


window.close()
