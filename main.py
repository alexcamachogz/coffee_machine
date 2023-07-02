from resources import menu, resources

money = {
    "quarters": 0.25,
    "dimes": 0.10,
    "nickles": 0.05,
    "pennies": 0.01
}


def print_report():
    for key in resources:
        if key == "money":
            print(f"{key.title()}: ${resources[key]}")
        elif key == "coffee":
            print(f"{key.title()}: {resources[key]}g")
        else:
            print(f"{key.title()}: {resources[key]}ml")


def payment(price):
    user_payment = 0
    print("Please insert coins.")
    for coin, value in money.items():
        user_payment += float(input(f"How many {coin}?: ")) * value
    if user_payment < price:
        print("Sorry that's not enough money. Money refunded.")
        return False

    change = "{:.2f}".format(user_payment - price)
    print(f"Here is ${change} in change.")
    resources["money"] += price
    return True


def check_stock(ingredients):
    for ingredient, amount in ingredients.items():
        if resources.get(ingredient, 0) < amount:
            return False, ingredient
    return True, ""


def update_stock(ingredients):
    for ingredient, amount in ingredients.items():
        resources[ingredient] -= amount


while True:
    option_selected = input("What would you like? (espresso/latte/cappuccino): ")

    if option_selected == "off":
        print("Coffee machine is turn off! Goodbye.")
        break
    elif option_selected == "report":
        print_report()
    elif option_selected in menu:
        drink = menu[option_selected]
        is_available, missing_ingredient = check_stock(drink["ingredients"])

        if not is_available:
            print(f"Sorry there is not enough {missing_ingredient}.")
        else:
            if payment(drink["cost"]):
                update_stock(drink["ingredients"])
                print(f"Here is your {option_selected} ☕️. Enjoy!")
    else:
        print("Invalid selection. Please try again.")

