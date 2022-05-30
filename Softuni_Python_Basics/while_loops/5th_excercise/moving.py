empty_width = int(input())
empty_length = int(input())
empty_height = int(input())
empty_space = empty_width * empty_length * empty_height
is_full = False

current = input()
while current != "Done":
    empty_space -= int(current)
    if empty_space <= 0:
        is_full = True
        break
    current = input()

empty_space = abs(empty_space)
if is_full:
    print(f"No more free space! You need {empty_space} Cubic meters more.")
else:
    print(f"{empty_space} Cubic meters left.")
