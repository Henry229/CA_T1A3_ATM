""" test withdran module"""
from transactions import Transactions
import pytest

# inputs = iter([200, 0, -500, 'asdf']) for verifying values of input_amount
inputs = iter([200, 300, 0, 'asdf'])


@pytest.fixture
def trans():
    """ test case for unittest in widthdraw module"""
    return Transactions('1', 10000)

# test 200, 300


def test_input_withdrawal_amount(trans, monkeypatch):
    monkeypatch.setattr('builtins.input', lambda prompt: next(inputs))
    assert trans.input_amount('1') == 200
    assert trans.input_amount('1') == 300

# test 0, 'asdf'


def test_input_withdrawal_amount_odds(trans, monkeypatch):
    monkeypatch.setattr('builtins.input', lambda prompt: next(inputs))
    with pytest.raises(StopIteration):
        trans.input_amount('1')

# test check balance


def test_check_balance(trans):
    tot = trans.check_balance(200, 0)  # when balance= $10000 withdrawn $200
    print('******* balance : ', tot)    # check if balance is correct
    # when balance = $10000 withdrawn $1200 -> Insufficient funds
    trans.check_balance(12000, 0)

# display balance


def test_display_balance(trans):
    trans.display_balance(9800)
