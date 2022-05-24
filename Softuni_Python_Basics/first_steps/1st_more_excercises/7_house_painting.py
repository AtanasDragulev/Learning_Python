needed_green = 3.4
needed_red = 4.3
door = 1.2 * 2
window = 1.5 * 1.5

base_height = float(input())
side_length = float(input())
top_height = float(input())

front_back = (base_height * base_height) * 2 - door
sides = (side_length * base_height) * 2 - (window * 2)
needed_green = (front_back + sides) / needed_green
print(f'{needed_green:.2f}')

roof_side = (base_height * side_length) * 2
roof_triangles = (base_height * top_height /2) * 2
needed_red = (roof_side + roof_triangles) / needed_red
print(f'{needed_red:.2f}')
