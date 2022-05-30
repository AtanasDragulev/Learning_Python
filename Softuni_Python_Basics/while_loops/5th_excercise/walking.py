steps_target = 10000
steps_made = 0

while steps_made < steps_target:
    current = input()
    if current == "Going home":
        final_steps = int(input())
        steps_made += final_steps
        break
    steps_made += int(current)

difference = abs(steps_made - steps_target)
if steps_made >= steps_target:
    print("Goal reached! Good job!")
    print(f"{difference} steps over the goal!")
else:
    print(f"{difference} more steps to reach goal.")
