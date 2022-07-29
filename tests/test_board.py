import pytest
from app.board import Board

def test_create_new_board() -> None:
    '''
    Tests board initialization
    '''
    sample_board = Board()

    clean_board = 'R N B K Q B N R \nP P P P P P P P \n- - - - - - - - \n- - - - - - - - \n- - - - - - - - \n- - - - - - - - \nP P P P P P P P \nR N B K Q B N R \n'

    assert str(sample_board) == clean_board