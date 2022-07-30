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
        if name not in ACCEPTED_NAMES:
            raise ValueError('Nonvalid piece name', name)
        if side not in ACCEPTED_SIDES:
            raise ValueError('Nonvalid piece side', side)
        self.name = name
        self.side = side