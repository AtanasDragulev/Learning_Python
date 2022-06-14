from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_machine = CoffeeMaker()
money_machine = MoneyMachine()
is_on = True
while is_on:
    action = input(f"What would you like ({menu.get_items()})")
    if action == "report":
        coffee_machine.report()
        money_machine.report()
    elif action == "off":
        is_on = False
    elif action in menu.get_items():
        drink = menu.find_drink(action)
        if coffee_machine.is_resource_sufficient(drink):
            if not money_machine.make_payment(drink.cost):
                continue
            coffee_machine.make_coffee(drink)

 