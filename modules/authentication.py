""" verigy identification """
# verify identification

# verify PIN 3 times


def verify_identification(usr_pin):
    """ verity identification"""
    print('**** Insert your card ****')
    print(' Reading your card!! ')

    for i in range(1, 4):
        pin = input('Enter your PIN number: ')
        if pin == usr_pin:
            go_next = True
            print('Welcome John!!!')
            break
        else:
            print('=== Wrong PIN number!!Try again ===')
            print(f' You have {3-i} to go')
            go_next = False

    return go_next
