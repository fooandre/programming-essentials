# Author: Andre Foo
# Admin No: 210119U

from inspect import signature

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

# set the default width for alignment of output, used in display_menu()
width = 23


# checks and returns a boolean value indicating status of user
def user_is_vendor():
    # create a variable for readability
    require_input = True

    while require_input:
        # check if user is vendor, covert input to uppercase to reduce number of checks needed
        is_user_vendor = input("Are you a vendor (Y/N)? ").upper()

        # use guard clauses to exit function early if user inputs valid answer
        if is_user_vendor == "Y":
            return True

        if is_user_vendor == "N":
            return False

        # by default, loop until valid answer is given
        print("Please enter a valid answer")


# handles adding new drink into menu
def add_drink_type(drink_id, description, price, quantity):
    drinks.update(
        {
            drink_id: {
                "description": description,
                "price": price,
                "quantity": quantity
            }
        }
    )


# handles input validation for add_new_drink()
def handle_add_drink():
    # takes in the parameters needed for add_drink_type()
    params = signature(add_drink_type).parameters

    # defines a skip condition
    def skip_condition(drink_id):
        if drink_id in drinks:
            print("Drink id exists!")
            return True

        return False

    # defines an end condition
    def end_condition(drink_id):
        return False

    # get needed params from user input
    args = get_function_args(params, skip_condition, end_condition)

    # call method for adding new drink and pass in all required params
    add_drink_type(*args)


# handles logic for replenishing drinks
def replenish_drink(drink_id, quantity):
    # declare a new variable to store the new quantity of selected drink after adding
    new_quantity = drinks[drink_id]["quantity"] + quantity

    # update quantity in drink list to reflect the new quantity
    drinks[drink_id]["quantity"] = new_quantity

    # output to alert the vendor that quantity has been changed
    print(drink_id, "has been top up!")


# handles input validation for replenish_drink()
def handle_replenish_drink():
    # takes in the parameters needed for add_drink_type()
    params = signature(replenish_drink).parameters

    # defines a skip condition
    def skip_condition(drink_id):
        if drink_id not in drinks:
            print("No drink with this drink id. Try again")
            return True

        return False

    # defines an end condition
    def end_condition(drink_id):
        if drinks[drink_id]["quantity"] > 5:
            print("No need to replenish. Quantity is greater than 5.")
            return True

        return False

    # get needed params from user input
    args = get_function_args(params, skip_condition, end_condition)

    # call method for adding new drink and pass in all required params
    replenish_drink(*args)


# handles getting input for vendor functions
def get_function_args(params, skip_condition, end_condition):
    # create an array to store parameters that will be passed
    args = []

    # create variable variables for readability
    need_input = True

    # interate and ask for input for every parameter needed
    for param in params:
        while need_input:
            arg = input(f"Enter {param}: ")

            # use guard clause to skip to next iteration if user gives no input
            if arg == "":
                print("Please enter a valid", param)
                continue

            try:
                # convert input to a number if needed
                if param == "price":
                    arg = float(arg)
                elif param == "quantity":
                    arg = int(arg)
                else:
                    # convert drink id to be uppercase
                    if param == "drink_id":
                        arg = arg.upper()

                    # throw error if user inputs a number
                    if arg.isnumeric():
                        print("Please enter a valid", param)
                        continue

                    # skip to next iteration if a certain condition is met
                    if skip_condition(arg):
                        continue

                    # break if a certain condition is met
                    if end_condition(arg):
                        continue
            except:
                # print an error message if input received is invalid
                print("Please enter a valid", param)
                continue

            # if input is valid, append it to an array and move on to next param
            args.append(arg)
            break

    # return arguments received
    return args


# dynamically displays menu depending on user's status and context
def display_menu(vendor, replenish=False):
    # select which menu to display according to whether user is vendor
    menu = vendor_menu if vendor else drinks

    # dynamically sets the last statement depending on whether user is vendor
    exit_statement = "0. Exit" if vendor else "0. Exit / Payment"

    if replenish:
        print("====================")
    else:
        print("Welcome to ABC Vending Machine.")
        print("Select from following choices to continue:")

    # get the last drink (new drinks get added to the back of the dictionary)
    last_drink = list(drinks.keys())[-1]

    # create variables for readability
    description = drinks[last_drink]["description"]
    price = str(drinks[last_drink]["price"])
    length = len(drinks[last_drink]) + len(description) + len(price)

    # reference global variable
    global width

    # if legnth of newly added drink is greater than current width of alignment, set new width
    if length > width:
        width = length + 9

    # iterate through and print each item in selected menu
    for item in menu:
        if vendor:
            print(f"{item}. {vendor_menu[item]}")
        else:
            # create variables to store description and price of each drink
            description, price = drinks[item]['description'], drinks[item]['price']

            # dynamically stores quantity of each drink, will be set to "***out of stock***" if it is 0
            quantity = f"Qty: {drinks[item]['quantity']}" if drinks[item]['quantity'] != 0 else "***out of stock***"

            # create variable for readability
            left_aligned = f"{item}. {description} (S${price})"

            # format and print all details for each item
            print(left_aligned.ljust(width), quantity)

    print("====================") if replenish else print(exit_statement)


# logic for handling user input
def get_user_input(vendor):
    # create variables for readability
    global drinks_selected

    user_is_choosing = True
    total = 0
    drinks_selected = {}

    # will loop indefinitely while user does not enter a "0"
    while user_is_choosing:
        choice = input("Enter choice: ")

        # guard clause, throws an error if user gives no input
        if choice == "":
            print("Invalid option")
            continue

        # break out of loop if user enters a "0"
        if choice == "0":
            user_is_choosing = False
            return total

        try:
            if vendor:
                # call the respective functions that the user chooses
                if choice == "1":
                    handle_add_drink()
                elif choice == "2":
                    display_menu(False, True)
                    handle_replenish_drink()
                else:
                    print("Invalid option")
            else:
                # capitalize user input
                choice = choice.upper()

                # check if drink is not out of stock
                if drinks[choice]["quantity"] != 0:
                    # add cost of selected drink to total
                    total += drinks[choice]["price"]

                    # add choice to drinks selected
                    if choice not in drinks_selected:
                        drinks_selected.update({choice: 1})
                    else:
                        drinks_selected[choice] += 1

                    # reduce the quantity of drink by 1
                    drinks[choice]["quantity"] -= 1

                    # print number of drinks selected
                    print(
                        f"No. of drinks selected: {sum(drinks_selected.values())}")
                else:
                    # if out of stock, throw warning
                    print(drinks[choice]["description"], "is out of stock")
        except:
            # throw warning if user inputs an invalid value
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
        print(f"Please pay: ${round(owed, 3)}\nIndicate your payment: ")

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
                enough_paid = True if amount_paid >= owed else False

                # if enough has been paid, print amount of change given and return out of function
                if enough_paid:
                    change_owed = amount_paid - owed
                    print("Please collect your change:", change_owed)
                    print("Drinks paid. Thank you.")

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
    cancel = input("Do you want to cancel the purchase? Y/N: ").upper()

    # handles canceling of transaction if user wants to, else ask for payment again
    if cancel == "Y":
        print("Purchase is cancelled. Thank you.")

        for drink in drinks_selected:
            drinks[drink]["quantity"] += drinks_selected[drink]

        return

    if cancel == "N":
        return ask_for_payment(owed)

    # throws an error if user inputs an invalid reply, and recalls function
    print("Please enter a valid answer")
    cancel_transaction(owed)


# function that handles the calling of all other functions needed, depending on whether user is vendor or not
def vending_machine_UI(vendor):
    display_menu(vendor)
    get_user_input(True) if vendor else ask_for_payment(get_total())


# calls the highest level function indefinitely until program is halted
while True:
    vending_machine_UI(user_is_vendor())

    # print new line to separete previous session from new session
    print("")
