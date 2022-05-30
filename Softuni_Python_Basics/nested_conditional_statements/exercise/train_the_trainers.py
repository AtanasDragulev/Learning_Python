members = int(input())
presentation_counter = 0
total_average = 0
presentation_name = input()
while presentation_name != "Finish":
    presentation_counter += 1
    score = 0
    for i in range(members):
        current = float(input())
        score += current
    average = score / members
    total_average += average
    print(f"{presentation_name} - {average:.2f}.")
    presentation_name = input()
total_average /= presentation_counter
print(f"Student's final assessment is {total_average:.2f}.")
