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
profit=0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

# TODO: 1.Print report of all coffee machine resources.
# TODO: 2. Check whether resources are sufficient to make a coffee.


def is_resource_sufficient(order_gradients):
    """ returns whether the resources are sufficient"""
    for items in order_gradients:
        if(order_gradients[items]) >= resources[items]:
            print(f"Sorry, your drink {items} can't be prepared")
            return False
        else:
            return True


def process_coins(q, d, n, p):
    """ returns the monetary value"""
    my_dict = {'quarters': 0.25, 'dimes': 0.1, 'nickels': 0.05, 'pennies': 0.01, }
    monetary_value = my_dict['quarters']*q + my_dict['dimes']*d + my_dict['nickels']*n + my_dict['pennies']*p
    return monetary_value


def check_transaction_successful(money_received, drink_cost):
    if money_received > drink_cost:
        change = round(money_received-drink_cost, 2)
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry not enough money, previous amounts refunded.")
        return False





    _



is_on = True
while is_on:
    choice = input("what the heck do you want")
    if choice == "off":
        is_on = False
    elif choice == "report":
        print(f"Water: {resources['water']} ")
        print(f"Milk:   {resources['milk']}")
        print(f"Coffee: {resources['coffee']}")
        print(f"Money:  ${profit}")
    else:
        drink = MENU[choice]
        if is_resource_sufficient(drink['ingredients']):
            quarters = int(input("Enter the number of quarters"))
            dimes = int(input("Enter the number of dimes"))
            nickels = int(input("Enter the number of nickels"))
            pennies = int(input("Enter the number of pennies"))
            payment= process_coins(quarters, dimes, nickels, pennies)
            check_transaction_successful(payment, drink['cost'])







