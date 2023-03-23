import PySimpleGUI as sg
from PIL import Image, ImageTk

from utils import fen_to_png


def main_layout():
    layout = [
        [sg.Text(key="-TITLE-", font=("Helvetica", 20))],
        [sg.Image(key="-IMAGE-")],

        [sg.Button("Test rapide", key="-SHORT-")],
        [sg.Button("Test complet", key="-LONG-")],
        [sg.Button("Reprendre", key="-LOAD-")]

    ]

    window = sg.Window("Echecs : le test", layout, finalize=True, element_justification="center")
    window["-IMAGE-"].update(data=ImageTk.PhotoImage(Image.open("book_cover.jpg")))

    return window


def quiz_layout():
    layout = [
        [sg.Text(key="-QUESTION-", font=("Helvetica", 20))],
        [sg.Image(key="-IMAGE-")],

        [sg.Text(key="-QUESTION1-", font=("Helvetica", 20))],

        [sg.Radio("A", "Q1", key="-A1-", font=("Helvetica", 12))],
        [sg.Radio("B", "Q1", key="-B1-", font=("Helvetica", 12))],
        [sg.Radio("C", "Q1", key="-C1-", font=("Helvetica", 12))],
        [sg.Radio("D", "Q1", key="-D1-", font=("Helvetica", 12))],

        [sg.Text(key="-QUESTION2-", font=("Helvetica", 20))],

        [sg.Radio("A", "Q2", key="-A2-", font=("Helvetica", 12))],
        [sg.Radio("B", "Q2", key="-B2-", font=("Helvetica", 12))],
        [sg.Radio("C", "Q2", key="-C2-", font=("Helvetica", 12))],
        [sg.Radio("D", "Q2", key="-D2-", font=("Helvetica", 12))],

        [sg.Button("Valider", key="-VALIDER-")]
    ]

    return sg.Window("Echecs : le test", layout, finalize=True)


def next_position(window, data, position):
    window["-QUESTION-"].update(f"Question {position + 1}")

    # Update board
    board = fen_to_png(data[position]["fen"])
    window["-IMAGE-"].update(data=board)

    q1 = data[position]["questions"][0]
    q2 = data[position]["questions"][1]

    window["-QUESTION1-"].update(q1["question"])
    window["-A1-"].update(text=q1["propositions"][0]["proposition"], value=False)
    window["-B1-"].update(text=q1["propositions"][1]["proposition"], value=False)
    window["-C1-"].update(text=q1["propositions"][2]["proposition"], value=False)
    window["-D1-"].update(text=q1["propositions"][3]["proposition"], value=False)

    window["-QUESTION2-"].update(q2["question"])
    window["-A2-"].update(text=q2["propositions"][0]["proposition"], value=False)
    window["-B2-"].update(text=q2["propositions"][1]["proposition"], value=False)
    window["-C2-"].update(text=q2["propositions"][2]["proposition"], value=False)
    window["-D2-"].update(text=q2["propositions"][3]["proposition"], value=False)
