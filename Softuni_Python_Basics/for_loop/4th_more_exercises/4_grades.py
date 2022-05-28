students = int(input())
under_three = 0
under_four = 0
under_five = 0
over_five = 0
total_score = 0

for i in range(students):
    current = float(input())
    total_score += current
    if current < 3:
        under_three += 1
    elif current < 4:
        under_four += 1
    elif current < 5:
        under_five += 1
    else:
        over_five += 1

over_five = over_five / students * 100
under_five = under_five / students * 100
under_four = under_four / students * 100
under_three = under_three / students * 100
average = total_score / students

print(f"Top students: {over_five:.2f}%")
print(f"Between 4.00 and 4.99: {under_five:.2f}%")
print(f"Between 3.00 and 3.99: {under_four:.2f}%")
print(f"Fail: {under_three:.2f}%")
print(f"Average: {average:.2f}")
