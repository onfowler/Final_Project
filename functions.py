import random

def roll():
    return random.randint(1, 6)

class Board:
    def __init__(self):
        self.board = {1: [], 2: [], 3:[]}
        self.score = 0
        
    def is_full(self):
        for col in self.board.values():
            if len(col) < 3:
                return False
        return True
    
    def place_die(self, column, die_value):
        if len(self.board[column]) < 3:
            self.board[column].append(die_value)
            return True
        return False

    def calculate_score(self):
        """
        Calculates the total score of a given board.

        Args:
            board: A dictionary representing the game board.

        Returns:
            The total score of the board.
        """
        score = 0
        for col_num, col in self.board.items():
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
        self.score = score
        return score
    
    def __str__(self):
        return (f"{self.board}")


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

    for col_index, col_values in ai_board.board.items():
        
        if die_value in col_values:
            return col_index

        if die_value in opponent_board.board[col_index]:
            return col_index

    min_score_col = min(ai_board.board, key=lambda x: sum(ai_board.board[x]))
    return min_score_col

    
def cancel_die(board, other_board):
    """
    Removes dice from a board if the opponent has placed the same value in the corresponding column.

    Args:
        board: The board to modify.
        other_board: The opponent's board.
    """
    for column_key in other_board.board:
        if column_key in board.board:
            matching_dice = set(board.board[column_key]) & set(other_board.board[column_key])
            board.board[column_key] = [die for die in board.board[column_key] if die not in matching_dice]
    

def manage_game(player1_board, player2_board):
    """
    Manages the game flow, alternating between player and computer turns.

    Args:
        player1_board: The player's board.
        player2_board: The computer's board.
    """

    current_player = 1

    while not player1_board.is_full() and not player2_board.is_full():
        print(f"Player {current_player} Board: {player1_board if current_player == 1 else player2_board}")
        print(f"Player {current_player} Score: {(player1_board.calculate_score() if current_player == 1 else player2_board.calculate_score())}")

        roll = random.randint(1,6)
        
        print(f"Player {current_player} rolled a {roll}.\n")

        if current_player == 1:
            while True:
                column_choice = int(input("What column would you like to place (1, 2, 3)? "))
                if 0 <= column_choice <= 3 and player1_board.place_die(column_choice, roll):
                    break
                else:
                    print("Invalid input. Please try again.")

            player2_board = cancel_die(player2_board, player1_board)  
        else:
            column_choice = computer_move(player2_board, player1_board, roll)
            player2_board.place_die(column_choice, roll)
            player1_board = cancel_die(player1_board, player2_board)

        current_player = 3 - current_player 

    player1_score = player1_board.calculate_score()
    player2_score = player2_board.calculate_score()
    
    print("\nGame Over!")
    if player1_score > player2_score:
        print("Player 1 Wins!")
    elif player2_score > player1_score:
        print("Player 2 Wins!")
    else:
        print("It's a tie!")
        
        
        
def main():
    player1_board = Board()
    player2_board = Board()
    
    manage_game(player1_board, player2_board)

if __name__ == "__main__":
    main()
        
