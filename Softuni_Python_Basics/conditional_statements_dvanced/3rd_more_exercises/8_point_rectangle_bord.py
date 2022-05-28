x_one = float(input())
y_one = float(input())
x_two = float(input())
y_two = float(input())
x = float(input())
y = float(input())

is_border_x = (x == x_one or x == x_two) and (y >= y_one and y <= y_two)
is_border_y = (y == y_one or y == y_two) and (x >= x_one and x <= x_two)

if is_border_x or is_border_y:
    print("Border")
else:
    print("Inside / Outside")
