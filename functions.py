class MockFunc:
    def __init__(self, outputs):
        self.outputs = outputs[:]
        
    def __call__(self, *args, **kwargs):
        if not self.outputs:
            raise RuntimeError(f"No more outputs to return!")
        return self.outputs.pop(0)
# example: roll_die = MockFunc([3, 2, 1, 3, 6, 5])
#*args- takes any positional arguments
#**kwargs - takesk any keyword arguments

example_board = ({1 : [6,6],
                  2 : [3, 4, 4], 
                  3 : [2, 2, 1]})


def calculate_score(board):
    score = 0
    for col_num, col in board.items():
        die_counts = {}
        for die in col:
            die_counts[die] = die_counts.get(die, 0) + 1
        for key, count in die_counts.items():
            if count == 2:
                score += key * 4
            elif count == 3:
                score += key * 9
            else:
                score += key
    return score


def computer_move(ai_board, opponent_board, die_value):
    """
    Makes the best move for the computer player.

    Args:
        ai_board: The computer player's board.
        opponent_board: The opponent player's board.
        die_value: The value of the die rolled.

    Returns:
        The column index where the die should be placed.
    """

    for col_index, col_values in ai_board.items():
        
        if die_value in col_values:
            return col_index

        if die_value in opponent_board[col_index]:
            return col_index

    min_score_col = min(ai_board, key=lambda x: sum(ai_board[x]))
    return min_score_col

    
def cancel_die(board, other_board):
    #removes die from board if opponent places same value die in the corresponding column
    for columnkey in other_board:
        if columnkey in board:
            for die in other_board[columnkey]:
                if die in board[columnkey]:
                    board[columnkey].remove(die)
    return board
    

def manage_game(player1_board, player2_board):
    roll_die = MockFunc([3, 2, 1, 3, 6, 5, 3, 5, 1, 4, 3, 6])
    is_board_full = MockFunc(False)

    current_player = 1

    while not is_board_full(player1_board) and not is_board_full(player2_board):
        print(f"Player {current_player} Board: {player1_board if current_player == 1 else player2_board}")
        print(f"Player {current_player} Score: {calculate_score(player1_board if current_player == 1 else player2_board)}")

        roll = roll_die()
        
        print(f"Player {current_player} rolled a {roll}.\n")

        if current_player == 1:
            while True:
                column_choice = int(input("What column would you like to place (1, 2, 3)? ")) - 1
                if 0 <= column_choice <= 2 and len(player1_board[column_choice]) < 3:
                    break
                else:
                    print("Invalid input. Please try again.")

            player1_board[column_choice].append(roll)
            if roll in player2_board[column_choice]:
                player2_board[column_choice].remove(roll)
        else:
            column_choice = computer_move(player2_board, player1_board, roll)
            player2_board[column_choice].append(roll)
            if roll in player1_board[column_choice]:
                player1_board[column_choice].remove(roll)

        current_player = 3 - current_player 

    player1_score = calculate_score(player1_board)
    player2_score = calculate_score(player2_board)
    
    print("\nGame Over!")
    if player1_score > player2_score:
        print("Player 1 Wins!")
    elif player2_score > player1_score:
        print("Player 2 Wins!")
    else:
        print("It's a tie!")
        
        
        
        
        
        
