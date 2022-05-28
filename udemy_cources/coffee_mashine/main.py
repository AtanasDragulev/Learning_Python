MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 240,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0
}
is_on = True


def report():
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${resources['money']}")


def check_resources(_drink):
    is_enough = True
    current = MENU[_drink]["ingredients"]
    for _ingredient in current:
        if resources[_ingredient] < current[_ingredient]:
            print(f"Sorry there is not enough {_ingredient}")
            is_enough = False
    if not is_enough:
        return False
    return True


def check_coins(_drink):
    print("Please insert coins.")
    quarters = int(input("how many quarters?: ")) * 0.25
    dimes = int(input("how many dimes?: ")) * 0.10
    nickles = int(input("how many nickles?: ")) * 0.05
    pennies = int(input("how many nickles?: ")) * 0.01
    total = quarters + dimes + nickles + pennies
    if MENU[_drink]["cost"] > total:
        print("Sorry that's not enough money. Money refunded.")
        return False
    elif MENU[_drink]["cost"] < total:
        print(f'Here is ${total - MENU[_drink]["cost"]} in change')
        return True
    return True


while is_on:
    # Todo: 1 Prompt user by asking “ What would you like? (espresso/latte/cappuccino):
    action = input("What would you like? (espresso/latte/cappuccino): ").lower()

    # Todo: 2 Turn off the Coffee Machine by entering “ off ” to the prompt.
    if action == "off":
        is_on = False
        continue
    # Todo: 3 Print report
    if action == "report":
        report()
        continue
    # Todo: 4 Check resources
    if check_resources(action):
        if not check_coins(action):
            continue
    else:
        continue

    # Todo: 7 Make drink
    current_recipe = MENU[action]["ingredients"]
    for ingredient in current_recipe:
        resources[ingredient] -= current_recipe[ingredient]
    resources["money"] += MENU[action]["cost"]
