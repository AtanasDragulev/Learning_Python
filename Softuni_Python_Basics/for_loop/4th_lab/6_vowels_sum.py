text = input()
total = 0

for i in range(len(text)):
    if text[i] == "a":
        total += 1
    elif text[i] == "e":
        total += 2
    elif text[i] == "i":
        total += 3
    elif text[i] == "o":
        total += 4
    elif text[i] == "u":
        total += 5

print(total)
