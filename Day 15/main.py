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
            "water": 250,
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
}

profit = 0


def print_remaining_resources(resources_remaining, profits):
    """Prints report of remaining resources and profits so far"""
    print(f"Water: {resources_remaining['water']}ml")
    print(f"Milk: {resources_remaining['milk']}ml")
    print(f"Coffee: {resources_remaining['coffee']}g")
    print(f"Money: ${profits}")


def is_resource_enough(resources_remaining, choice):
    """Returns True is resources are enough, False if not enough"""
    resources_not_enough = []
    chosen_menu_ingredients = MENU[choice]["ingredients"]
    for ingredient in chosen_menu_ingredients:
        if resources_remaining[ingredient] <= chosen_menu_ingredients[ingredient]:
            resources_not_enough.append(ingredient)
    if len(resources_not_enough) > 0:
        print(f"Sorry there is not enough {', '.join(resources_not_enough)}")
        return False
    else:
        return True


def get_coins():
    """Function to accept coins for transaction and calculate total accepted payment"""
    print("Please insert coins.")
    quarters_accepted = int(input("how many quarters?: "))
    dimes_accepted = int(input("how many dimes?: "))
    nickles_accepted = int(input("how many nickles?: "))
    pennies_accepted = int(input("how many pennies?: "))
    return quarters_accepted * 0.25 + dimes_accepted * 0.1 + nickles_accepted * 0.05 + pennies_accepted * 0.01


def process_transaction(accepted_payment, cost, coffee_chosen):
    """Process accepted payment and return changes. Also add to total profits.
    If accepted payment not enough, then refund"""
    global profit
    if accepted_payment >= cost:
        changes = round(accepted_payment - cost, 2)
        profit += cost
        print(f"Here is ${changes} in change.")
        print(f"Here is your {coffee_chosen} ☕ Enjoy!")
    else:
        print("Sorry that's not enough money. Money refunded.")


def make_coffee(resources_remaining, ingredients):
    """Deduct the ingredients from remaining resources"""
    for ingredient in ingredients:
        resources_remaining[ingredient] -= ingredients[ingredient]


def coffee_machine():
    continue_business = True

    while continue_business:
        user_choice = input("  What would you like? (espresso/latte/cappuccino): ").lower()
        if user_choice == "report":
            print_remaining_resources(resources, profit)
        elif user_choice == "off":
            continue_business = False
        else:
            if user_choice in MENU:
                if is_resource_enough(resources, user_choice):
                    total_accepted_money = get_coins()
                    make_coffee(resources, MENU[user_choice]["ingredients"])
                    process_transaction(total_accepted_money, MENU[user_choice]["cost"], user_choice)
            else:
                print("Not a valid choice. Please choose again.")
                continue


coffee_machine()
