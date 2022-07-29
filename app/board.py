from app.piece import Piece

class Board:
    '''
    Class for chess board
    '''
    def __init__(self) -> None:
        '''
        Creates the board object and initializes attributes
        '''
        # Initialize a new chess board
        self.board: list[Piece] = []
        for r in range(8):
            row = []
            if r == 0:
                row = [Piece('R', 'W'), Piece('N', 'W'), Piece('B', 'W'), Piece('K', 'W'),
                        Piece('Q', 'W'), Piece('B', 'W'), Piece('N', 'W'), Piece('R', 'W')]
            elif r == 1:
                row = [Piece('P', 'W'), Piece('P', 'W'), Piece('P', 'W'), Piece('P', 'W'),
                        Piece('P', 'W'), Piece('P', 'W'), Piece('P', 'W'), Piece('P', 'W')]
            elif r == 6:
                row = [Piece('P', 'B'), Piece('P', 'B'), Piece('P', 'B'), Piece('P', 'B'),
                        Piece('P', 'B'), Piece('P', 'B'), Piece('P', 'B'), Piece('P', 'B')]
            elif r == 7:
                row = [Piece('R', 'B'), Piece('N', 'B'), Piece('B', 'B'), Piece('K', 'B'),
                        Piece('Q', 'B'), Piece('B', 'B'), Piece('N', 'B'), Piece('R', 'B')]
            else:
                row = [None, None, None, None, None, None, None, None]
            self.board.append(row)

        # Sets current side to W by default
        self.current_side = 'W'


    def __str__(self) -> str:
        '''
        Creates string representation of the board
        '''
        output_string = ''

        for row in self.board:
            for itm in row:
                if type(itm) == Piece:
                    # Piece name in place of Piece object
                    output_string += itm.name + ' '
                else:
                    # Dash for empty space
                    output_string += '- '
            # Add new line between rows
            output_string += '\n'
        
        return output_string