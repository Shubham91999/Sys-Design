from Piece import Piece

class Knight(Piece):

    def canMove(self, board, dest_row, dest_col):
        row_diff = abs(dest_row - self.row)
        col_diff = abs(dest_col - self.col)

        # Check -> Two steps in one direction, one step in the other (L-shape)
        return (row_diff == 2 and col_diff == 1) or (row_diff == 1 and col_diff == 1 and col_diff == 2)
    

        # Improved Implementation -> Preventing capturing a piece of same color at the destination
        if not ((row_diff == 2 and col_diff == 1) or (row_diff == 1 and col_diff == 2)):
            return False
        
        dest_piece = board.get_piece(dest_row, dest_col)
        if dest_piece is not None and dest_piece.color == self.color:
            return False
        return True
    
        