askUser = input("Are you a vendor (Y/N)? ")

drinkMenu = [
    "IM. Iced Milo (S$1.5)",
    "HM. Hot Milo (S$1.2)",
    "IC. Iced Coffee (S$1.5)",
    "HC. Hot Coffee (S$1.2)", "1P. 100 Plus (S$1.1)",
    "CC. Coca Cola (S$1.3)",
    "0. Exit / Payment"
]

drinkList = {
    "IM": 1.5,
    "HM": 1.2,
    "IC": 1.5,
    "HC": 1.2,
    "1P": 1.1,
    "CC": 1.3
}

vendorMenu = [
    "1. Add Drink Type",
    "2. Replenish Drink",
    "0. Exit"
]

vendorList = ["Vendor List"]


def checkIfVendor(userInput):
    userInput = userInput.upper()

    if userInput != "Y" and userInput != "N":
        return "Please enter a valid answer"

    isVendor = True if userInput == "Y" else False
    return isVendor


def displayMenu(isVendor):
    total = 0
    drinksSelected = 0

    menu = vendorMenu if isVendor == True else drinkMenu
    list = vendorList if menu == vendorMenu else drinkList

    print("Welcome to ABC Vending Machine.")
    print("Select from following choices to continue:")

    for item in menu:
        print(item)

    while True:
        userChoice = input("Enter choice: ")

        if userChoice == "0":
            askForPayment(total) if total != 0 else False
            break

        userChoice = userChoice.upper()

        try:
            total += list[userChoice]
            drinksSelected += 1

            print(f"No. of drinks selected = {drinksSelected}")
        except:
            print("Invalid option")


def askForPayment(owed):
    print(f"Please pay: ${owed}")
    print("Indicate your payment:")

    enoughPaid = False
    amountPaid = 0

    notesAccepted = [10, 5, 2]

    while enoughPaid == False:
        for noteValue in notesAccepted:
            notesGiven = input(f"Enter no. of ${noteValue} notes: ")

            try:
                notesGiven = int(notesGiven)
                amountPaid += notesGiven * {noteValue}
                enoughPaid = True if amountPaid >= owed else False
            except:
                return "Please input a valid value"

                # if enoughPaid:
                #     print(f"Please collect your change: ${changeOwed}")


displayMenu(checkIfVendor(askUser))
