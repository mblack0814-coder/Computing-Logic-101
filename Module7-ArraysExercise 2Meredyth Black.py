
coffee_shop_items = {
    'coffee': 2,
    'whipped cream': .89,
    'cinnamon': .25,
    'chocolate sauce': .59,
    'amaretto': 1.50,
    'irish whiskey': 1.75
}

user_input = []
total = 0
while user_input != 'done':
    user_input = input("Enter a your order or enter 'done' to finish: ")
    if user_input in coffee_shop_items:
        print(f"The price of {user_input} is ${coffee_shop_items[user_input]}")
        total += coffee_shop_items[user_input]
    elif user_input != 'done':
        print("Sorry, we do not carry that.")
        break
print("Your order total: $"+str (total)) 