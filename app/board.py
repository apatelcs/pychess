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
                row = [Piece('R', 'W', r, 0), Piece('N', 'W', r, 1), Piece('B', 'W', r, 2), Piece('K', 'W', r, 3),
                       Piece('Q', 'W', r, 4), Piece('B', 'W', r, 5), Piece('N', 'W', r, 6), Piece('R', 'W', r, 7)]
            elif r == 1:
                row = [Piece('P', 'W', r, 0), Piece('P', 'W', r, 1), Piece('P', 'W', r, 2), Piece('P', 'W', r, 3),
                       Piece('P', 'W', r, 4), Piece('P', 'W', r, 5), Piece('P', 'W', r, 6), Piece('P', 'W', r, 7)]
            elif r == 6:
                row = [Piece('P', 'B', r, 0), Piece('P', 'B', r, 1), Piece('P', 'B', r, 2), Piece('P', 'B', r, 3),
                       Piece('P', 'B', r, 4), Piece('P', 'B', r, 5), Piece('P', 'B', r, 6), Piece('P', 'B', r, 7)]
            elif r == 7:
                row = [Piece('R', 'B', r, 0), Piece('N', 'B', r, 1), Piece('B', 'B', r, 2), Piece('K', 'B', r, 3),
                       Piece('Q', 'B', r, 4), Piece('B', 'B', r, 5), Piece('N', 'B', r, 6), Piece('R', 'B', r, 7)]
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