import time

try:
    input()
except NameError:
    pass


def choose_xo():
    choice = input('Would you like to be \'X\' or \'O\'?\n')
    while choice.upper() not in ['X', 'O']:
        print('That is an invalid input!')

        choice = input('Would you like to be \'X\' or \'O\'?\n')
    if choice.upper() == 'X':
        print('AI will go first\n')
        time.sleep(1.5)
        return 'p1', 'O', 'X'
    elif choice.upper() == 'O':
        print('You will go first\n')
        time.sleep(1.5)
        return 'AI', 'X', 'O'
