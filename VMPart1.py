# Author: Andre Foo
# Admin No: 210119U

# will be True until user inputs a valid answer
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
    "IM": {"description": "Iced Milo", "price": 1.5},
    "HM": {"description": "Hot Milo", "price": 1.2},
    "IC": {"description": "Iced Coffee", "price": 1.5},
    "HC": {"description": "Hot Coffee", "price": 1.2},
    "1P": {"description": "100 Plus", "price": 1.1},
    "CC": {"description": "Coca Cola", "price": 1.3}
}

# dictionary of vendor menu and possible choices to choose from
vendor_menu = {
    "1": "Add Drink Type",
    "2": "Replenish Drink"
}

# array of notes accepted for payment
notes_accepted = [10, 5, 2]


# dynamically displays menu depending on user's status
def display_menu(vendor):
    # select which menu to display according to whether user is vendor
    menu = vendor_menu if vendor else drinks
    exit_statement = "0. Exit" if vendor else "0. Exit / Payment"

    print("Welcome to ABC Vending Machine. \nSelect from following choices to continue:")

    # iterate through and print each item in selected menu
    for choice in menu:
        if vendor:
            print(f"{choice}. {vendor_menu[choice]}")
        else:
            print(
                f"{choice}. {drinks[choice].get('description')} ({drinks[choice].get('price')})")

    print(exit_statement)


# logic for handling user input
def get_user_input(vendor):
    # will be True until user enters a "0"
    user_is_choosing = True

    # initialise variables to store cost and number of drinks selected (default value set to 0), needed if user is customer
    total, drinks_selected = 0, 0

    if vendor:
        # get user input
        choice = input("Enter choice: ")

        # return out of function if user inputs "0" so except block won't run
        if choice == "0":
            return

        try:
            # print user input
            print(vendor_menu[choice])
        except:
            # throw a warning if user input is not in vendor menu and
            # call the function again to get user input
            print("Invalid option")
            get_user_input(True)
    else:
        while user_is_choosing:
            # get drink of user's choosing
            drink = input("Enter choice: ")

            # break out of loop if user enters a "0"
            if drink == "0":
                user_is_choosing = False
                return total

            try:
                # capitalize user input
                drink = drink.upper()

                # add cost of selected drink to total
                total += drinks[drink].get("price")

                # increment number of drinks selected by 1
                drinks_selected += 1

                print(f"No. of drinks selected: {drinks_selected}")
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


# calls the highest level function
vending_machine_UI(user_is_vendor)
