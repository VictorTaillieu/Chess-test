import PySimpleGUI as sg

from actions import next_position
from scores import get_position_score
from utils import load_data

# Load questions data
data = load_data()

# Layout
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

window = sg.Window("Echecs : le test", layout, finalize=True)

position = 0
score = []
next_position(window, data, position)

# Run the event loop
while True:
    event, values = window.read()
    if event == "Exit" or event == sg.WIN_CLOSED:
        break
    elif event == "-VALIDER-":
        s1, s2 = get_position_score(data[position]["questions"], values)
        score.extend([s1, s2])

        position += 1

        if position == len(data):
            sg.popup(f"Votre score est de {score} points.")
        else:
            next_position(window, data, position)

window.close()
