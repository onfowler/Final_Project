import random
import time

def roll():
    return random.randint(1, 6)

class Board:
    def __init__(self):
        #Side effect - creates self.board, self.score attributes
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
        """
        Returns a string representation of the board in a text art style,
        including the current score.
        """

        board_str = ""
        for row in range(3):
            for col in range(3):
                if row < len(self.board[col + 1]):
                    board_str += f"|{self.board[col + 1][row]:^3}|"
                else:
                    board_str += "|   |"
            board_str += "\n"
        board_str += f"Score: {self.calculate_score()}"
        return board_str


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
        
        if die_value in col_values and len(col_values) < 3:
            return col_index

        if die_value in opponent_board.board[col_index] and len(col_values) < 3:
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
    for columnkey in other_board.board:
        if columnkey in board.board:
            for die in other_board.board[columnkey]:
                while die in board.board[columnkey]:
                    board.board[columnkey].remove(die)
    return board
    

def manage_game(player1_board, player2_board):
    """
    Manages the game flow, alternating between player and computer turns.

    Args:
        player1_board: The player's board.
        player2_board: The computer's board.
    """

    current_player = 1

    while not player1_board.is_full() and not player2_board.is_full():
        
        print(f"Computer Board:\n{player2_board}\n")
        print(f"Your Board:\n{player1_board}")

        roll = random.randint(1,6)
        
        print(f"\n{('You' if current_player == 1 else 'Computer')} rolled a {roll}.")

        if current_player == 1:
            while True:
                try:
                    column_choice = int(input("What column would you like to place (1, 2, 3)? "))
                    if 0 <= column_choice <= 3 and player1_board.place_die(column_choice, roll):
                        break
                    else:
                        print("Column is full or invalid. Please try again.")
                except ValueError:
                    print("Please type a column number 1, 2, 3")

            player2_board = cancel_die(player2_board, player1_board)  
        else:
            column_choice = computer_move(player2_board, player1_board, roll)
            print(f"Computer placed {roll} in column {column_choice}.\n")
            time.sleep(1.5)
            player2_board.place_die(column_choice, roll)
            player1_board = cancel_die(player1_board, player2_board)

        current_player = 3 - current_player 

    player1_score = player1_board.calculate_score()
    player2_score = player2_board.calculate_score()
    
    print(f"Player 2 Board:\n{player2_board}")
    print(f"Player 1 Board:\n{player1_board}")
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
        
