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
    #calculates the score of the board
    #takes board
    #returns int
    return



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
    return
    

def manage_game(player1_board, player2_board):
    #plays the game and simulates two players playing
    roll_die = MockFunc([3, 2, 1, 3, 6, 5, 3, 5, 1, 4, 3, 6])
    board_is_full = MockFunc(False)
    add_die_to_board = MockFunc()

    
    while not board_is_full(player1_board) or not board_is_full(player2_board):
        print(f"Player 1 Board:{player1_board}")
        print(f"Player 2 Board:{player2_board}")
        roll = roll_die()
        input = f"You rolled a {roll}.\nWhat column would you like to place (1, 2, 3)"
        player1_board = add_die_to_board(player1_board, player2_board, input, roll)
        
        print(f"Player 1 Board:{player1_board}")
        print(f"Player 2 Board:{player2_board}")
        roll = roll_die()
        input = f"Computer rolled a {roll}."
        player2_board = add_die_to_board(player1_board, player2_board, computer_move(player2_board, player1_board, roll), roll)
        
    print("Game Over!")
        
        
        
        
        
        
