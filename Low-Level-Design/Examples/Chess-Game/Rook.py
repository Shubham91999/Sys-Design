from Piece import Piece

class Rook(Piece):
    def canMove(self, board, dest_row, dest_col):
        return dest_row == self.row or dest_col == self.col
    
    # dest_row == self.row -> Means the rook is moving horizontally
    # dest_col == self.col -> Means the rook is moving vertically

        """
        if self.row != dest_row and self.col != dest_col:
            return False
        
        # Horizontal Move
        if self.row == dest_row:
            if dest_col > self.col:
                step = 1
            else:
                step = -1
            for c in range(self.col + step, dest_col, step):
                if board.get_piece(self.row, c) is not None:
                    return False
        
        # Vertical Move
        else:
            if dest_row > self.row:
                step = 1
            else:
                step = -1
            for r in range(self.row + step, dest_row, step):
                if board.get_piece(r, self.col) is not None:
                    return False
                
        # Final check: can't capture own piece
        dest_piece = board.get_piece(dest_row, dest_col)
        if dest_piece is not None and dest_piece.color == self.color:
            return False
        return True
        
        """
                
        