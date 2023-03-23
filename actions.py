from utils import fen_to_png


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
