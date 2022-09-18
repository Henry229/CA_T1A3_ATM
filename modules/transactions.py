from time import sleep


def time_interval():
    i = 0
    while i < 10:
        i += 1
        sleep(0.2)


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
            print(type(input_amount))
            # chack input (input only number)
            if input_amount.strip().isdigit():
                break
            else:
                print(f'Wrong Amount {input_amount}')
        return input_amount

    def check_amount(self, amt):
        sub = self.usr_amount - int(amt)
        if sub > 0:
            print('Please wait')
            time_interval()
            print(f"${amt} has been withdrawn")
        else:
            print('Insufficient amount!!')
        return sub


class Withdraw(Transactions):
    def __init__(self, input_id, usr_amount):
        Transactions.__init__(self, input_id, usr_amount)
        print('<<< You selected Withdrawal Transaction >>>')

    # def
