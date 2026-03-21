import random

# INSTRUCTIONS
def display_intructions():
    print("Use W/A/S/D to move tiles and combine numbers to reach 2048!")
    print("This version is kept very simple for beginners.")
    input("\nPress Enter to return to the menu...")

# DIFFICULTY SELECTION
def choose_difficulty():
    print("Choose difficulty:")
    print("1. Easy (6x6)")
    print("2. Medium (5x5)")
    print("3. Hard (4x4)")


def create_grid(size):
    return [[0] * size for _ in range(size)]

# SIMPLE 2048 GAME (WSAD + SCORE)

def show(board, score):
    print("Score:", score)
    for row in board:
        print(" ".join(f"{n:4}" for n in row))
    print()

def add(board):
    size = len(board)
    while True:
        r = random.randint(0, size - 1)
        c = random.randint(0, size - 1)
        if board[r][c] == 0:
            board[r][c] = 2
            break

def merge_left(row):
    """Merge a single row to the left and return score gained."""
    row = [n for n in row if n != 0]
    score_gain = 0
    i = 0
    while i < len(row) - 1:
        if row[i] == row[i+1]:
            row[i] *= 2
            score_gain += row[i]
            del row[i+1]
        i += 1
    row += [0] * (len_size - len(row))
    return row, score_gain

def rotate(board):
    """Rotate board clockwise."""
    return [list(row) for row in zip(*board[::-1])]

def move(board, direction):
    """Move in any direction using rotation."""
    global len_size
    size = len(board)
    len_size = size

    score_gain = 0

    if direction == "up":
        board = rotate(board)
    elif direction == "right":
        board = rotate(rotate(board))
    elif direction == "down":
        board = rotate(rotate(rotate(board)))

    for r in range(size):
        board[r], gain = merge_left(board[r])
        score_gain += gain

    if direction == "up":
        board = rotate(rotate(rotate(board)))
    elif direction == "right":
        board = rotate(rotate(board))
    elif direction == "down":
        board = rotate(board)

    return board, score_gain

def play_game(board):
    score = 0

    add(board)
    add(board)
    show(board, score)

    while True:
        move_key = input("Move (W/A/S/D, Q to quit): ").lower()

        if move_key == "a":
            board, gain = move(board, "left")
        elif move_key == "d":
            board, gain = move(board, "right")
        elif move_key == "w":
            board, gain = move(board, "up")
        elif move_key == "s":
            board, gain = move(board, "down")
        elif move_key == "q":
            print("Exiting game...")
            break
        else:
            print("Invalid input")
            continue

        score += gain
        add(board)
        show(board, score)

# MAIN MENU
def main_menu():

    print("=== 2048 ===")
    print("1. Play Game")
    print("2. Instructions")

    choice = input("Choose an option: ")

    if choice == "1":
        choose_difficulty()
        diff = input("Select difficulty: ")

        if diff == "1":
            print("Easy mode selected")
            grid = create_grid(6)

        elif diff == "2":
            print("Medium mode selected")
            grid = create_grid(5)

        elif diff == "3":
            print("Hard mode selected")
            grid = create_grid(4)

        else:
            print("Invalid difficulty")
            grid = None

        if grid:
            play_game(grid)

    elif choice == "2":
        display_intructions()
        main_menu()

    else:
        print("Invalid choice.")

# START PROGRAM
if __name__ == "__main__":
    main_menu()
