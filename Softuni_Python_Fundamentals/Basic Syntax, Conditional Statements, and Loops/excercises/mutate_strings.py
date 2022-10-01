string_one = input()
string_two = input()

for index, char in enumerate(string_one):
    if string_one[index] is string_two[index]:
        continue
    else:
        print(string_two[:index+1] + string_one[index+1:])
