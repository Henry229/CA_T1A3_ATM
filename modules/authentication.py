# verify identification

# verify PIN 3 times
def verity_identification(usr_pin):
    print('**** Insert your card ****')
    # 시간 지체하는 로직 필요!!!!!
    print(' Reading your card!! ')

    for i in range(1, 4):
        pin = int(input('Enter your PIN number: '))
        if pin == usr_pin:
            go_next = True
            print('Welcome John!!!')
            break
        else:
            print('=== Wrong PIN number!!Try again ===')
            print(f' You have {3-i} to go')
            go_next = False

    return go_next
