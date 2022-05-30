import sys
current = input()
max_number = -sys.maxsize

while current != "Stop":
    number = int(current)
    if number > max_number:
        max_number = number
    current = input()

print(max_number)
