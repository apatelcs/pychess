ACCEPTED_NAMES = ['P', 'R', 'N', 'B', 'K', 'Q']
ACCEPTED_SIDES = ['W', 'B']

class Piece:
    '''
    Class for chess pieces

    Attributes
    ----------
    name: str -> letter representation of the piece
    side: str -> letter representation of the side the piece belongs to
    row: int -> row coordinate of the piece
    col: int -> column coordinate of the piece
    '''
    def __init__(self, name: str, side: str, row: int, col: int) -> None:
        '''
        Sets attributes to given parameters

        Parameters
        ----------
        name: str -> letter representation of the piece
        side: str -> letter representation of the side the piece belongs to
        row: int -> row coordinate of the piece
        col: int -> column coordinate of the piece
        '''
        # Validity checks
        if not isinstance(name, str):
            raise TypeError('Piece name is not a string', name)
        if not isinstance(side, str):
            raise TypeError('Piece side is not a string', side)
        if not isinstance(row, int):
            raise TypeError('Piece row is not an integer', row)
        if not isinstance(col, int):
            raise TypeError('Piece column is not an integer', col)
        if name not in ACCEPTED_NAMES:
            raise ValueError('Nonvalid piece name', name)
        if side not in ACCEPTED_SIDES:
            raise ValueError('Nonvalid piece side', side)
        if row not in range(8):
            raise ValueError('Nonvalid row value', row)
        if col not in range(8):
            raise ValueError('Nonvalid col value', col)
        # Assign attribute values
        self.name = name
        self.side = side
        self.row = row
        self.col = col

    
    def move(self, target_row: int, target_col: int) -> None:
        '''
        Updates row and col attributes of current piece to move it according to piece name

        Parameters
        ----------
        target_row: int -> new row
        target_col: int -> new column
        '''
        # Check if new position is inside the board
        if target_row not in range(8) or target_col not in range(8):
            raise ValueError('Tried to move piece off the board')
        # Validity checks according to piece name and side
        allowed_moves = []
        # Pawns can move forward by one
        if self.name == 'P':
            if self.side == 'W':
                allowed_moves.append((self.row + 1, self.col))
            else:
                allowed_moves.append((self.row - 1, self.col))
        # Rooks can move vertically or horizontally
        elif self.name == 'R':
            if target_row != self.row and target_col != self.col:
                raise ValueError('Tried to move rook diagonally')
            elif target_row == self.row:
                allowed_moves += [(self.row, c) for c in range(8)]
            else:
                allowed_moves += [(r, self.col) for r in range(8)]
        # Knights can move in L patterns
        elif self.name == 'N':
            valid_knight_moves = [(self.row + 2, self.col - 1), (self.row + 2, self.col + 1),
                                  (self.row - 2, self.col - 1), (self.row - 2, self.col + 1),
                                  (self.row + 1, self.col - 2), (self.row - 1, self.col - 2),
                                  (self.row + 1, self.col + 2), (self.row - 1, self.col + 2)]
            allowed_moves += valid_knight_moves
        # Bishops can move diagonally
        elif self.name == 'B':
            valid_bishop_moves = [(self.row, self.col)]
            r = self.row + 1
            c = self.col - 1
            while r in range(8) and c in range(8):
                valid_bishop_moves.append((r, c))
                r += 1
                c -= 1
            r = self.row + 1
            c = self.col + 1
            while r in range(8) and c in range(8):
                valid_bishop_moves.append((r, c))
                r += 1
                c += 1
            r = self.row - 1
            c = self.col + 1
            while r in range(8) and c in range(8):
                valid_bishop_moves.append((r, c))
                r -= 1
                c += 1
            r = self.row - 1
            c = self.col - 1
            while r in range(8) and c in range(8):
                valid_bishop_moves.append((r, c))
                r -= 1
                c -= 1
            allowed_moves += valid_bishop_moves
        # Kings can move by 1 space diagonally, horizontally, or vertically
        elif self.name == 'K':
            valid_king_moves = [(self.row + 1, self.col), (self.row - 1, self.col),
                                (self.row, self.col + 1), (self.row, self.col - 1),
                                (self.row + 1, self.col + 1), (self.row + 1, self.col - 1),
                                (self.row - 1, self.col + 1), (self.row - 1, self.col - 1)]
            allowed_moves += valid_king_moves
        # Queens can move diagonally, horizontally, or vertically
        else:
            valid_queen_moves = []
            r = self.row + 1
            c = self.col - 1
            while r in range(8) and c in range(8):
                valid_queen_moves.append((r, c))
                r += 1
                c -= 1
            r = self.row + 1
            c = self.col + 1
            while r in range(8) and c in range(8):
                valid_queen_moves.append((r, c))
                r += 1
                c += 1
            r = self.row - 1
            c = self.col + 1
            while r in range(8) and c in range(8):
                valid_queen_moves.append((r, c))
                r -= 1
                c += 1
            r = self.row - 1
            c = self.col - 1
            while r in range(8) and c in range(8):
                valid_queen_moves.append((r, c))
                r -= 1
                c -= 1
            if target_row == self.row:
                valid_queen_moves += [(self.row, c) for c in range(8)]
            elif target_col == self.col:
                valid_queen_moves += [(r, self.col) for r in range(8)]
            allowed_moves += valid_queen_moves
        if (target_row, target_col) not in allowed_moves:
            raise ValueError(f'Tried moving a {self.name} to an invalid postiion')
        # If valid, assign new row/col to row/col attributes
        self.row = target_row
        self.col = target_col