def display_intructions():
    print("Use W/A/S/D to move tiles and combine numbers to reach 2048!")

def choose_difficulty():
    print("Choose difficulty:")
    print("1. Easy (6x6)")
    print("2. Medium (5x5)")
    print("3. Hard (4x4)")

def create_grid(size):
    return [[0] * size for _ in range(size)]


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
        for row in grid:
            print(row)

elif choice == "2":
    display_intructions()

else:
    print("Invalid choice.")
