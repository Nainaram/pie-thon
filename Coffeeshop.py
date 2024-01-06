# Define the menu with nested dictionaries
menu = {
    'coffee': {
        'black': 2.00,
        'latte': 3.50,
        'cappuccino': 3.00,
    },
    'tea': {
        'green': 2.50,
        'black': 2.00,
        'herbal': 2.50,
    },
    'extras': {
        'sugar': 0.25,
        'cream': 0.50,
    }
}

def coffee_machine():
    print("Welcome to the Coffee Machine!")

    # Ask the customer if they would like to order
    order_preference = input("Would you like to place an order? (yes/no): ")

    if order_preference.lower() == 'yes':
        print("Great! Here is the menu:")
        
        # Display the menu
        for category, items in menu.items():
            print(f"\n{category.capitalize()} Menu:")
            for item, price in items.items():
                print(f"{item.capitalize()}: ${price:.2f}")

        # Ask for the customer's order
        customer_order = {}
        while True:
            category = input("\nEnter the category you'd like to order from (coffee/tea/extras): ").lower()
            
            if category in menu:
                item = input(f"Select {category} item: ").lower()
                if item in menu[category]:
                    customer_order[item] = menu[category][item]
                else:
                    print("Invalid item. Please choose again.")
            else:
                print("Invalid category. Please choose again.")
            
            another_order = input("Do you want to add another item to your order? (yes/no): ")
            if another_order.lower() != 'yes':
                break

        # Display the customer's order
        print("\nYour Order:")
        for item, price in customer_order.items():
            print(f"{item.capitalize()}: ${price:.2f}")

        # Calculate the total price
        total_price = sum(customer_order.values())
        print(f"\nTotal Price: ${total_price:.2f}")

        # Ask for confirmation to proceed with the order
        confirm_order = input("Do you want to proceed with the order? (yes/no): ")
        if confirm_order.lower() == 'yes':
            print("Thank you for your order! Enjoy your drink.")
        else:
            print("Order canceled. Have a great day!")

    else:
        print("No problem. If you change your mind, we're here for you!")

# Run the coffee machine program
coffee_machine()
