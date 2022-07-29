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
        self.name = name
        self.side = side