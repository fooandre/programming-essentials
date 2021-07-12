# Author: Andre Foo
# Admin No: 210119U

prompt_user = False

while prompt_user:
    is_user_vendor = input("Are you a vendor (Y/N)? ")

    is_user_vendor = is_user_vendor.upper()

    prompt_user = False if is_user_vendor == 'Y' else False if is_user_vendor == 'N' else True
    user_is_vendor = True if is_user_vendor == "Y" else False if is_user_vendor == "N" else print(
        "Please enter a valid answer"
    )

inventory = {
    'IM': {'description': 'Iced Milo', 'price': 1.5, 'quantity': 30},
    'IC': {'description': 'Iced Coffee', 'price': 1.5, 'quantity': 40},
    'CC': {'description': 'Coca Cola', 'price': 1.3, 'quantity': 50}
}

vendor_menu = {
    "1": "Add Drink Type",
    "2": "Replenish Drink",
    "0": "Mkay bye"
}

notes_accepted = [10, 5, 2]


def add_drink_type():
    prompt_user = True

    while prompt_user:
        drink_id = input("Enter drink id: ")

        drink_id = drink_id.upper()

        prompt_user = False if inventory.get(drink_id) != None else True

        try:
            description = input("Enter description of drink: ")
            error_message = "PLease enter a valid description"
            description = description.capitalize()

            price = input("Enter price: $ ")
            error_message = "PLease enter a valid price"
            price = int(price)

            quantity = input("Enter quantity: ")
            error_message = "PLease enter a valid number"
            quantity = int(quantity)
        except:
            return error_message


# add_drink_type()
# drink_id = "JT"
# description = "Jasmine Tea"
# price = 2.3
# quantity = 50
# inventory.update(
#     {drink_id: {"description": description, "price": price, "quantity": quantity}}
# )
# for drink in inventory:
#     print(drink)


def display_menu(vendor):
    menu = vendor_menu if vendor else inventory

    print("Welcome to ABC Vending Machine.\nSelect from following choices to continue:")

    for item in menu:
        list = f"{item}. {menu[item]}" if vendor else f"{item}. {menu[item].get('description')} (S${menu[item].get('price')}"

        print(list)


def get_user_input(vendor):
    user_is_choosing = True

    total = 0
    drinks_selected = 0

    while user_is_choosing:
        user_input = input("Enter choice: ")

        try:
            if user_input == "0":
                user_is_choosing = False
                return total

            if vendor:
                print(vendor_menu[user_input])
                return vendor_menu[user_input]

            user_input = user_input.upper()

            total += inventory[user_input].get("price")
            drinks_selected += 1
            print(f"No. of drinks selected: {drinks_selected}")
        except:
            print("Invalid option")


def calculate_total():
    return get_user_input(user_is_vendor)


def ask_for_payment(owed):
    if owed == 0:
        print("Mkay bye")
    else:
        print(f"Please pay: ${round(owed, 2)}0\nIndicate your payment: ")

        amount_paid = 0
        enough_paid = False

        for note_value in notes_accepted:
            notes_given = input(f"Enter no. of ${note_value} notes: ")

            try:
                notes_given = int(notes_given)
                amount_paid += notes_given * note_value
                enough_paid = True if amount_paid >= owed else False

                if enough_paid:
                    change_owed = amount_paid - owed

                    print(
                        f"Please collect your change: ${change_owed}0\nDrinks paid. Thank you."
                    )

                    return
            except:
                print("Please enter a valid number")
                return ask_for_payment(owed)

        print("Not enough to pay for the drinks\nTake back your cash!")
        cancel_transaction(owed)


def cancel_transaction(owed):
    cancel = input("Do you want to cancel the purchase? Y/N: ")

    cancel = cancel.upper()

    if cancel != "Y" and cancel != "N":
        print("Please enter a valid answer")
        return cancel_transaction(owed)

    print("Purchase is cancelled. Thank you.") if cancel == "Y" else ask_for_payment(owed)


def vending_machine_UI(vendor):
    display_menu(vendor)
    get_user_input(True) if vendor else ask_for_payment(calculate_total())


# vending_machine_UI(user_is_vendor)
