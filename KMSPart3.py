vending = {
    "IM": {"description": "Iced Milo", "price": 1.5, "quantity": 30},
    "HM": {"description": "Hot Milo", "price": 1.2, "quantity": 20},
    "IC": {"description": "Iced Coffee", "price": 1.5, "quantity": 2},
    "HC": {"description": "Hot Coffee", "price": 1.2, "quantity": 2},
    "1P": {"description": "100 Plus", "price": 1.1, "quantity": 50},
    "CC": {"description": "Coca cola", "price": 1.3, "quantity": 50},
}


def add_drink_type(drink_id, description, price, quantity):
    vending[drink_id] = {"description": description, "price": price, "quantity": quantity}


def replenish_drink(drink_id, quantity):
    vending[drink_id]['quantity'] += quantity


while True:
    vendor = input("Are you a vendor?(Y/N): ").upper()
    if vendor == "N":
        counter = 0
        price = 0
        drinks_bought = []
        print("Welcome to ABC Vending Machine")
        print("Select from following choices to continue:")
        for i in vending:
            if vending[i]["quantity"] == 0:
                vending[i]["quantity"] = "** Out Of Stocks **"
            print("%s. %s ($%s) QTY: %s" % (i, vending[i]["description"], vending[i]["price"], vending[i]["quantity"]))
        while True:
            choice = input("Enter choice:").upper()
            if choice == "0":
                break
            if choice in vending:
                if vending[choice]["quantity"] == 0:
                    vending[choice]["quantity"] = "** Out Of Stocks **"
                    print(vending[choice]["description"], "already out of stocks!")
                    print("Number of drink selected = ", counter)
            counter += 1
            if choice in vending:
                try:
                    drinks_bought.append(choice)
                    int(vending[choice]['quantity'])
                    vending[choice]['quantity'] -= 1
                    price += vending[choice]["price"]
                    print("Number of drink selected = ", counter)
                except ValueError:
                    counter -= 1
                    for i in vending:
                        print("%s. %s ($%s) QTY: %s" % (i, vending[i]["description"], vending[i]["price"], vending[i][
                            "quantity"]))
                    print(vending[choice]["description"], "already out of stocks!")
                    print("Number of drink selected = ", counter)
            elif choice == "0":
                break
            else:
                print("Invalid option")
                counter -= 1
        if price > 0:
            while True:
                print("Please pay: $%.2f" % price)
                print("Indicate your payment:")
                while True:
                    note10 = input("Enter no. of $10 note:")
                    if note10.isnumeric():
                        break
                    else:
                        print("Please Enter an integer")
                        continue
                price = price - (int(note10) * 10)
                if price <= 0:
                    price = -price
                    print("Please collect your change: $%.2f" % price)
                    print("Drink paid.Thank you.")
                    break
                else:
                    print("$%.2f more" % price)
                    while True:
                        note5 = input("Enter no. of $5 note:")
                        if note5.isnumeric():
                            break
                        else:
                            print("Please Enter an integer")
                            continue
                    price = price - (int(note5) * 5)
                    if price <= 0:
                        price = -price
                        print("Please collect your change: $%.2f" % price)
                        print("Drink paid.Thank you.")
                        break
                    else:
                        print("$%.2f more" % price)
                        while True:
                            note2 = input("Enter no. of $2 note:")
                            if note2.isnumeric():
                                break
                            else:
                                print("Please Enter an integer")
                                continue
                        price = price - (int(note2) * 2)
                        if price <= 0:
                            price = -price
                            print("Please collect your change: $%.2f" % price)
                            print("Drink paid.Thank you.")
                            break

                        else:
                            print("Take your cash back!")
                            cancel = input("Do you want to cancel the purchase? Y/N:").upper()
                            if cancel == "Y":
                                print("Purchased is cancelled. Thank you.")
                                for i in drinks_bought:
                                    vending[i]['quantity'] += 1
                                break
                            elif cancel == "N":
                                continue
    elif vendor == "Y":
        while True:
            print("Select from following choices to continue:")
            print("1. Add Drink Type")
            print("2. Replenish Drink")
            print("0. Exit")
            choice = int(input("Enter choice:"))
            if choice == 1:
                while True:
                    drink_id = input("Enter Drink ID:").upper()
                    if drink_id not in vending:
                        description = input("Enter description of drink: ")
                        while True:
                            price = input("Enter price: ")
                            try:
                                float(price)
                                break
                            except ValueError:
                                continue
                        while True:
                            quantity = input("Enter quantity: ")
                            if quantity.isnumeric():
                                break
                            else:
                                "Please enter an integer."
                        add_drink_type(drink_id, description, price, quantity)
                        print(drink_id, "has been added")
                        break
                    else:
                        print("ID already used")
            elif choice == 2:
                for i in vending:
                    if vending[i]["quantity"] == "** Out Of Stocks **":
                        vending[i]["quantity"] = 0
                    print("%s. %s (%s) QTY: %s" % (i, vending[i]["description"], vending[i]["price"], vending[i][
                        "quantity"]))
                drink_id = input("Enter drink ID of the drink you want to replenish: ").upper()
                if drink_id in vending:
                    if vending[drink_id]["quantity"] <= 5:
                        replenish = int(input("How many to replenish: "))
                        replenish_drink(drink_id, replenish)
                        print(vending[drink_id]["description"], "has been replenish")
                    else:
                        print("No need to replenish. Quantity is greater than 5")
                else:
                    print("No drink with this drink id. Try again")
            elif choice == 0:
                break
    else:
        print("Invalid Input. Please enter Y or N")
