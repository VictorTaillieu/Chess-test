def get_position_score(question, values):
    q1 = question[0]
    q2 = question[1]

    a1 = values["-A1-"] * q1["propositions"][0]["score"]
    b1 = values["-B1-"] * q1["propositions"][1]["score"]
    c1 = values["-C1-"] * q1["propositions"][2]["score"]
    d1 = values["-D1-"] * q1["propositions"][3]["score"]

    a2 = values["-A2-"] * q2["propositions"][0]["score"]
    b2 = values["-B2-"] * q2["propositions"][1]["score"]
    c2 = values["-C2-"] * q2["propositions"][2]["score"]
    d2 = values["-D2-"] * q2["propositions"][3]["score"]

    return a1 + b1 + c1 + d1, a2 + b2 + c2 + d2
