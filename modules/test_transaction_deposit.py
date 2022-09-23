""" test deposit module"""
from transactions import Transactions
import pytest

# inputs = iter([200, 0, -500, 'asdf']) for verifying values of input_amount
inputs = iter([200, 300, 0, 'asdf'])


@pytest.fixture
def trans():
    """ test case for unittest in deposit module"""
    return Transactions('2', 10000)


# test deposit amount 200, 300 for inputs
def test_input_deposit_amount(trans, monkeypatch):
    monkeypatch.setattr('builtins.input', lambda prompt: next(inputs))
    assert trans.input_amount('2') == 200
    assert trans.input_amount('2') == 300

# test deposit amount  with 0, 'asdf' for varifying odds values


def test_input_deposit_amount_odds(trans, monkeypatch):
    monkeypatch.setattr('builtins.input', lambda prompt: next(inputs))
    with pytest.raises(StopIteration):
        trans.input_amount('2')

# test check balance


def test_check_balance(trans):
    tot = trans.check_balance(200, 0)  # when balance= $10000 withdrawn $200
    print('******* balance : ', tot)    # check if balance is correct

# display balance


def test_display_balance(trans):
    trans.display_balance(10200)
