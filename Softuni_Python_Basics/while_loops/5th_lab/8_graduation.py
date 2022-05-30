student_name = input()
grade = 1
total_score = 0
failed = 0

while grade <= 12:
    if failed > 1:
        break
    current_score = float(input())
    if current_score < 4.00:
        failed += 1
        continue
    total_score += current_score
    grade += 1

if failed > 1:
    print(f"{student_name} has been excluded at {grade} grade")
else:
    total_score /= 12
    print(f"{student_name} graduated. Average grade: {total_score:.2f}")
