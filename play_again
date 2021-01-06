try:
    input()
except NameError:
    pass

def play_again():
    play_again_choice = str(input('Would you like to play again (y/n)?\n'))
    while play_again_choice not in ['y', 'Y', 'yes', 'Yes', 'n', 'N', 'no', 'No']:
        print('That is an invalid input!')
        play_again_choice = str(input('Would you like to play again (y/n)?\n'))
    if play_again_choice == 'n' or play_again_choice == 'N'\
    or play_again_choice == 'no' or play_again_choice == 'No':
        print('Ok, thank you for playing!')
        return False
    elif play_again_choice == 'y' or play_again_choice == 'Y'\
    or play_again_choice == 'yes' or play_again_choice == 'Yes':
        return True
