start = int(input())
end = int(input())
magic_number = int(input())
combination = 0
is_found = False
first = 0
second = 0
for first in range(start, end+1):
    if is_found:
        first -= 1
        break
    for second in range(start, end+1):
        combination += 1
        if first + second == magic_number:
            is_found = True
            break

if is_found:
    print(f"Combination N:{combination} ({first} + {second} = {magic_number})")
else:
    print(f"{combination} combinations - neither equals {magic_number}")
