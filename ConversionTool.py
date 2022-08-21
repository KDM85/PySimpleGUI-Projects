import PySimpleGUI as sg

sg.theme("DarkGrey15")

arrLenImp = ["th", "bc", "in", "h", "ft", "yd", "ftm", "ch", "fur", "mi", "nmi", "lea"]
arrLenMet = ["mm", "cm", "dm", "m", "dam", "hm", "km"]
arrWtImp = ["gr", "dr", "oz", "lb", "st", "qtr", "cwt-l", "cwt-s", "t-l", "t-s"]
arrWtMet = ["mg", "cg", "dg", "g", "dag", "hg", "kg"]
arrVolImp = ["fl oz", "gi", "pt", "qt", "gal"]
arrVolMet = ["ml", "cl", "dl", "l", "dal", "hl", "kl"]


def convert(dblValue, strType, strInUnit, strOutUnit):
    match strType:
        case "Distance":
            arrTable = arrLenImp
            dblMultiplier = 25.4

        case "Mass":
            arrTable = arrWtImp
            dblMultiplier = 453592.37

        case "Volume":
            arrTable = arrVolImp
            dblMultiplier = 28.4130625

    for i in range(0, len(arrTable)):
        if strInUnit == arrTable[i]:
            bIsFromImperial = True
            break
        else:
            bIsFromImperial = False

    for j in range(0, len(arrTable)):
        if strOutUnit == arrTable[j]:
            bIsToImperial = True
            break
        else:
            bIsToImperial = False

    if bIsFromImperial and not bIsToImperial:
        dblConversion = dblMultiplier
    elif not bIsFromImperial and bIsToImperial:
        dblConversion = 1 / dblMultiplier
    elif (bIsFromImperial and bIsToImperial) or (
        not bIsFromImperial and not bIsToImperial
    ):
        dblConversion = 1

    match strInUnit:
        case "th":
            dblConversion = dblConversion / 1000
        case "bc":
            dblConversion = dblConversion / 3
        case "in":
            dblConversion = dblConversion
        case "h":
            dblConversion = dblConversion * 4
        case "ft":
            dblConversion = dblConversion * 12
        case "yd":
            dblConversion = dblConversion * 36
        case "ftm":
            dblConversion = dblConversion * 72.9132
        case "ch":
            dblConversion = dblConversion * 792
        case "fur":
            dblConversion = dblConversion * 7920
        case "mi":
            dblConversion = dblConversion * 63360
        case "nmi":
            dblConversion = dblConversion * 72913.2
        case "lea":
            dblConversion = dblConversion * 190080
        case "mm":
            dblConversion = dblConversion
        case "cm":
            dblConversion = dblConversion * 10
        case "dm":
            dblConversion = dblConversion * 100
        case "m":
            dblConversion = dblConversion * 1000
        case "dam":
            dblConversion = dblConversion * 10000
        case "hm":
            dblConversion = dblConversion * 100000
        case "km":
            dblConversion = dblConversion * 1000000
        case "gr":
            dblConversion = dblConversion / 7000
        case "dr":
            dblConversion = dblConversion / 256
        case "oz":
            dblConversion = dblConversion / 16
        case "lb":
            dblConversion = dblConversion
        case "st":
            dblConversion = dblConversion * 14
        case "qtr":
            dblConversion = dblConversion * 28
        case "cwt-l":
            dblConversion = dblConversion * 112
        case "cwt-s":
            dblConversion = dblConversion * 100
        case "t-l":
            dblConversion = dblConversion * 2240
        case "t-s":
            dblConversion = dblConversion * 2000
        case "mg":
            dblConversion = dblConversion
        case "cg":
            dblConversion = dblConversion * 10
        case "dg":
            dblConversion = dblConversion * 100
        case "g":
            dblConversion = dblConversion * 1000
        case "dag":
            dblConversion = dblConversion * 10000
        case "hg":
            dblConversion = dblConversion * 100000
        case "kg":
            dblConversion = dblConversion * 1000000
        case "fl oz":
            dblConversion = dblConversion
        case "gi":
            dblConversion = dblConversion * 5
        case "pt":
            dblConversion = dblConversion * 20
        case "qt":
            dblConversion = dblConversion * 40
        case "gal":
            dblConversion = dblConversion * 160
        case "ml":
            dblConversion = dblConversion
        case "cg":
            dblConversion = dblConversion * 10
        case "dl":
            dblConversion = dblConversion * 100
        case "l":
            dblConversion = dblConversion * 1000
        case "dal":
            dblConversion = dblConversion * 10000
        case "hl":
            dblConversion = dblConversion * 100000
        case "kl":
            dblConversion = dblConversion * 1000000

    match strOutUnit:
        case "th":
            dblConversion = dblConversion * 1000
        case "bc":
            dblConversion = dblConversion * 3
        case "in":
            dblConversion = dblConversion
        case "h":
            dblConversion = dblConversion / 4
        case "ft":
            dblConversion = dblConversion / 12
        case "yd":
            dblConversion = dblConversion / 36
        case "ftm":
            dblConversion = dblConversion / 72.9132
        case "ch":
            dblConversion = dblConversion / 792
        case "fur":
            dblConversion = dblConversion / 7920
        case "mi":
            dblConversion = dblConversion / 63360
        case "nmi":
            dblConversion = dblConversion / 72913.2
        case "lea":
            dblConversion = dblConversion / 190080
        case "mm":
            dblConversion = dblConversion
        case "cm":
            dblConversion = dblConversion / 10
        case "dm":
            dblConversion = dblConversion / 100
        case "m":
            dblConversion = dblConversion / 1000
        case "dam":
            dblConversion = dblConversion / 10000
        case "hm":
            dblConversion = dblConversion / 100000
        case "km":
            dblConversion = dblConversion / 1000000
        case "gr":
            dblConversion = dblConversion * 7000
        case "dr":
            dblConversion = dblConversion * 256
        case "oz":
            dblConversion = dblConversion * 16
        case "lb":
            dblConversion = dblConversion
        case "st":
            dblConversion = dblConversion / 14
        case "qtr":
            dblConversion = dblConversion / 28
        case "cwt-l":
            dblConversion = dblConversion / 112
        case "cwt-s":
            dblConversion = dblConversion / 100
        case "t-l":
            dblConversion = dblConversion / 2240
        case "t-s":
            dblConversion = dblConversion / 2000
        case "mg":
            dblConversion = dblConversion
        case "cg":
            dblConversion = dblConversion / 10
        case "dg":
            dblConversion = dblConversion / 100
        case "g":
            dblConversion = dblConversion / 1000
        case "dag":
            dblConversion = dblConversion / 10000
        case "hg":
            dblConversion = dblConversion / 100000
        case "kg":
            dblConversion = dblConversion / 1000000
        case "fl oz":
            dblConversion = dblConversion
        case "gi":
            dblConversion = dblConversion / 5
        case "pt":
            dblConversion = dblConversion / 20
        case "qt":
            dblConversion = dblConversion / 40
        case "gal":
            dblConversion = dblConversion / 160
        case "ml":
            dblConversion = dblConversion
        case "cl":
            dblConversion = dblConversion / 10
        case "dl":
            dblConversion = dblConversion / 100
        case "l":
            dblConversion = dblConversion / 1000
        case "dal":
            dblConversion = dblConversion / 10000
        case "hl":
            dblConversion = dblConversion / 100000
        case "kl":
            dblConversion = dblConversion / 1000000

    return round(dblValue * dblConversion, 4)


arrChoice = []
for i in range(0, len(arrLenImp)):
    arrChoice.append(arrLenImp[i])
for j in range(0, len(arrLenMet)):
    arrChoice.append(arrLenMet[j])

layout = [
    [
        sg.Combo(
            ["Distance", "Mass", "Volume"],
            key="cboChoice",
            size=(30, 1),
            default_value="Distance",
            enable_events=True,
        )
    ],
    [
        sg.Text("Input:", size=(10, 1)),
        sg.InputText(key="dblInput", size=(25, 1), enable_events=True),
        sg.Combo(
            arrChoice,
            key="strFromUnit",
            default_value="ft",
        ),
    ],
    [
        sg.Text("Output:", size=(10, 1), key="strOutput"),
        sg.Text(key="dblOutput", size=(25, 1)),
        sg.Combo(
            arrChoice,
            key="strToUnit",
            default_value="m",
        ),
    ],
    [sg.Button("Convert", key="btnConvert")],
]

window = sg.Window("Conversion Tool", layout, element_justification="c")

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break

    if (
        event == "dblInput"
        and values["dblInput"]
        and values["dblInput"][-1] not in ("0123456789.")
    ):
        window["dblInput"].update(values["dblInput"][:-1])

    if event == "cboChoice":
        if values["cboChoice"] == "Distance":
            arrChoice = []
            for i in range(0, len(arrLenImp)):
                arrChoice.append(arrLenImp[i])
            for j in range(0, len(arrLenMet)):
                arrChoice.append(arrLenMet[j])
            window["strFromUnit"].update(values=arrChoice, value="ft")
            window["strToUnit"].update(values=arrChoice, value="m")
        elif values["cboChoice"] == "Mass":
            arrChoice = []
            for i in range(0, len(arrWtImp)):
                arrChoice.append(arrWtImp[i])
            for j in range(0, len(arrWtMet)):
                arrChoice.append(arrWtMet[j])
            window["strFromUnit"].update(values=arrChoice, value="lb")
            window["strToUnit"].update(values=arrChoice, value="kg")
        elif values["cboChoice"] == "Volume":
            arrChoice = []
            for i in range(0, len(arrVolImp)):
                arrChoice.append(arrVolImp[i])
            for j in range(0, len(arrVolMet)):
                arrChoice.append(arrVolMet[j])
            window["strFromUnit"].update(values=arrChoice, value="fl oz")
            window["strToUnit"].update(values=arrChoice, value="ml")
        window["dblInput"].update(value="")
        window["dblOutput"].update(value="")

    if event == "btnConvert" and values["dblInput"]:
        dblValue = values["dblInput"]
        try:
            dblConversion = convert(
                float(values["dblInput"]),
                values["cboChoice"],
                values["strFromUnit"],
                values["strToUnit"],
            )

            window["dblOutput"].update(value=dblConversion)
        except:
            window["dblOutput"].update(value="Invalid Input")

window.close()
