import random

# INSTRUCTIONS
def display_instructions():
    print("Use W/A/S/D to move tiles and combine numbers to reach 2048!")
    input("\nPress Enter to return to the menu...")

# DIFFICULTY SELECTION
def choose_difficulty():
    print("Choose difficulty:")
    print("1. Easy (6x6)")
    print("2. Medium (5x5)")
    print("3. Hard (4x4)")

    choice = input("Select difficulty: ")

    if choice == "1":
        print("Easy mode selected")
        return 6
    elif choice == "2":
        print("Medium mode selected")
        return 5
    elif choice == "3":
        print("Hard mode selected")
        return 4
    else:
        print("Invalid difficulty")
        return None

# CREATE GRID
def create_grid(size):
    return [[0] * size for _ in range(size)]

# DISPLAY BOARD
def show(board, score):
    print("Score:", score)
    for row in board:
        print(" ".join(f"{n:4}" for n in row))
    print()

# ADD NEW TILE
def add(board):
    size = len(board)
    empty = [(r, c) for r in range(size) for c in range(size) if board[r][c] == 0]
    if empty:
        r, c = random.choice(empty)
        board[r][c] = 2

# MERGE LEFT
def merge_left(row):
    size = len(row)
    row = [n for n in row if n != 0]
    score_gain = 0
    i = 0

    while i < len(row) - 1:
        if row[i] == row[i + 1]:
            row[i] *= 2
            score_gain += row[i]
            del row[i + 1]
        i += 1

    row += [0] * (size - len(row))
    return row, score_gain

# ROTATE CLOCKWISE
def rotate(board):
    return [list(row) for row in zip(*board[::-1])]

def move(board, direction):
    score_gain = 0

    if direction == "up":
        board = rotate(rotate(rotate(board)))
    elif direction == "right":
        board = rotate(rotate(board))
    elif direction == "down":
        board = rotate(board)

    # Merge left
    for r in range(len(board)):
        board[r], gain = merge_left(board[r])
        score_gain += gain

    # Rotate back
    if direction == "up":
        board = rotate(board)
    elif direction == "right":
        board = rotate(rotate(board))
    elif direction == "down":
        board = rotate(rotate(rotate(board)))

    return board, score_gain

# GAME LOOP
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
        size = choose_difficulty()
        if size:
            play_game(create_grid(size))

    elif choice == "2":
        display_instructions()
        main_menu()

    else:
        print("Invalid choice.")

# START PROGRAM
if __name__ == "__main__":
    main_menu()