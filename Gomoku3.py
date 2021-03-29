#!/usr/local/bin/python3
# /usr/bin/python3
# Set the path to your python3 above

from gtp_connection import GtpConnection
from board_util import GoBoardUtil
from board import GoBoard
import numpy as np


class Gomoku():
    def __init__(self):
        """
        Gomoku player that selects moves randomly from the set of legal moves.
        Passes/resigns only at the end of the game.

        Parameters
        ----------
        name : str
            name of the player (used by the GTP interface).
        version : float
            version number (used by the GTP interface).
        """
        self.numSimulations = 10
        self.name = "GomokuAssignment3"
        self.version = 1.0

    def get_move(self, board, color):
        
        return GoBoardUtil.generate_random_move(board, color)
    
    def simulate(self, board, move, color):
        num_wins = 0
        color_opponent = GoBoardUtil.opponent(color)
        for _ in range(self.numSimulations):
            simulation_result = board.uniform_random_simulation(board, move, color)
            if simulation_result == color:
                num_wins += 1
        return num_wins


    def play_game(self, board, color):
        num_pass = 0
        while (board.detect_five_in_a_row() == board_util.EMPTY || len(board.get_empty_points()) >= 1):
            color = board.current_player
            move = GoBoardUtil.generate_random_move(board, color)
            board.play_move(move, color)
        return board.detect_five_in_a_row()


def run():
    """
    start the gtp connection and wait for commands.
    """
    board = GoBoard(7)
    con = GtpConnection(Gomoku(), board)
    con.start_connection()


if __name__ == "__main__":
    run()
