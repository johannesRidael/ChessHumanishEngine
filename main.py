import math
class Board:
    state = []
    whitePieces = [[]] * 8
    blackPieces = [[]] * 8
    whiteTurn = True

    """
    Pieces are represented like so, negation means black piece
    0: empty square
    1: Pawn
    2: Knight
    3: Bishop
    4: Rook
    5: Queen
    6: King
    
    location is a tuple where loc[0][0] = a1
    """
    def Board(self):
        self.state = [
            [-4, -2, -3, -5, -6, -3, -2, -4],
            [-1, -1, -1, -1, -1, -1, -1, -1],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [1, 1, 1, 1, 1, 1, 1, 1],
            [4, 2, 3, 5, 6, 3, 2, 4]
        ]
        # starting state of a board
        for i in range(8):
            for j in range(8):
                if self.state[i][j] < 0:
                    self.blackPieces[math.fabs(self.state[i][j])].append((i, j))
                elif self.state[i][j] > 0:
                    self.whitePieces[self.state[i][j]].append((i, j))
        # storing whitePieces locations means we don't need to search all 64 slots for a piece

    def move(self, move):
        # implemented 
