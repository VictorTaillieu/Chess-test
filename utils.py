import json

import chess
import chess.svg
from cairosvg import svg2png


def load_data():
    with open("data.json", 'r') as file:
        data = json.load(file)

    return data


def fen_to_png(fen):
    board = chess.Board(fen)
    board_svg = chess.svg.board(board, orientation=board.turn)

    return svg2png(bytestring=board_svg)
