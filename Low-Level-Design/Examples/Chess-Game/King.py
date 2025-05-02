from Piece import Piece

class King(Piece):

    def canMove(self, board, dest_row, dest_col):
        row_diff = abs(dest_row - self.row)
        col_diff = abs(dest_col - self.col)
        return row_diff <= 1 and col_diff <= 1 
    
    # Check the destination row and column with self i.e. current, if distance greater than 1, it will return false stating invalid move
