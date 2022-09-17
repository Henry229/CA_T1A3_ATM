# ATM applicatoin

# import prettytable module
from prettytable import PrettyTable
# import transaction modules
from modules import authentication

print('ATM applicatoin')

menu_id = []
# design manu


def transaction_menu():
    x = PrettyTable()
    x.field_names = ['Transaction ID', 'Transaction Type']
    x.add_row(['1', 'Withdrawal'])
    x.add_row(['2', 'Deposit'])
    x.add_row(['3', 'Transfer'])
    x.add_row(['4', 'Balance'])
    x.add_row(['5', 'Cancel Transaction'])
    print(x.get_string(title='<<< Select a transaction >>>'))
    for id, menu in x.rows:
        menu_id.append(id)
    print(menu_id)


transaction_menu()
# if __name__ == '__main__':
#     next = authentication.verity_identification()
#     if not next:
