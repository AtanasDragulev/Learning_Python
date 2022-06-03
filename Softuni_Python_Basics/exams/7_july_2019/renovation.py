import math

wall_height = int(input())
wall_width = int(input())
skip_percent = int(input())
skip_percent = skip_percent / 100
to_paint = (wall_height * wall_width * 4)
to_paint -= math.ceil(to_paint * skip_percent)
paint_amount = input()
is_done = False
while paint_amount != "Tired!":
    current_paint = int(paint_amount)
    to_paint -= current_paint
    if to_paint <= 0:
        is_done = True
        break
    paint_amount = input()

if is_done and to_paint < 0:
    print(f"All walls are painted and you have {abs(to_paint)} l paint left!")
elif is_done:
    print("All walls are painted! Great job, Pesho!")
else:
    print(f"{abs(to_paint)} quadratic m left.")
