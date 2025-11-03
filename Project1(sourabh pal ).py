# NAME = Sourabh Pal
# Enrollment number = 2502140102
# Project name = Cafeteria / Canteen Order Manager (Mini Project 16, E-Project)

menu = {
    1: ("Veg Thali", 80),
    2: ("Paneer Roll", 60),
    3: ("Aloo Paratha", 40),
    4: ("Masala Dosa", 70),
    5: ("Idli Sambhar", 50),
    6: ("Vada Pav", 25),
    7: ("Tea", 15),
    8: ("Cold Coffee", 40),
    9: ("Chole Bhature", 90),
    10: ("Pasta", 75),
    11: ("Samosa", 10),
    12: ("Chips", 20),
    13: ("Ice Cream", 30),
    14: ("Fruit Salad", 40)
}

cart = {}

def show_dashboard():
    print("\n==========RISHIHOOD CAFE ==========\n")
    print("1. Show Menu")
    print("2. Add Item to Cart (by number)")
    print("3. View Cart")
    print("4. Remove Item from Cart")
    print("5. Show Total Bill (with Discount Option)")
    print("6. Clear Cart")
    print("7. Show Most Selling Items")
    print("8. EXIT")
    print("=======================================================")

def show_menu():
    print("\n-------------------- MENU --------------------")
    for num, (item, price) in menu.items():
        print(f"{num:2}. {item:20} ₹{price}")
    print("----------------------------------------------")

def add_item():
    while True:
        show_menu()
        try:
            num = int(input("Enter item number to add (0 to stop): "))
            if num == 0:
                print("Returning to main menu...")
                break
            if num in menu:
                qty = int(input(f"Enter quantity of {menu[num][0]}: "))
                item_name = menu[num][0]
                cart[item_name] = cart.get(item_name, 0) + qty
                print(f"{qty} x {item_name} added to cart.")
            else:
                print("Invalid item number. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def view_cart():
    if not cart:
        print("\nYour cart is empty.")
        return
    print("\n------------- Your Cart -------------")
    for item, qty in cart.items():
        price = [v[1] for k, v in menu.items() if v[0] == item][0]
        print(f"{item:20} x {qty} = ₹{price * qty}")
    print("------------------------------------")

def remove_item():
    if not cart:
        print("\nCart is empty.")
        return
    item = input("Enter item name to remove: ").strip().title()
    if item in cart:
        del cart[item]
        print(f"{item} removed from cart.")
    else:
        print("Item not found in cart.")

def show_bill():
    if not cart:
        print("\nCart is empty.")
        return
    total = sum([qty * [v[1] for k, v in menu.items() if v[0] == item][0] for item, qty in cart.items()])
    print("\n=========== BILL ===========")
    for item, qty in cart.items():
        price = [v[1] for k, v in menu.items() if v[0] == item][0]
        print(f"{item:20} x {qty} = ₹{price * qty}")
    print("----------------------------")
    print(f"Subtotal: ₹{total:.2f}")


    coupon = input("Enter discount coupon (DIS10 / DIS20 / none): ").strip().upper()
    discount = 0
    if coupon == "DIS10":
        discount = 0.10 * total
    elif coupon == "DIS20":
        discount = 0.20 * total

    total_after_discount = total - discount
    if discount > 0:
        print(f"Discount Applied: -₹{discount:.2f}")

    print(f"Total Payable: ₹{total_after_discount:.2f}")
    print("============================")

def clear_cart():
    cart.clear()
    print("Cart cleared successfully!")

def show_most_selling_items():
    print("\n------ Most Selling Items ------")
    print("1. Veg Thali")
    print("2. Vada Pav")
    print("3. Cold Coffee")
    print("4. Masala Dosa")
    print("--------------------------------")

while True:
    show_dashboard()
    choice = input("Enter your choice [1-8]: ").strip()

    if choice == "1":
        show_menu()
    elif choice == "2":
        add_item()
    elif choice == "3":
        view_cart()
    elif choice == "4":
        remove_item()
    elif choice == "5":
        show_bill()
    elif choice == "6":
        clear_cart()
    elif choice == "7":
        show_most_selling_items()
    elif choice == "8":
        print("\nThank you for visiting our RISHIHOOD cafe ")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 8.")
