from Piece import Piece

class Bishop(Piece):

    def canMove(self, board, dest_row, dest_col):
        row_diff = abs(dest_row - self.row)
        col_diff = abs(dest_col - self.col)
        return row_diff == col_diff
    
        # Improved Implementation with check for obstruction and preventing illegal move i.e. moving to dest already occupied by same color piece
        if row_diff != col_diff:
            return False
        
        if dest_row > self.row:
            row_step = 1
        else:
            row_step = -1

        if dest_col > self.col:
            col_step = 1
        else:
            col_step = -1

        r = self.row + row_step
        c = self.col + col_step

        while r != dest_row and c != dest_col:
            if board.get_piece(r, c) is not None:
                return False  # Path is blocked
            
            r += row_step
            c += col_step

        # Destination should not contain a friendly piece
        dest_piece = board.get_piece(dest_row, dest_col)
        if dest_piece is not None and dest_piece.color == self.color:
            return False
        return True
        

            
        

    
    
    