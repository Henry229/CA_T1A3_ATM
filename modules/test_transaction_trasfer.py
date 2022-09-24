""" test transfer module"""
from transactions import Transactions, Transfer
import pytest

# inputs = iter([200, 0, -500, 'asdf']) for verifying values of
# input_bankdetails
inputs = iter([12001, 455112, 0, 'asdf'])
# verifying input amount for transfer
amount = iter([200, 300, 0, 'asdf'])


@pytest.fixture
def trans():
    """ delclare instance  with transaction class """
    return Transactions('3', 10000)


@pytest.fixture
def transfer():
    """ delclare instance  with transaction.transfer class """
    return Transfer('3', 10000)

# test input bsb 12001, account no 45112


def test_input_transfer_bankdetails(transfer, monkeypatch):
    monkeypatch.setattr('builtins.input', lambda prompt: next(inputs))
    assert transfer.input_bankdetails() == "12001 | 455112"
    # assert transfer.input_bankdetails() == 455112

# test input bsb 0, bsb 'asdf'


def test_input_transfer_bankdetails_odds(transfer, monkeypatch):
    monkeypatch.setattr('builtins.input', lambda prompt: next(inputs))
    # with pytest.raises(StopIteration):
    with pytest.raises(StopIteration):
        transfer.input_bankdetails()


# test 200, 300
def test_input_transfer_amount(trans, monkeypatch):
    monkeypatch.setattr('builtins.input', lambda prompt: next(amount))
    assert trans.input_amount('3') == 200
    assert trans.input_amount('3') == 300

# test 0, 'asdf'


def test_input_transfer_amount_odds(trans, monkeypatch):
    monkeypatch.setattr('builtins.input', lambda prompt: next(amount))
    with pytest.raises(StopIteration):
        trans.input_amount('3')


# test check balance
def test_check_balance(trans):
    tot = trans.check_balance(200, 0)  # when balance= $10000 transferred $200
    print('******* balance : ', tot)    # check if balance is correct
    # when balance = $10000 withdrawn $1200 -> Insufficient funds
    trans.check_balance(12000, 0)

# display balance


def test_display_balance(trans):
    trans.display_balance(9800)
