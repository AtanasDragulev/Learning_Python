pass_counter = 0
password = "A"
is_found = False
control_sum = int(input())
for first in range(1,10):
    for second in range(first+1,10):
        for third in range(1,10):
            for forth in range(1, third):
                current = (first * second) + (third * forth)
                if current == control_sum:
                    print(f"{first}{second}{third}{forth}", end=" ")
                    pass_counter += 1
                if pass_counter == 4:
                    password = f"{first}{second}{third}{forth}"
                    pass_counter += 1
                    is_found = True

print()
if is_found:
    print(f"Password: {password}")
else:
    print("No!")