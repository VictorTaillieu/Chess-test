import pickle
from random import randint
from os.path import exists

import PySimpleGUI as sg

from actions import main_layout, next_position, quiz_layout
from scores import get_position_score
from utils import load_data

# Load questions data
data = load_data()

# Initialize variables
close = False
choice = ""
position = 0
score = []

# Display home window
home = main_layout()

# Run home event loop
while True:
    event, values = home.read()
    if event == "Exit" or event == sg.WIN_CLOSED:
        close = True
        break
    elif event == "-SHORT-":
        choice = "short"
        short_index = randint(0, 9)
        data = data[short_index * 10:(short_index + 1) * 10]
        break
    elif event == "-LONG-":
        choice = "long"
        break
    elif event == "-LOAD-":
        choice = "long"
        if exists("save.pkl"):
            score = pickle.load(open("save.pkl", "rb"))
            position = len(score) // 2
            break
        else:
            sg.popup("Aucune sauvegarde n'a été trouvée")

home.close()

if not close:
    # Display quiz window
    quiz = quiz_layout()

    next_position(quiz, data, position)

    # Run quiz event loop
    while True:
        event, values = quiz.read()
        if event == "Exit" or event == sg.WIN_CLOSED:
            break
        elif event == "-VALIDER-":
            s1, s2 = get_position_score(data[position]["questions"], values)
            score.extend([s1, s2])

            position += 1

            if choice == "long":
                pickle.dump(score, open("save.pkl", "wb"))

            if position == len(data):
                sg.popup(f"Votre score est de {score} points.")
            else:
                next_position(quiz, data, position)

    quiz.close()
