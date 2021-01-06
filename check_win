def check_win(board, number):

    # winning possibilities
    win_combs = [['1', '2', '3'],
                 ['4', '5', '6'],
                 ['7', '8', '9'],
                 ['1', '4', '7'],
                 ['2', '5', '8'],
                 ['3', '6', '9'],
                 ['1', '5', '9'],
                 ['3', '5', '7']]

    for win in win_combs:
        if board.spaces[win[0]] == board.spaces[win[1]] and board.spaces[win[0]]\
         == board.spaces[win[2]]:

            return board.spaces[win[0]]
        if number == 9:
            return 'Tie!'
        else:
            return None
