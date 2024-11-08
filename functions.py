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

    for col_idx, col_values in ai_board.items():
        
        if die_value in col_values:
            return col_idx

        if die_value in opponent_board[col_idx]:
            return col_idx

    min_score_col = min(ai_board, key=lambda x: sum(ai_board[x]))
    return min_score_col

    
def cancel_die(board, other_board):
    #removes die from board if opponent places same value die in the corresponding column
    

def manage_game(player1_board, player2_board):
    #plays the game and simulates two players playing