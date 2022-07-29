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