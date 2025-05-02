from Piece import Piece

class Queen(Piece):
    def canMove(self, board, dest_row, dest_col):
        row_diff = abs(dest_row - self.row)
        col_diff = abs(dest_col - self.col)

        return (row_diff == col_diff) or (self.row == dest_row or self.col == dest_col)
    
    # (row_diff == col_diff) -> checks the diagonal move
    # (self.row == dest_row or self.col == dest_col) -> checks the horizontal & vertical movements like a rook

    # Code to check path clearance and destination legality -> can't move to a square with a friendly piece
    '''
        if self.row == dest_row:
            # Moving horizontally
            step = 1 if dest_col > self.col else -1
            for c in range(self.col + step, dest_col, step):
                if board.get_piece(self.row, c) is not None:
                    return False

        elif self.col == dest_col:
            # Moving vertically
            step = 1 if dest_row > self.row else -1
            for r in range(self.row + step, dest_row, step):
                if board.get_piece(r, self.col) is not None:
                    return False

        elif abs(dest_row - self.row) == abs(dest_col - self.col):
            # Moving diagonally
            row_step = 1 if dest_row > self.row else -1
            col_step = 1 if dest_col > self.col else -1
            r, c = self.row + row_step, self.col + col_step
            while r != dest_row and c != dest_col:
                if board.get_piece(r, c) is not None:
                    return False
                r += row_step
                c += col_step
        else:
            return False

        # Can't capture own piece
        dest_piece = board.get_piece(dest_row, dest_col)
        if dest_piece is not None and dest_piece.color == self.color:
            return False

        return True

    '''
        
        
        