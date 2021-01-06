import random


def easy(board, possible_numbers, ai_xo):
    # this function will generate a random available number on the board and change it to 'O'
    rand_choice = random.choice(possible_numbers)
    possible_numbers.remove(rand_choice)
    board.spaces[rand_choice] = ai_xo


def hard(board, possible_numbers, ai_xo):
    # winning combs:
    win_combs = [['1', '2', '3'],
                 ['4', '5', '6'],
                 ['7', '8', '9'],
                 ['1', '4', '7'],
                 ['2', '5', '8'],
                 ['3', '6', '9'],
                 ['1', '5', '9'],
                 ['3', '5', '7']]

    # use the shuffle method, so the computer doesn't use the same order each time
    random.shuffle(win_combs)

    # if two of the three spaces is the same, add an 'O' in order to block the win
    for win in win_combs:
        if board.spaces[win[0]] == board.spaces[win[1]]:
            if board.spaces[win[2]] in possible_numbers:
                possible_numbers.remove(board.spaces[win[2]])
                board.spaces[win[2]] = ai_xo
                return possible_numbers
        elif board.spaces[win[0]] == board.spaces[win[2]]:
            if board.spaces[win[1]] in possible_numbers:
                possible_numbers.remove(board.spaces[win[1]])
                board.spaces[win[1]] = ai_xo
                return possible_numbers
        elif board.spaces[win[1]] == board.spaces[win[2]]:
            if board.spaces[win[0]] in possible_numbers:
                possible_numbers.remove(board.spaces[win[0]])
                board.spaces[win[0]] = ai_xo
                return possible_numbers
        else:
            pass

    # if there aren't any matches of two in any row, choose a random available spot
    return easy(board, possible_numbers, ai_xo)


def impossible(board, possible_numbers, ai_xo):
    # winning combinations
    win_combs = [['1', '2', '3'],
                 ['4', '5', '6'],
                 ['7', '8', '9'],
                 ['1', '4', '7'],
                 ['2', '5', '8'],
                 ['3', '6', '9'],
                 ['1', '5', '9'],
                 ['3', '5', '7']]

    # again, use the shuffle method, so the computer doesn't use the same order each time
    random.shuffle(win_combs)

    # if two of the three spaces is the same, add an 'O' in order to block the win
    for win in win_combs:
        if board.spaces[win[0]] == board.spaces[win[1]]:
            if board.spaces[win[2]] in possible_numbers:
                possible_numbers.remove(board.spaces[win[2]])
                board.spaces[win[2]] = ai_xo
                return possible_numbers
        elif board.spaces[win[0]] == board.spaces[win[2]]:
            if board.spaces[win[1]] in possible_numbers:
                possible_numbers.remove(board.spaces[win[1]])
                board.spaces[win[1]] = ai_xo
                return possible_numbers
        elif board.spaces[win[1]] == board.spaces[win[2]]:
            if board.spaces[win[0]] in possible_numbers:
                possible_numbers.remove(board.spaces[win[0]])
                board.spaces[win[0]] = ai_xo
                return possible_numbers
        else:
            pass

    # take either the middle or the corner sections,
    # which make it impossible for the other player to win
    for space in random.shuffle(['5', '1', '7', '9', '3']):
        if space in possible_numbers:
            possible_numbers.remove(space)
            board.spaces[space] = ai_xo
            return possible_numbers

    return easy(board, possible_numbers, ai_xo)
