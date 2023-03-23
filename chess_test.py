import PySimpleGUI as sg

from actions import main_layout, next_position, quiz_layout
from scores import get_position_score
from utils import load_data

# Load questions data
data = load_data()

# Display home window
home = main_layout()

# Run the event loop
while True:
    event, values = home.read()
    if event == "Exit" or event == sg.WIN_CLOSED:
        break
    elif event == "-SHORT-":
        break
    elif event == "-LONG-":
        break
    elif event == "-LOAD-":
        break

home.close()

quiz = quiz_layout()

position = 0
score = []
next_position(quiz, data, position)

# Run the event loop
while True:
    event, values = quiz.read()
    if event == "Exit" or event == sg.WIN_CLOSED:
        break
    elif event == "-VALIDER-":
        s1, s2 = get_position_score(data[position]["questions"], values)
        score.extend([s1, s2])

        position += 1

        if position == len(data):
            sg.popup(f"Votre score est de {score} points.")
        else:
            next_position(quiz, data, position)

quiz.close()
