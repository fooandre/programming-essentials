# Author: Andre Foo
# Admin No: 210119U

prompt_user = True

while prompt_user:
    is_user_vendor = input("Are you a vendor (Y/N)? ")

    is_user_vendor = is_user_vendor.upper()

    prompt_user = False if is_user_vendor == 'Y' else False if is_user_vendor == 'N' else True
    user_is_vendor = True if is_user_vendor == "Y" else False if is_user_vendor == "N" else print(
        "Please enter a valid answer"
    )

drink_menu = [
    "IM. Iced Milo (S$1.5)",
    "HM. Hot Milo (S$1.2)",
    "IC. Iced Coffee (S$1.5)",
    "HC. Hot Coffee (S$1.2)", "1P. 100 Plus (S$1.1)",
    "CC. Coca Cola (S$1.3)",
    "0. Exit / Payment"
]

drink_list = {
    "IM": 1.5,
    "HM": 1.2,
    "IC": 1.5,
    "HC": 1.2,
    "1P": 1.1,
    "CC": 1.3
}

vendor_menu = [
    "1. Add Drink Type",
    "2. Replenish Drink",
    "0. Exit"
]

vendor_list = {
    "1": "Add Drink Type",
    "2": "Replenish Drink",
    "0": "Mkay bye"
}

notes_accepted = [10, 5, 2]


def display_menu(vendor):
    menu = vendor_menu if vendor else drink_menu

    print("Welcome to ABC Vending Machine. \nSelect from following choices to continue:")

    for item in menu:
        print(item)


def get_user_input(vendor):
    user_is_choosing = True

    total = 0
    drinks_selected = 0

    if vendor:
        user_input = input("Enter choice: ")
        try:
            print(vendor_list[user_input])
            return vendor_list[user_input]
        except:
            print("Invalid option")
    else:
        while user_is_choosing:
            user_input = input("Enter choice: ")

            if user_input == "0":
                user_is_choosing = False
                return total

            try:
                user_input = user_input.upper()

                total += drink_list[user_input]
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
        print(f"Please pay: {round(owed, 3)}\nIndicate your payment: ")

        amount_paid = 0
        enough_paid = False

        for note_value in notes_accepted:
            notes_given = input(f"Enter no. of ${note_value} notes: ")

            try:
                notes_given = int(notes_given)
                amount_paid += notes_given * note_value
                change_owed = amount_paid - owed
                enough_paid = True if amount_paid >= owed else False

                if enough_paid:
                    print(
                        f"Please collect your change: ${change_owed}\nDrinks paid. Thank you."
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
        return "Please enter a valid answer"

    print("Purchase is cancelled. Thank you.") if cancel == "Y" else ask_for_payment(owed)


def vending_machine_UI(vendor):
    display_menu(vendor)
    get_user_input(vendor) if vendor else ask_for_payment(calculate_total())


vending_machine_UI(user_is_vendor)
