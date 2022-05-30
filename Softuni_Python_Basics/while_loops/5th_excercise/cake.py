cake_width = int(input())
cake_length = int(input())
pieces = cake_width * cake_length

current = input()
while pieces >= 0:
    if current == "STOP":
        break
    pieces -= int(current)
    if pieces <= 0:
        break
    current = input()

if pieces <= 0:
    print(f"No more cake left! You need {abs(pieces)} pieces more.")
else:
    print(f"{abs(pieces)} pieces are left.")
