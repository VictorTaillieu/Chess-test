import PySimpleGUI as sg
import json
import chess
import chess.svg
from cairosvg import svg2png

# Read the JSON file
with open("data.json", 'r') as file:
    data = json.load(file)

# ----- Full layout -----
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

window = sg.Window("Echecs : le Test", layout, finalize=True)


def update_question(question):
    window["-QUESTION-"].update(f"Question {question + 1}")

    # Create a board
    board = chess.Board(data[question]["fen"])
    board_svg = chess.svg.board(board, orientation=board.turn)
    board_png = svg2png(bytestring=board_svg)
    window["-IMAGE-"].update(data=board_png)

    q1 = data[question]["questions"][0]
    q2 = data[question]["questions"][1]

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


def get_score(question, values):
    q1 = data[question]["questions"][0]
    q2 = data[question]["questions"][1]

    a1 = values["-A1-"] * q1["propositions"][0]["score"]
    b1 = values["-B1-"] * q1["propositions"][1]["score"]
    c1 = values["-C1-"] * q1["propositions"][2]["score"]
    d1 = values["-D1-"] * q1["propositions"][3]["score"]

    a2 = values["-A2-"] * q2["propositions"][0]["score"]
    b2 = values["-B2-"] * q2["propositions"][1]["score"]
    c2 = values["-C2-"] * q2["propositions"][2]["score"]
    d2 = values["-D2-"] * q2["propositions"][3]["score"]

    return a1 + b1 + c1 + d1 + a2 + b2 + c2 + d2


question = 0
score = 0
update_question(question)

# Run the Event Loop
while True:
    event, values = window.read()
    if event == "Exit" or event == sg.WIN_CLOSED:
        break
    elif event == "-VALIDER-":
        score += get_score(question, values)

        question += 1

        if question == len(data):
            sg.popup(f"Votre score est de {score} points.")
        else:
            update_question(question)

window.close()
