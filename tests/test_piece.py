import pytest
from app.piece import Piece

def test_create_piece() -> None:
    '''
    Tests piece creation
    '''
    sample_piece_name = 'P'
    sample_piece_side = 'W'

    sample_piece = Piece(sample_piece_name, sample_piece_side)

    assert sample_piece.name == 'P' and sample_piece.side == 'W'


def test_valid_names() -> None:
    '''
    Tests if valid name does not raise ValueError
    '''
    for name in ['P', 'R', 'N', 'B', 'K', 'Q']:
        try:
            sample_piece = Piece(name, 'W')
        except ValueError as exc:
            assert False, f'{name} raised a ValueError {exc}'


def test_name_error() -> None:
    '''
    Tests if invalid name raises proper ValueError
    '''
    with pytest.raises(ValueError):
        sample_piece = Piece('H', 'W')


def test_valid_sides() -> None:
    '''
    Tests if valid side does not raise ValueError
    '''
    for side in ['W', 'B']:
        try:
            sample_piece = Piece('P', side)
        except ValueError as exc:
            assert False, f'{side} raised a ValueError {exc}'


def test_side_error() -> None:
    '''
    Tests if invalid side raises proper ValueError
    '''
    with pytest.raises(ValueError):
        sample_piece = Piece('P', 'Y')