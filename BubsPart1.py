# Author: Cheryl Choo Ying Chi
# Admin No: <Admin Num>

while True:
    vendor = input("Are you a vendor (Y/N)? ").upper()

    total = 0
    drinks = 0

    if vendor == 'Y' or vendor == 'N':
        if vendor == 'N':
            print("Welcome to ABC Vending Machine.")
            print("Select from following choices to continue:")
            print("IM. Iced Milo (S$1.50)")
            print("HM. Hot Milo (S$1.20)")
            print("IC. Iced Coffee (S$1.50)")
            print("HC. Hot Coffee (S$1.20)")
            print("1P. 100 Plus (S$1.10)")
            print("CC. Coca Cola (S$1.30)")
            print("0. Exit / Payment")

            while True:
                choice = input("Enter choice: ").upper()

                if choice == "0":
                    break
                elif choice == "IM" or choice == "IC":
                    total += 1.5
                    drinks += 1
                    print("No. of drinks selected =", drinks)
                elif choice == "HM" or choice == "HC":
                    total += 1.2
                    drinks += 1
                    print("No. of drinks selected =", drinks)
                elif choice == "1P":
                    total += 1.1
                    drinks += 1
                    print("No. of drinks selected =", drinks)
                elif choice == "CC":
                    total += 1.3
                    drinks += 1
                    print("No. of drinks selected =", drinks)
                else:
                    print("Invalid option")

            if total > 0:
                paid = 0
                change = paid - total

                print(f"Please pay: ${total}0")
                print("Indicate your payment:")

                while True:
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
                            break

        else:
            print("1. Add Drink Type")
            print("2. Replenish Drink")
            print("0. Exit")

            while True:
                choice = input("Enter choice: ")

                if choice == "0":
                    break
                elif choice == "1":
                    print("Add Drink Type")
                elif choice == "2":
                    print("Replenish Drink")
                else:
                    print("Invalid option")

    else:
        print("Please enter a valid answer")
