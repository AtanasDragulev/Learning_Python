number = int(input())
counter = 0

for x_one in range(number+1):
    for x_two in range(number+1):
        for x_tree in range(number+1):
            if x_one + x_two + x_tree == number:
                counter += 1
print(counter)