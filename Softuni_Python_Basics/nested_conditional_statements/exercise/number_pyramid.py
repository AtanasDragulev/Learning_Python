number = int(input())
number_to_print = 1

for num in range(1, number + 1):
    current_row = ""
    for row in range(num):
        if number_to_print > number:
            break
        current_row += (str(number_to_print)) + " "
        number_to_print += 1
    print(current_row)
    if number_to_print > number:
        break
