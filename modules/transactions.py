"""create class and def for each transaction"""
from time import sleep
# import datetime for getting today's date
import datetime
# import prettytable module
from prettytable import PrettyTable
# Package Pypi for colored font
from colorama import Fore, Back, Style


def time_interval():
    """ put some interval in order to look real transaction"""
    i = 0
    while i < 8:
        i += 1
        sleep(0.2)


def receipt():
    """ print receipt of transaction"""
    table_x = PrettyTable()
    table_x.field_names = ['Transaction', 'Amount']
    table_x.add_row(['Withdrawal', '$200'])
    # table_x.field_names = ['', 'Balance']
    table_x.add_row(['Balance', '$9800'])
    print(table_x.get_string(title='<<< Receipt >>>'))


class Transactions:
    """class Transaction for all AMT transactions"""

    def __init__(self, input_id, usr_amount):
        self.input_id = input_id
        self.usr_amount = usr_amount

    def input_amount(self, input_id):
        """ getting input amoount for relevant transaction"""
        while True:
            try:
                if input_id == '1':
                    input_amount = int(input('Type your withdrawal amount : '))
                elif input_id == '2':
                    input_amount = int(input('Type your deposit amount : '))
                elif input_id == '3':
                    input_amount = int(input('Type your sending amount  : '))
                else:
                    print(f'Something went wrong {input_id}')
                if input_amount > 0:
                    break
                else:
                    raise ValueError(
                        'Please enter an amount greater than zero!! ')
            except ValueError:
                print('**** What you entered is wrong number!!****')
        return input_amount

    def check_balance(self, amt, acc_tr):
        """ check balance if available before transaction starts"""
        if self.input_id == '1' or self.input_id == '3':
            tot = self.usr_amount - int(amt)
            if tot > 0:
                if self.input_id == '1':
                    print('Please wait')
                    time_interval()   # making interval looking real transactions
                    print(f"${amt} has been withdrawn")
                elif self.input_id == '3':
                    print(f"${amt} will be trasferred to account no {acc_tr}")
            else:
                print('Insufficient amount!!')
        elif self.input_id == '2':
            tot = self.usr_amount + int(amt)
        return tot

    def receipt(self, field_names, add_row, title):
        """ print recipients"""
        print('==========================')
        today = datetime.datetime.now()
        print(today.strftime('%x-%X'))
        print('==========================')
        table_x = PrettyTable()
        table_x.field_names = field_names
        table_x.add_row(add_row)
        print(table_x.get_string(title=title))

    def display_balance(self, bal):
        """ display balance"""
        print('========================')
        print(f'Your balance is ${bal}')
        print('========================')


class Withdraw(Transactions):
    """ class Withdrawal"""

    def __init__(self, input_id, usr_amount):
        Transactions.__init__(self, input_id, usr_amount)
        print(Back.WHITE + Fore.RED + Style.NORMAL +
              '<<< You selected Withdrawal Transaction >>>' + Style.RESET_ALL)


class Deposit(Transactions):
    """ class Deposit"""

    def __init__(self, input_id, usr_amount):
        Transactions.__init__(self, input_id, usr_amount)

    def chk_amount(self, amt):
        """ confrim money if it is correct before deposit and trasferred"""
        while True:
            pickup = input(f'Is ${amt} correct? (Y/N)').lower()
            if pickup == 'y':
                print('Please wait....')
                time_interval()  # making interval looking real transactions
                if self.input_id == '2':
                    print(f"${amt} has deposited")
                    break
                elif self.input_id == '3':
                    print(f"${amt} has trasferred")
                    break
            else:
                if pickup == 'n':
                    print(' Please start transaction again after checking amount..')
                    break
                else:
                    print('You have to enter either Y or N!!')


class Transfer(Deposit, Transactions):
    """class Tranfer Transaction"""

    def __init__(self, input_id, usr_amount):
        Deposit.__init__(self, input_id, usr_amount)
        Transactions.__init__(self, input_id, usr_amount)

    def input_bankdetails(self):
        """ enter bankdetails for you want to transfer"""
        while True:
            try:
                bsb = int(input('Enter BSB number you want to transfer :'))
                account_no = int(
                    input('Enter account number you want to transfer :'))
                # check input (input only number)
                if bsb > 100 and account_no > 100:
                    break
                else:
                    raise ValueError(
                        f'Wrong Input {bsb} | {account_no} It should be more than 3 digit!!!')
            except ValueError:
                print('**** What you entered is wrong number!!****')

        return f"{bsb}' | '{account_no}"


class CheckBalance(Transactions):
    """ class check balance transaction"""

    def __init__(self, input_id, usr_amount):
        Transactions.__init__(self, input_id, usr_amount)
        print(
            Back.WHITE +
            Fore.RED +
            Style.NORMAL +
            '<<< You selected Check-Balance Transaction >>>' +
            Style.RESET_ALL)
