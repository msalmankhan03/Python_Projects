# Simple Cafeteria Management System

# Menu with 5 items and their prices
menu = {
    1: {"name": "Coffee", "price": 2.5},
    2: {"name": "Sandwich", "price": 5.0},
    3: {"name": "Burger", "price": 6.5},
    4: {"name": "Juice", "price": 3.0},
    5: {"name": "Cake", "price": 4.0}
}

# Function to show the menu to the user
def show_menu():
    print("\n--- Cafeteria Menu ---")
    for key, item in menu.items():
        print(f"{key}. {item['name']} - ${item['price']}")  # show item number, name and price

# Function to take the order from the user
def take_order():
    order = {}  # to store what the user orders
    while True:
        show_menu()
        try:
            # asking user for item choice
            choice = int(input("Enter the item number to order (0 to finish): "))
            if choice == 0:
                break  # if user enters 0, stop taking order
            if choice not in menu:
                print("Invalid choice. Try again.")
                continue
            quantity = int(input(f"How many {menu[choice]['name']}s? "))
            if quantity <= 0:
                print("Quantity must be at least 1.")
                continue
            # if item already in order, add more
            if choice in order:
                order[choice]['quantity'] += quantity
            else:
                # new item added to order
                order[choice] = {
                    "name": menu[choice]['name'],
                    "price": menu[choice]['price'],
                    "quantity": quantity
                }
            print(f"{quantity} x {menu[choice]['name']} added.")
        except ValueError:
            print("Please enter a valid number.")
    return order

# Function to print the final bill
def print_bill(order):
    print("\n--- Your Order ---")
    total = 0  # to calculate total cost
    for item in order.values():
        item_total = item['price'] * item['quantity']
        print(f"{item['quantity']} x {item['name']} - ${item_total:.2f}")
        total += item_total
    print(f"Total Bill: ${total:.2f}")
    return total

# Main function to run the whole system
def main():
    print("Welcome to the Cafeteria!")
    order = take_order()  # get the order from user
    if not order:
        print("No items were ordered. Goodbye!")
        return
    total = print_bill(order)  # show the bill
    confirm = input("Do you want to confirm and buy? (yes/no): ").strip().lower()
    if confirm == 'yes':
        print(f"Thank you! Please pay ${total:.2f}. Enjoy your food!")
    else:
        print("Order cancelled. See you next time!")

# Run the program
if __name__ == "__main__":
    main()
