""" ATM application"""
# ATM application

import sys
# Package Pypi for colored font
from colorama import Fore, Back, Style
# import prettytable module
from prettytable import PrettyTable
# import transaction modules
from modules import authentication
from modules import transactions

print('=== < ATM Applicatoin > ====')

menu_id = []

# Set user data
user_data = {'pin_no': '1234', 'usr_amount': 10000}
# design manu


def transaction_menu():
    """ show main menu for choosing transactions using prettytable"""
    table_x = PrettyTable()
    table_x.field_names = ['Transaction ID', 'Transaction Type']
    table_x.add_row(['1', 'Withdrawal'])
    table_x.add_row(['2', 'Deposit'])
    table_x.add_row(['3', 'Transfer'])
    table_x.add_row(['4', 'Balance'])
    table_x.add_row(['5', 'Cancel Transaction'])
    print(table_x.get_string(title='<<< Select a transaction >>>'))
    for key, menu in table_x.rows:
        menu_id.append(key)


# transaction_menu()
if __name__ == '__main__':
    # verify identification
    NEXT_STEP = authentication.verify_identification(user_data['pin_no'])
    # if PIN is correct?
    if NEXT_STEP:
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
        sys.exit()

    #===========#
    # withdrawal
    #===========#
    if input_id == '1':
        AMT_BL = 0
        wd = transactions.Withdraw('1', user_data['usr_amount'])
        # input amount of withdrawal
        amt_wd = wd.input_amount('1')
        # check balance for deduction
        AMT_BL = wd.check_balance(amt_wd, 0)
        if AMT_BL > 0:
            reply = wd.chk_amount(amt_wd)
            if reply == 'y':
                # create receipt
                field_names = ['Transaction', 'Amount']
                add_row = ['Transfer', '$' + str(amt_wd)]
                TITLE = '<<< Receipt for Withdrawal >>>'
                wd.receipt(field_names, add_row, TITLE)
                # diplay balance
                wd.display_balance(AMT_BL)
            else:
                print('=== Please start again! ====')
        else:
            print('Please start transaction again!!')
    #===========#
    # deposit
    #===========#
    elif input_id == '2':
        AMT_BL = 0
        dp = transactions.Deposit('2', user_data['usr_amount'])
        # amount of deposit
        amt_dp = dp.input_amount('2')
        # confrim amount of deposit
        # add amount of deposit to balance
        AMT_BL = dp.check_balance(amt_dp, 0)
        if AMT_BL > 0:
            reply = dp.chk_amount(amt_dp)
            if reply == 'y':
                # create receipt
                field_names = ['Transaction', 'Amount']
                add_row = ['Deposit', '$' + str(amt_dp)]
                TITLE = '<<< Receipt for Transfer >>>'
                dp.receipt(field_names, add_row, TITLE)
                # diplay balance
                dp.display_balance(AMT_BL)
            else:
                print('=== Please start again! ====')
        else:
            print('Please start transaction again!!')
    #===========#
    # transfer
    #===========#
    elif input_id == '3':
        AMT_BL = 0
        tr = transactions.Transfer('3', user_data['usr_amount'])
        # input account number you want to transfer
        acc_tr = tr.input_bankdetails()
        # amount of transfer
        amt_tr = tr.input_amount('3')
        # check balance if transfer is possible
        AMT_BL = tr.check_balance(amt_tr, acc_tr)
        if AMT_BL > 0:
            reply = tr.chk_amount(amt_tr)
            if reply == 'y':
                # create receipt
                field_names = ['Transaction', 'Amount']
                add_row = ['Transfer', '$' + str(amt_tr)]
                TITLE = '<<< Receipt for Transfer >>>'
                tr.receipt(field_names, add_row, TITLE)
                # diplay balance
                tr.display_balance(AMT_BL)
            else:
                print('=== Please start again! ====')
        else:
            print('Please start transaction again!!')
        # check if amoutn entered is correct
    #===========#
    # Check Balance
    #===========#
    elif input_id == '4':
        print(Back.WHITE + Fore.RED + Style.NORMAL +
              '<<< check Balance Transaction >>>' + Style.RESET_ALL)
        ck = transactions.CheckBalance('4', user_data['usr_amount'])
        ck.display_balance(user_data['usr_amount'])
    elif input_id == '5':
        print('See you next time! Thank you')
        sys.exit()
    else:
        pass

    print('**************************************')
    print('*** Thank you!  😀  See you again! ***')
    print('**************************************')
