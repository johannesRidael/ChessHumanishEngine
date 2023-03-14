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
    
    location is a tuple where loc[7][0] = a1
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
        # takes a move string, with only XxX or O-O or O-O-O format
        # NO LEGALITY CHECKING

        if self.whiteTurn:
            if move == 'O-O':
                kingX, kingY = self.locFromNotation('e1')
                rookX, rookY = self.locFromNotation('h1')
                self.state[kingX][kingY] = 0
                self.stat[rookX][rookY] = 0
                kingX, kingY = self.locFromNotation('g1')
                rookX, rookY = self.locFromNotation('f1')
                self.state[kingX][kingY] = 6
                self.state[rookX][rookY] = 4
            elif move == 'O-O-O':
                kingX, kingY = self.locFromNotation('e1')
                rookX, rookY = self.locFromNotation('a1')
                self.state[kingX][kingY] = 0
                self.stat[rookX][rookY] = 0
                kingX, kingY = self.locFromNotation('c1')
                rookX, rookY = self.locFromNotation('d1')
                self.state[kingX][kingY] = 6
                self.state[rookX][rookY] = 4
        else:
            if move == 'O-O':
                kingX, kingY = self.locFromNotation('e8')
                rookX, rookY = self.locFromNotation('h8')
                self.state[kingX][kingY] = 0
                self.stat[rookX][rookY] = 0
                kingX, kingY = self.locFromNotation('g8')
                rookX, rookY = self.locFromNotation('f8')
                self.state[kingX][kingY] = 6
                self.state[rookX][rookY] = 4
            elif move == 'O-O-O':
                kingX, kingY = self.locFromNotation('e8')
                rookX, rookY = self.locFromNotation('a8')
                self.state[kingX][kingY] = 0
                self.stat[rookX][rookY] = 0
                kingX, kingY = self.locFromNotation('c8')
                rookX, rookY = self.locFromNotation('d8')
                self.state[kingX][kingY] = 6
                self.state[rookX][rookY] = 4

    @staticmethod
    def locFromNotation(notation : str):
        # takes notation of form (lowercase)letter number(a1) to coordinate on state board
        return 8-int(notation[1]), ord(notation[0].lower()) - 97

    @staticmethod
    def notationFromLoc(loc):
        return str(chr(loc[1] + 97)) + str(8 - loc[0])