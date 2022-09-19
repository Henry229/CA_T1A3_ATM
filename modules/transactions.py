from time import sleep
# import prettytable module
from prettytable import PrettyTable


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
            print(type(input_amount))  # 반드시 지울 것!!!!!

            # check input (input only number)
            if input_amount.strip().isdigit():
                break
            else:
                print(f'Wrong Amount {input_amount}')
        return input_amount

    def check_balance(self, amt):
        if self.input_id == '1':
            tot = self.usr_amount - int(amt)
            if tot > 0:
                print('Please wait')
                time_interval()   # making interval looking real transactions
                print(f"${amt} has been withdrawn")
            else:
                print('Insufficient amount!!')
        elif self.input_id == '2':
            tot = self.usr_amount + int(amt)
        return tot

    def receipt(self, field_names, add_row, title):
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
        print('<<< You selected Withdrawal Transaction >>>')


class Deposit(Transactions):
    def __init__(self, input_id, usr_amount):
        Transactions.__init__(self, input_id, usr_amount)
        print('<<< You selected Deposit Transaction >>>')

    def chk_amount(self, amt):
        while True:
            pickup = input(f'Is ${amt} correct? (Y/N)').lower()
            if pickup == 'y':
                print('Please wait....')
                time_interval()  # making interval looking real transactions
                print(f"${amt} has deposited")
                break
            else:
                print('You have to enter either Y or N!!')
