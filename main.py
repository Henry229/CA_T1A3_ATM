# ATM applicatoin

# import sys
# import prettytable module
from prettytable import PrettyTable
# import transaction modules
from modules import authentication

print('=== < ATM Applicatoin > ====')

menu_id = []
# design manu


def transaction_menu():
    table_x = PrettyTable()
    table_x.field_names = ['Transaction ID', 'Transaction Type']
    table_x.add_row(['1', 'Withdrawal'])
    table_x.add_row(['2', 'Deposit'])
    table_x.add_row(['3', 'Transfer'])
    table_x.add_row(['4', 'Balance'])
    table_x.add_row(['5', 'Cancel Transaction'])
    print(table_x.get_string(title='<<< Select a transaction >>>'))
    for id, menu in table_x.rows:
        menu_id.append(id)


# transaction_menu()
if __name__ == '__main__':
    # verify identification
    next_step = authentication.verity_identification()
    # if PIN is correct?
    if next_step:
        while True:
            transaction_menu()
            # ask a client to enter the menu id
            input_id = input('Please select a transaction number : ')
            # chack if the item is in the menu list
            try:
                if input_id in menu_id:
                    print(f' you selected id : {input_id} ')
                    break
                else:
                    print('ID not found!!')
            # exception block
            except Exception:
                print('No ID, please select it again!!')
    #  wrong PIN with 3 times
    else:
        print(' You have entered wrong PIN number, Please check your PIN.')
        exit()
