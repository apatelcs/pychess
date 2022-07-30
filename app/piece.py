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
    col: int -> col coordinate of the piece
    '''
    def __init__(self, name: str, side: str, row: int, col: int) -> None:
        '''
        Sets attributes to given parameters

        Parameters
        ----------
        name: str -> letter representation of the piece
        side: str -> letter representation of the side the piece belongs to
        row: int -> row coordinate of the piece
        col: int -> col coordinate of the piece
        '''
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
        self.name = name
        self.side = side
        self.row = row
        self.col = col