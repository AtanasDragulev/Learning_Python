product_name = input()

is_fruit = product_name == "banana" or product_name == "apple" or product_name == "kiwi" or \
    product_name == "cherry" or product_name == "lemon" or  product_name == "grapes"
is_vegetable = product_name == "tomato" or product_name == "cucumber" or \
               product_name == "pepper" or product_name == "carrot"

if is_fruit:
    print("fruit")
elif is_vegetable:
    print("vegetable")
else:
    print("unknown")
    