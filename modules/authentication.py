# verify identification

print('**** Insert your card ****')
# 시간 지체하는 로직 필요!!!!!
print(' Reading your card!! ')

# verify PIN 3 times


def verity_identification():
    for i in range(1, 4):
        pin = int(input('Enter your PIN number: '))
        if pin == 1234:
            go_next = True
            break
        else:
            print('=== Wrong PIN number!!Try again ===')
            print(f' You have {3-i} to go')
            go_next = False

    return go_next
