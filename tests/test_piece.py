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
            assert False, f'{name} raised a ValueError {exc}'


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
            assert False, f'{side} raised a ValueError {exc}'


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
            assert False, f'{r} raised a ValueError {exc}'


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
            assert False, f'{c} raised a ValueError {exc}'


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