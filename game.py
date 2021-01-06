from board import board, display_board
from difficulty import difficulty
from chooseXO import choose_xo
from AI_turn import easy, hard, impossible
from user_turn import p1_turn
from check_win import check_win
from play_again import play_again
import time

def tic_tac_toe():
    def main():

        diff = difficulty()
        time.sleep(1.5)

        initial_board = display_board(board)
        turns = 0
        possible_numbers = [str(i) for i in range(1, 10)]
        last_move, ai_xo, p1_xo = choose_xo()

        while turns < 9:
            initial_board.display_board(board)

            if last_move == 'p1':
                print('AI\'s turn.\n')
                time.sleep(1.5)
                if diff == 'E':
                    possible_numbers = easy(initial_board, possible_numbers, ai_xo)
                elif diff == 'H':
                    possible_numbers = hard(initial_board, possible_numbers, ai_xo)
                elif diff == 'I':
                    possible_numbers = impossible(initial_board, possible_numbers, ai_xo)
                last_move = 'AI'
            elif last_move == 'AI':
                possible_numbers = p1_turn(initial_board, possible_numbers, p1_xo)
                last_move = 'p1'

            win = check_win(initial_board, turns)
            if win == None:
                pass
            else:
                break

            turns += 1

        initial_board.display_board(board)

        if win == ai_xo:
            print('AI wins. You lose!\n')
        elif win == p1_xo:
            print('You win. AI loses!')
        elif win == 'Tie':
            print('It\'s a tie!')

        time.sleep(1.5)

    tic_tac_toe()

    times_played = 1
    while times_played < 10:
        if play_again():
            tic_tac_toe()
            times_played += 1
        else:
            break

    print('Goodbye!')
    time.sleep(1.5)
    quit()

    if __name__ == '__main__':
        main()

tic_tac_toe()
