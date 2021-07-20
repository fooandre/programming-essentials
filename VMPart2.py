# Author: Andre Foo
# Admin No: 210119U

from inspect import signature

prompt_user = True

while prompt_user:
    # check if user is vendor
    is_user_vendor = input("Are you a vendor (Y/N)? ")

    # convert all user input to uppercase
    is_user_vendor = is_user_vendor.upper()

    # update prompt_user to False if input is valid, else keep it as True
    prompt_user = False if is_user_vendor == 'Y' else False if is_user_vendor == 'N' else True

    # if user input is valid, store user as vendor based on user input, else ask user to enter valid answer
    user_is_vendor = True if is_user_vendor == "Y" else False if is_user_vendor == "N" else print(
        "Please enter a valid answer"
    )

# dictionary of drinks in menu containing price and description
drinks = {
    "IM": {"description": "Iced Milo", "price": 1.5, "quantity": 2},
    "HM": {"description": "Hot Milo", "price": 1.2, "quantity": 20},
    "IC": {"description": "Iced Coffee", "price": 1.5, "quantity": 2},
    "HC": {"description": "Hot Coffee", "price": 1.2, "quantity": 0},
    "1P": {"description": "100 Plus", "price": 1.1, "quantity": 50},
    "CC": {"description": "Coca Cola", "price": 1.3, "quantity": 50},
    "JT": {"description": "Jasmine Tea", "price": 2.3, "quantity": 50},
}

# dictionary of vendor menu and possible choices to choose from
vendor_menu = {
    "1": "Add Drink Type",
    "2": "Replenish Drink"
}

# array of notes accepted for payment
notes_accepted = [10, 5, 2]

int_params = ["price", "quantity"]


# handles adding new drink into inventory
def add_drink_type(drink_id, description, price, quantity):
    if drink_id not in drinks:
        drinks.update(
            {
                drink_id: {
                    "description": description,
                    "price": price,
                    "quantity": quantity}
            }
        )
    else:
        print("Drink id exists!")


add_drink_params = signature(add_drink_type).parameters


# handles getting input for adding new drink and calling add_new_drink()
def handle_add_drink():
    args = []

    need_input = True

    for param in add_drink_params:
        while need_input:
            invalid_input = False

            arg = input(f"Enter {param}: ")

            try:
                if param in int_params:
                    arg = float(arg)
                elif arg != "":
                    arg = arg.upper() if param == "drink_id" else arg
                else:
                    invalid_input = True

                args.append(arg) if not invalid_input else none

                if args[0] in drinks:
                    print("Drink id exists!")
                    args = []
                else:
                    break

            except:
                print('Please enter a valid', param)

    add_drink_type(*args)


# handles logic for replenishing drinks
def replenish_drink(drink_id, quantity):
    # declare a new variable to store the new quantity of selected drink after adding
    new_quantity = drinks[drink_id]["quantity"] + quantity

    # update quantity in drink list to reflect the new quantity
    drinks[drink_id]["quantity"] = new_quantity

    # output to alert the vendor that quantity has been changed
    print(drink_id, "has been top up!")


replenish_drink_params = signature(replenish_drink).parameters


def handle_replenish_drink():
    args = []

    need_input = True

    for param in replenish_drink_params:
        while need_input:
            arg = input(f"Enter {param}: ")

            if param == "drink_id":
                arg = arg.upper()

                if arg not in drinks:
                    print("No drink with this drink id. Try again.")
                    continue
                elif drinks[arg]["quantity"] > 5:
                    print("No need to replenish. Quantity is greater than 5.")
                    continue
            else:
                arg = int(arg)

            args.append(arg)

            break

    replenish_drink(*args)


# dynamically displays menu depending on user's status
def display_menu(vendor):
    # select which menu to display according to whether user is vendor
    menu = vendor_menu if vendor else drinks

    # dynamically sets the last statement depending on whether user is vendor
    exit_statement = "0. Exit" if vendor else "0. Exit / Payment"

    print("Welcome to ABC Vending Machine. \nSelect from following choices to continue:")

    # iterate through and print each item in selected menu
    for item in menu:
        if vendor:
            print(f"{item}. {vendor_menu[item]}")
        else:
            # create a variable to store description and price of each drink
            description, price = drinks[item]['description'], drinks[item]['price']

            # dynamically stores quantity of each drink, will be set to "***out of stock***" if it is 0
            quantity = f"Qty: {drinks[item]['quantity']}" if drinks[item]['quantity'] != 0 else "***out of stock***"

            # format and print all details for each item
            print(f"{item}. {description} (S${price}) {quantity}")

    print(exit_statement)


# logic for handling user input
def get_user_input(vendor):
    user_is_choosing = True
    total, drinks_selected = 0, 0

    while user_is_choosing:
        choice = input("Enter choice: ")

        if choice == "0":
            user_is_choosing = False
            return total

        try:
            if vendor:
                handle_add_drink() if choice == "1" else handle_replenish_drink() if choice == "2" else none
            else:
                # capitalize user input
                choice = choice.upper()

                # check if drink is not out of stock
                if drinks[choice]["quantity"] != 0:
                    # add cost of selected drink to total
                    total += drinks[choice]["price"]

                    # increment number of drinks selected by 1
                    drinks_selected += 1

                    # print number of drinks selected
                    print(f"No. of drinks selected: {drinks_selected}")
                else:
                    # if out of stock, throw warning
                    print(drinks[choice]["description"], "is out of stock")
        except:
            # throw warning if user input is not an existing drink
            print("Invalid option")


# function that calls get_user_input(), improves readability
def get_total():
    # parameter is hardcoded as False as this function will only be called if user is not a vendor
    return get_user_input(False)


# logic to handle payment, function will be called regardless of cost
def ask_for_payment(owed):
    # breaks out of function if cost is $0
    if owed == 0:
        print("Mkay bye")
    else:
        # print amount owed and ask for payment
        print(f"Please pay: {round(owed, 3)}\nIndicate your payment: ")

        # initialise variables to store amount paid and if enough has been paid
        # set to 0 and False by default respectively
        amount_paid, enough_paid = 0, False

        # iterates through notes accepted for payment
        for note_value in notes_accepted:
            # get amount of each note given
            notes_given = input(f"Enter no. of ${note_value} notes: ")

            # calculates amount paid after each note, and sets enough_paid to True if amount paid is more than cost
            try:
                notes_given = int(notes_given)
                amount_paid += notes_given * note_value
                change_owed = amount_paid - owed
                enough_paid = True if amount_paid >= owed else False

                # if enough has been paid, print amount of change given and return out of function
                if enough_paid:
                    print(
                        f"Please collect your change: ${change_owed}\nDrinks paid. Thank you."
                    )

                    return
            except:
                # throws a warning if user did not enter a valid number of notes and recalls the function
                print("Please enter a valid number")
                return ask_for_payment(owed)

        print("Not enough to pay for the drinks\nTake back your cash!")

        # if not enough is paid after iterating through all accepted notes, allow user to cancel transaction
        cancel_transaction(owed)


# logic to handle cancellation of transaction
def cancel_transaction(owed):
    # ask user if they want to cancel the transaction
    cancel = input("Do you want to cancel the purchase? Y/N: ")

    # capitalize user input
    cancel = cancel.upper()

    # throws an error if user inputs an invalid reply, and recalls function
    if cancel != "Y" and cancel != "N":
        print("Please enter a valid answer")
        return cancel_transaction(owed)

    # cancels transaction if user wants to, else ask for payment again
    print("Purchase is cancelled. Thank you.") if cancel == "Y" else ask_for_payment(owed)


# function that handles the calling of all other functions needed, depending on whether user is vendor or not
def vending_machine_UI(vendor):
    display_menu(vendor)
    get_user_input(True) if vendor else ask_for_payment(get_total())


# calls the highest level function indefinitely until program is halted
while True:
    vending_machine_UI(user_is_vendor)
    print("")
