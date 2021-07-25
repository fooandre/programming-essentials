# Author: Cheryl Choo Ying Chi
# Admin No: <Admin Num>

inventory = {
    "IM": {"description": "Iced Milo", "price": 1.5, "quantity": 2},
    "HM": {"description": "Hot Milo", "price": 1.2, "quantity": 20},
    "IC": {"description": "Iced Coffee", "price": 1.5, "quantity": 2},
    "HC": {"description": "Hot Coffee", "price": 1.2, "quantity": 0},
    "1P": {"description": "100 Plus", "price": 1.1, "quantity": 50},
    "CC": {"description": "Coca Cola", "price": 1.3, "quantity": 50},
    "JT": {"description": "Jasmine Tea", "price": 2.3, "quantity": 50}
}


def add_drink_type(drink_id, description, price, quantity):
    inventory.update(
        {
            drink_id: {
                "description": description,
                "price": price,
                "quantity": quantity
            }
        }
    )


def replenish_drink(drink_id, quantity):
    new_quantity = inventory[drink_id]["quantity"] + quantity
    inventory[drink_id]["quantity"] = new_quantity
    print(drink_id, "has been top up!")


while True:
    vendor = input("Are you a vendor (Y/N)? ").upper()

    total = 0
    drinks = 0

    if vendor == 'Y' or vendor == 'N':
        if vendor == 'N':
            print("Welcome to ABC Vending Machine.")
            print("Select from following choices to continue:")

            for item in inventory:
                if inventory[item]['quantity'] > 0:
                    quantity = f"Qty: {inventory[item]['quantity']}"
                else:
                    quantity = "***out of stock***"
                print(
                    f"{item}. {inventory[item]['description']} (S${inventory[item]['price']}) {quantity}")

            print("0. Exit / Payment")

            drinks = []

            while True:
                choice = input("Enter choice: ").upper()

                if choice == "0":
                    break
                elif choice == "IM" or choice == "IC":
                    if inventory[choice]["quantity"] == 0:
                        print(choice, "is out of stock")
                    else:
                        total += 1.5
                        drinks.append(choice)
                        inventory[choice]["quantity"] -= 1
                        print("No. of drinks selected =", len(drinks))
                elif choice == "HM" or choice == "HC":
                    if inventory[choice]["quantity"] == 0:
                        print(choice, "is out of stock")
                    else:
                        total += 1.2
                        drinks.append(choice)
                        inventory[choice]["quantity"] -= 1
                        print("No. of drinks selected =", len(drinks))
                elif choice == "1P":
                    if inventory[choice]["quantity"] == 0:
                        print(choice, "is out of stock")
                    else:
                        total += 1.1
                        drinks.append(choice)
                        inventory[choice]["quantity"] -= 1
                        print("No. of drinks selected =", len(drinks))
                elif choice == "CC":
                    if inventory[choice]["quantity"] == 0:
                        print(choice, "is out of stock")
                    else:
                        total += 1.3
                        drinks.append(choice)
                        inventory[choice]["quantity"] -= 1
                        print("No. of drinks selected =", len(drinks))
                else:
                    print("Invalid option")

            if total > 0:
                paid = 0
                change = paid - total

                print(f"Please pay: ${total}0")
                print("Indicate your payment:")

                while True:
                    try:
                        tens = int(input("Enter no. of $10 notes: "))
                        paid += tens * 10

                        if paid >= total:
                            change = paid - total
                            print(f"Please collet your change: ${change}0")
                            print("Drinks paid. Thank you")
                            break

                        fives = int(input("Enter no. of $5 notes: "))
                        paid += fives * 5

                        if paid >= total:
                            change = paid - total
                            print(f"Please collet your change: ${change}0")
                            print("Drinks paid. Thank you")
                            break

                        twos = int(input("Enter no. of $2 notes: "))
                        paid += twos * 2

                        if paid >= total:
                            change = paid - total
                            print(f"Please collet your change: ${change}0")
                            print("Drinks paid. Thank you")
                            break
                        else:
                            print("Not enough to pay for the drinks")
                            print("Take back your cash!")

                            user_input = input(
                                "Do you wanna cancel the purchase? Y/N: ").upper()

                            if user_input == "Y":
                                print("Purchase is cancelled. Thank you.")

                                for drink in drinks:
                                    inventory[drink]["quantity"] += 1

                                break

                    except:
                        print("Please enter a valid input")
        else:
            print("1. Add Drink Type")
            print("2. Replenish Drink")
            print("0. Exit")

            while True:
                choice = input("Enter choice: ")

                if choice == "0":
                    break
                elif choice == "1":
                    while True:
                        try:
                            drink_id = input("Enter drink id: ").upper()

                            if drink_id == "" or drink_id.isnumeric():
                                print("Please enter a valid drink id")
                                continue

                            if drink_id not in inventory:
                                break

                            print("Drink id exists!")
                        except:
                            print("Please enter a valid drink id")

                    while True:
                        description = input("Enter description of drink: ")

                        if description == "":
                            print("Please enter a valid description")
                            continue

                        break

                    while True:
                        try:
                            price = float(input("Enter price: $"))
                            break
                        except:
                            print("Please enter a valid price")

                    while True:
                        try:
                            quantity = int(input("Enter quantity: "))
                            break
                        except:
                            print("please enter a valid quantity")

                    add_drink_type(drink_id, description, price, quantity)
                elif choice == "2":
                    while True:
                        try:
                            drink_id = input("Enter drink id: ").upper()

                            if drink_id == "" or drink_id.isnumeric():
                                print("Please enter a valid drink id")
                                continue

                            if drink_id in inventory:
                                break

                            print("No drink with this drink id. Try again.")
                        except:
                            print("Please enter a valid drink id")

                    while True:
                        if inventory[drink_id]["quantity"] > 5:
                            print(
                                "No need to replenish. Quantity is greater than 5.")
                            break

                        try:
                            quantity = int(input("Enter quantity: "))
                            replenish_drink(drink_id, quantity)
                            break
                        except:
                            print("please enter a valid quantity")

                else:
                    print("Invalid option")
    else:
        print("Please enter a valid answer")
