from unittest.mock import Mock
from transactions import Transactions
import pytest
# from exceptions import get_int, RangeError

# inputs = iter([200, 0, -500, 'asdf'])
inputs = iter([200, 300, 0, 'asdf'])

@pytest.fixture
def trans():
    return Transactions('1', 10000)

def test_input_withdrawal_amount(trans, monkeypatch):
    monkeypatch.setattr('builtins.input', lambda prompt: next(inputs))
    assert trans.input_amount('1') == 200
    assert trans.input_amount('1') == 300

def test_input_withdrawal_amount_odds(trans, monkeypatch):
    monkeypatch.setattr('builtins.input', lambda prompt: next(inputs))
    with pytest.raises(StopIteration):
        trans.input_amount('1')


    # test_input = Mock(side_effect=input_list)
    # test_input = Mock(return_value=input_list)
    # assert test_input == 200

# class TestInputAmount:
#     def test_valid(self,monkeypatch):
#         input_test = Transactions('1', 10000)
#         input_test.input_amount('1')
#         # get_int에서 input할때 이 fake_input으로 대체해 리턴한다.
#         monkeypatch.setattr('builtins.input', fake_input)
#         assert input_test.input_amount() == 200
#         assert input_test.input_amount() == 300
        # assert get_int() in range(1, 11)

    # def test_above_range(self, monkeypatch):
    #     monkeypatch.setattr('builtins.input', fake_input)
    #     with pytest.raises(RangeError):
    #         get_int()

    # def test_below_range(self, monkeypatch):
    #     monkeypatch.setattr('builtins.input', fake_input)
    #     with pytest.raises(RangeError):
    #         get_int()
