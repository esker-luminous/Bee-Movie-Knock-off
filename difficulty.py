import time

try:
    input()
except NameError:
    pass

def difficulty():
    print('1:  Easy\n')
    print('2:  Hard\n')
    print('3:  Impossible\n')

    diff_choice = input('What level would you like to try?\n')
    while diff_choice.isdigit() == False or int(diff_choice) not in [1, 2, 3]:
        print('This is an invalid input!')
        diff_choice = input('What level would you like to try?\n')
    if int(diff_choice) in [1, 2, 3]:
        if int(diff_choice) == 1:
            print('You have chosen the \'easy\' module\n')
            time.sleep(1.5)
            return 'E'
        elif int(diff_choice) == 2:
            print('You have chosen the \'hard\' module\n')
            time.sleep(1.5)
            return 'H'
        elif int(diff_choice) == 3:
            print('You have chosen the \'impossible\' module\n')
            time.sleep(1.5)
            return 'I'
