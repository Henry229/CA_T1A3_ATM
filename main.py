# ATM applicatoin

# import sys
# import prettytable module
from prettytable import PrettyTable
# import transaction modules
from modules import authentication
from modules import transactions

print('=== < ATM Applicatoin > ====')

menu_id = []
# for making Table
# field_names = []
# add_row = []

# Set user data
user_data = {'pin_no': 1234, 'usr_amount': 10000}
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
    next_step = authentication.verity_identification(user_data['pin_no'])
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
    #===========#
    # withdrawal
    #===========#
    if input_id == '1':
        amt_bl = 0
        wd = transactions.Withdraw('1', user_data['usr_amount'])
        # input amount of withdrawal
        amt_wd = wd.input_amount('1')
        # check balance for deduction
        amt_bl = wd.check_balance(amt_wd, 0)
        # update balance
        user_data['usr_amount'] = amt_bl
        # create receipt
        # making parameters for receipt
        field_names = ['Transaction', 'Amount']
        add_row = ['Withdrawal', '$'+amt_wd]
        title = '<<< Receipt >>>'
        wd.receipt(field_names, add_row, title)
        # display balance
        wd.display_balance(amt_bl, amt_wd)
    #===========#
    # deposit
    #===========#
    elif input_id == '2':
        amt_bl = 0
        dp = transactions.Deposit('2', user_data['usr_amount'])
        # amount of deposit
        amt_dp = dp.input_amount('2')
        # confrim amount of deposit & deposit
        dp.chk_amount(amt_dp)
        # add amount of deposit to balance
        amt_bl = dp.check_balance(amt_dp)
        # create receipt
        field_names = ['Transaction', 'Amount']
        add_row = ['Deposit', '$'+amt_dp]
        title = '<<< Receipt >>>'
        dp.receipt(field_names, add_row, title)
        # diplay balance
        dp.display_balance(amt_bl, amt_dp)
    #===========#
    # transfer
    #===========#
    elif input_id == '3':
        amt_bl = 0
        tr = transactions.Transfer('3', user_data['usr_amount'])
        # input account number you want to transfer
        acc_tr = tr.input_bankdetails()
        # amount of transfer
        amt_tr = tr.input_amount('3')
        # check balance if transfer is possible
        amt_bl = tr.check_balance(amt_tr, acc_tr)
        if amt_bl > 0:
            tr.chk_amount(amt_tr)
        # else에 대한 로직 추가!!!!!
         # create receipt
        field_names = ['Transaction', 'Amount']
        add_row = ['Transfer', '$'+amt_tr]
        title = '<<< Receipt >>>'
        tr.receipt(field_names, add_row, title)
        # diplay balance
        tr.display_balance(amt_bl, amt_tr)
     #===========#
    # Check Balance
    #===========#
    elif input_id == '4':
        ck = transactions.Check_balance('4', user_data['usr_amount'])
        ck.display_balance(user_data['usr_amount'], 0)
    elif input_id == '5':
        print('See you next time! Thank you')
        exit()
    else:
        pass
