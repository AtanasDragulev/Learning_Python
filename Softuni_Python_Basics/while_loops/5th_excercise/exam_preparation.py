max_not_enough = int(input())
not_enough = 0
total_score = 0
total_tasks = 0
is_failed = False
last_task = ""
current_task = input()
current_score = int(input())

while True:
    total_tasks += 1
    if current_score <= 4:
        not_enough += 1
    if not_enough == max_not_enough:
        is_failed = True
        break
    total_score += current_score
    last_task = current_task
    current_task = input()
    if current_task == "Enough":
        break
    current_score = int(input())

if is_failed:
    print(f"You need a break, {max_not_enough} poor grades.")
else:
    total_score = total_score / total_tasks
    print(f"Average score: {total_score:.2f}")
    print(f"Number of problems: {total_tasks}")
    print(f"Last problem: {last_task}")
