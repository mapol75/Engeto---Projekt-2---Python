"""
projekt_2.py: druhý projekt do Engeto Online Python Akademie

author: Martin Polák
email: mapol@centrum.cz
"""

# Importy nejsou třeba, hra nevyžaduje žádné knihovny

def print_intro():
    print("Welcome to Tic Tac Toe")
    print("=" * 40)
    print("GAME RULES:")
    print("Each player can place one mark (or stone)")
    print("per turn on the 3x3 grid. The WINNER is")
    print("who succeeds in placing three of their")
    print("marks in a:")
    print("* horizontal,\n* vertical or\n* diagonal row")
    print("=" * 40)
    print("Let's start the game")


def create_board():
    """Vrátí list 9 pozic jako herní plochu."""
    return [" "] * 9


def print_board(board):
    print("=" * 40)
    for i in range(0, 9, 3):
        print("+---+---+---+")
        print(f"| {board[i]} | {board[i+1]} | {board[i+2]} |")
    print("+---+---+---+")
    print("=" * 40)


def player_input(board, player):
    """Zpracuje vstup hráče a aktualizuje plochu."""
    while True:
        move = input(f"Player {player} | Please enter your move number (1-9): ")
        if not move.isdigit():
            print("Invalid input. Please enter a number between 1 and 9.")
            continue
        move = int(move)
        if move < 1 or move > 9:
            print("Invalid number. Please enter a number between 1 and 9.")
            continue
        if board[move - 1] != " ":
            print("This field is already taken. Choose another one.")
            continue
        board[move - 1] = player
        break


def check_win(board, player):
    """Zkontroluje, zda daný hráč vyhrál."""
    win_conditions = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),  # horizontální
        (0, 3, 6), (1, 4, 7), (2, 5, 8),  # vertikální
        (0, 4, 8), (2, 4, 6)             # diagonální
    ]
    return any(board[a] == board[b] == board[c] == player for a, b, c in win_conditions)


def check_draw(board):
    """Zkontroluje, zda došlo k remíze."""
    return all(cell != " " for cell in board)


def main():
    print_intro()
    board = create_board()
    current_player = "O"

    while True:
        print_board(board)
        player_input(board, current_player)

        if check_win(board, current_player):
            print_board(board)
            print(f"Congratulations, the player {current_player} WON!")
            print("=" * 40)
            break

        if check_draw(board):
            print_board(board)
            print("It's a DRAW!")
            print("=" * 40)
            break

        # Střídání hráčů
        current_player = "X" if current_player == "O" else "O"


if __name__ == '__main__':
    main()
