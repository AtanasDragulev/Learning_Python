number_one = int(input())
number_two = int(input())

for number in range(number_one, number_two+1):
    as_string = str(number)
    even_part = int(as_string[0]) + int(as_string[2]) + int(as_string[4])
    odd_part = int(as_string[1]) + int(as_string[3]) + int(as_string[5])
    if even_part == odd_part:
        print(number, end=" ")