actor_name = input()
academy_points = float(input())
critics_amount = int(input())
is_nominated = False

for i in range(critics_amount):
    current_critic = input()
    current_score = float(input())
    academy_points += (len(current_critic) * current_score) / 2
    if academy_points >= 1250.5:
        is_nominated = True
        break

if is_nominated:
    print(f"Congratulations, {actor_name} got a nominee for leading role with {academy_points:.1f}!")
else:
    difference = 1250.50 - academy_points
    print(f"Sorry, {actor_name} you need {difference:.1f} more!")
