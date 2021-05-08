from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


def main():
    continue_operate = True
    menu = Menu()
    coffee_maker = CoffeeMaker()
    money_machine = MoneyMachine()
    while continue_operate:
        user_choice = input(f" What would you like? ({menu.get_items()}): ").lower()
        if user_choice == "report":
            coffee_maker.report()
            money_machine.report()
        elif user_choice == "off":
            continue_operate = False
        else:
            drink = menu.find_drink(user_choice)
            if drink is not None:
                if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
                    coffee_maker.make_coffee(drink)
            else:
                print(f"{user_choice} is not sold here. Please choose again.")


main()
