chicken_menu_price = 10.35
fish_menu_price = 12.40
vegetarian_menu_price= 8.15

chicken_menu = int(input()) * chicken_menu_price
fish_menu = int(input()) * fish_menu_price
vegetarian_menu = int(input()) * vegetarian_menu_price
desert = (chicken_menu + fish_menu + vegetarian_menu) / 5

print(chicken_menu + fish_menu + vegetarian_menu +desert + 2.50)
