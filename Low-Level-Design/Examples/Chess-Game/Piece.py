from abc import ABC, abstractmethod
from Color import Color

class Piece(ABC):
    
    # Constructor initializes color and current position on the board
    def __init__(self, color, row, col):
        self.color = Color
        self.row = row
        self.col = col

    @abstractmethod
    def canMove(self, board, dest_row, dest_col):
        pass
        
