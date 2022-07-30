ACCEPTED_NAMES = ['P', 'R', 'N', 'B', 'K', 'Q']
ACCEPTED_SIDES = ['W', 'B']

class Piece:
    '''
    Class for chess pieces

    Attributes
    ----------
    name: str -> letter representation of the piece
    side: str -> letter representation of the side the piece belongs to
    '''
    def __init__(self, name: str, side: str) -> None:
        '''
        Sets attributes to given parameters

        Parameters
        ----------
        name: str -> letter representation of the piece
        side: str -> letter representation of the side the piece belongs to
        '''
        if not isinstance(name, str):
            raise TypeError('Piece name is not a string', name)
        if not isinstance(side, str):
            raise TypeError('Piece side is not a string', side)
        if name not in ACCEPTED_NAMES:
            raise ValueError('Nonvalid piece name', name)
        if side not in ACCEPTED_SIDES:
            raise ValueError('Nonvalid piece side', side)
        self.name = name
        self.side = side