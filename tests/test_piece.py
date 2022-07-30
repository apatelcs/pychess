from random import sample
import pytest
from app.piece import Piece

def test_create_piece() -> None:
    '''
    Tests piece creation
    '''
    sample_piece_name = 'P'
    sample_piece_side = 'W'
    sample_piece_row = 0
    sample_piece_col = 1

    sample_piece = Piece(sample_piece_name, sample_piece_side, sample_piece_row, sample_piece_col)

    assert sample_piece.name == 'P' and sample_piece.side == 'W' and sample_piece.row == 0 and sample_piece.col == 1


def test_valid_names() -> None:
    '''
    Tests if valid name does not raise ValueError
    '''
    for name in ['P', 'R', 'N', 'B', 'K', 'Q']:
        try:
            sample_piece = Piece(name, 'W', 0, 0)
        except ValueError as exc:
            assert False, f'{name} raised a ValueError: {exc}'


def test_name_type_error() -> None:
    '''
    Tests if non-string name raises proper TypeError
    '''
    with pytest.raises(TypeError):
        sample_piece = Piece(False, 'W', 0, 0)


def test_name_value_error() -> None:
    '''
    Tests if invalid name raises proper ValueError
    '''
    with pytest.raises(ValueError):
        sample_piece = Piece('H', 'W', 0, 0)


def test_valid_sides() -> None:
    '''
    Tests if valid side does not raise ValueError
    '''
    for side in ['W', 'B']:
        try:
            sample_piece = Piece('P', side, 0, 0)
        except ValueError as exc:
            assert False, f'{side} raised a ValueError: {exc}'


def test_side_type_error() -> None:
    '''
    Tests if non-string side raises proper TypeError
    '''
    with pytest.raises(TypeError):
        sample_piece = Piece('P', False, 0, 0)


def test_side_value_error() -> None:
    '''
    Tests if invalid side raises proper ValueError
    '''
    with pytest.raises(ValueError):
        sample_piece = Piece('P', 'Y', 0, 0)


def test_valid_rows() -> None:
    '''
    Tests if valid row does not raise ValueError
    '''
    for r in range(8):
        try:
            sample_piece = Piece('P', 'W', r, 0)
        except ValueError as exc:
            assert False, f'{r} raised a ValueError: {exc}'


def test_row_type_error() -> None:
    '''
    Tests if non-integer row raises proper TypeError
    '''
    with pytest.raises(TypeError):
        sample_piece = Piece('P', 'W', '1', 0)


def test_row_value_error() -> None:
    '''
    Tests if invalid row raises proper ValueError
    '''
    with pytest.raises(ValueError):
        sample_piece = Piece('P', 'W', 8, 0)


def test_valid_cols() -> None:
    '''
    Tests if valid col does not raise ValueError
    '''
    for c in range(8):
        try:
            sample_piece = Piece('P', 'W', 0, c)
        except ValueError as exc:
            assert False, f'{c} raised a ValueError: {exc}'


def test_col_type_error() -> None:
    '''
    Tests if non-integer col raises proper TypeError
    '''
    with pytest.raises(TypeError):
        sample_piece = Piece('P', 'W', 0, '1')


def test_col_value_error() -> None:
    '''
    Tests if invalid col raises proper ValueError
    '''
    with pytest.raises(ValueError):
        sample_piece = Piece('P', 'W', 0, 8)


def test_move_off_board() -> None:
    '''
    Tests if ValueError is raised on trying to move piece off the board
    '''
    with pytest.raises(ValueError):
        sample_piece = Piece('P', 'W', 7, 0)
        sample_piece.move(8, 0)


def test_valid_move_pawn() -> None:
    '''
    Tests valid pawn movement
    '''
    sample_piece_w = Piece('P', 'W', 1, 0)
    sample_piece_b = Piece('P', 'B', 6, 0)

    try:
        sample_piece_w.move(2, 0)
        sample_piece_b.move(5, 0)

        assert sample_piece_w.row == 2 and sample_piece_w.col == 0 and sample_piece_b.row == 5 and sample_piece_b.col == 0
    except ValueError as exc:
        assert False, f'Valid pawn move raised a ValueError: {exc}'


def test_invalid_move_pawn_backward_w() -> None:
    '''
    Tests if ValueError is raised when pawn moves backward
    '''
    sample_piece = Piece('P', 'W', 1, 0)
    with pytest.raises(ValueError):
        sample_piece.move(0, 0)


def test_invalid_move_pawn_far_w() -> None:
    '''
    Tests if ValueError is raised when pawn moves too far
    '''
    sample_piece = Piece('P', 'W', 1, 0)
    with pytest.raises(ValueError):
        sample_piece.move(3, 0)


def test_invalid_move_pawn_backward_b() -> None:
    '''
    Tests if ValueError is raised when pawn moves backward
    '''
    sample_piece = Piece('P', 'B', 6, 0)
    with pytest.raises(ValueError):
        sample_piece.move(7, 0)


def test_invalid_move_pawn_far_b() -> None:
    '''
    Tests if ValueError is raised when pawn moves too far
    '''
    sample_piece = Piece('P', 'B', 6, 0)
    with pytest.raises(ValueError):
        sample_piece.move(4, 0)


def test_valid_move_rook() -> None:
    '''
    Tests valid rook movement
    '''
    sample_piece = Piece('R', 'W', 0, 0)
    moves = [(r, 0) for r in range(8)] + [(0, c) for c in range(8)]
    for mv in moves:
        try:
            sample_piece.move(mv[0], mv[1])
            sample_piece.move(0, 0)
        except ValueError as exc:
            assert False, f'Valid rook move raised a ValueError: {exc}'


def test_invalid_move_rook() -> None:
    '''
    Tests if ValueError is raised when rook moves non-vertically/non-horizontally
    '''
    sample_piece = Piece('R', 'W', 0, 0)
    with pytest.raises(ValueError):
        sample_piece.move(1, 1)


def test_valid_move_knight() -> None:
    '''
    Tests valid knight movement
    '''
    sample_piece = Piece('N', 'W', 2, 2)
    moves = [(4, 1), (4, 3), (0, 1), (0, 3), (3, 4), (1, 4), (3, 0), (1, 0)]
    for mv in moves:
        try:
            sample_piece.move(mv[0], mv[1])
            sample_piece.move(2, 2)
        except ValueError as exc:
            assert False, f'Valid knight move raised a ValueError: {exc}'


def test_invalid_move_knight() -> None:
    '''
    Tests if ValueError is raised when knight moves in non-L pattern
    '''
    sample_piece = Piece('N', 'W', 2, 2)
    with pytest.raises(ValueError):
        sample_piece.move(3, 2)


def test_valid_move_bishop() -> None:
    '''
    Tests valid bishop movement
    '''
    sample_piece = Piece('B', 'W', 0, 0)
    moves = [(i, i) for i in range(8)]
    for mv in moves:
        try:
            sample_piece.move(mv[0], mv[1])
            sample_piece.move(0, 0)
        except ValueError as exc:
            assert False, f'Valid bishop move raised a ValueError: {exc}'


def test_invalid_move_bishop() -> None:
    '''
    Tests if ValueError is raised when bishop moves non-diagonally
    '''
    sample_piece = Piece('B', 'W', 0, 0)
    with pytest.raises(ValueError):
        sample_piece.move(1, 0)


def test_valid_move_king() -> None:
    '''
    Tests valid king movement
    '''
    sample_piece = Piece('K', 'W', 1, 1)
    moves = [(sample_piece.row - 1, sample_piece.col), (sample_piece.row + 1, sample_piece.col),
             (sample_piece.row, sample_piece.col - 1), (sample_piece.row, sample_piece.col + 1),
             (sample_piece.row - 1, sample_piece.col - 1), (sample_piece.row - 1, sample_piece.col + 1),
             (sample_piece.row + 1, sample_piece.col - 1), (sample_piece.row + 1, sample_piece.col + 1)]
    for mv in moves:
        try:
            sample_piece.move(mv[0], mv[1])
            sample_piece.move(1, 1)
        except ValueError as exc:
            assert False, f'Valid king move raised a ValueError: {exc}'


def test_invalid_move_king() -> None:
    '''
    Tests if ValueError is raised when king moves non-vertically/non-horizontally/non-diagonally
    '''
    sample_piece = Piece('K', 'W', 1, 1)
    with pytest.raises(ValueError):
        sample_piece.move(3, 0)


def test_valid_move_queen() -> None:
    '''
    Tests valid queen movement
    '''
    sample_piece = Piece('Q', 'W', 0, 0)
    moves = [(r, 0) for r in range(8)] + [(0, c) for c in range(8)] + [(i, i) for i in range(8)]
    for mv in moves:
        try:
            sample_piece.move(mv[0], mv[1])
            sample_piece.move(0, 0)
        except ValueError as exc:
            assert False, f'Valid queen move raised a ValueError: {exc}'