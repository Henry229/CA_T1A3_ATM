from time import sleep
from xmlrpc.client import DateTime
# import prettytable module
from prettytable import PrettyTable
# Package Pypi for colored font
from colorama import Fore, Back, Style
# get date of today
import datetime


def time_interval():
    i = 0
    while i < 8:
        i += 1
        sleep(0.2)


def receipt():
    table_x = PrettyTable()
    table_x.field_names = ['Transaction', 'Amount']
    table_x.add_row(['Withdrawal', '$200'])
    # table_x.field_names = ['', 'Balance']
    table_x.add_row(['Balance', '$9800'])
    print(table_x.get_string(title='<<< Receipt >>>'))


class Transactions:
    def __init__(self, input_id, usr_amount):
        self.input_id = input_id
        self.usr_amount = usr_amount

    def input_amount(self, input_id):
        while True:
            if input_id == '1':
                input_amount = input('Type your withdrawal amount : ')
            elif input_id == '2':
                input_amount = input('Type your deposit amount : ')
            elif input_id == '3':
                input_amount = input('Type your sending amount  : ')
            else:
                print('Something went wrong!!')

            # check input (input only number)
            if input_amount.strip().isdigit():
                break
            else:
                print(f'Wrong Amount {input_amount}')
        return input_amount

    def check_balance(self, amt, acc_tr):
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
        print('==========================')
        today = datetime.datetime.now()
        print(today.strftime('%x-%X'))
        print('==========================')
        table_x = PrettyTable()
        table_x.field_names = field_names
        table_x.add_row(add_row)
        print(table_x.get_string(title=title))

    def display_balance(self, bal, amt):
        print('========================')
        print(f'Your balance is ${bal}')
        print('========================')


class Withdraw(Transactions):
    def __init__(self, input_id, usr_amount):
        Transactions.__init__(self, input_id, usr_amount)
        print(Back.WHITE + Fore.RED + Style.NORMAL +
              '<<< You selected Withdrawal Transaction >>>' + Style.RESET_ALL)


class Deposit(Transactions):
    def __init__(self, input_id, usr_amount):
        Transactions.__init__(self, input_id, usr_amount)

    def chk_amount(self, amt):
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
    def __init__(self, input_id, usr_amount):
        Deposit.__init__(self, input_id, usr_amount)
        Transactions.__init__(self, input_id, usr_amount)
        print(Back.WHITE + Fore.RED + Style.NORMAL +
              '<<< You selected Trasfer Transaction >>>' + Style.RESET_ALL)

    def input_bankdetails(self):
        while True:
            bsb = input('Enter BSB number you want to transfer :')
            account_no = input('Enter account number you want to transfer :')
            # check input (input only number)
            if bsb.strip().isdigit() and account_no.strip().isdigit():
                break
            else:
                print(
                    f'Wrong Input {bsb} | {account_no} It should be number!!!')
        return bsb+'|'+account_no


class Check_balance(Transactions):
    def __init__(self, input_id, usr_amount):
        Transactions.__init__(self, input_id, usr_amount)
        print(Back.WHITE + Fore.RED + Style.NORMAL +
              '<<< You selected Check-Balance Transaction >>>' + Style.RESET_ALL)
