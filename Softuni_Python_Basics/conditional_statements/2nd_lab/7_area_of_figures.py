from math import pi

figure_type = input()
area = 0

if figure_type == "square":
    side_a = float(input())
    area = side_a * side_a
elif figure_type == "rectangle":
    side_a =float(input())
    side_b = float(input())
    area = side_a * side_b
elif figure_type == "circle":
    radius = float(input())
    area = pi * radius * radius
elif figure_type == "triangle":
    tr_height = float(input())
    tr_width = float(input())
    area = (tr_width * tr_height) / 2

print(f'{area:.3f}')