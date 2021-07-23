def handle_add_drink():
    params = signature(add_drink_type).parameters

    def skip_condition(drink_id):
        return drink_id in drinks

    def end_condition(drink_id):
        return false

    args = get_user_input_for_params(params, skip_condition, end_condition)

    add_drink_type(*args)


def handle_replenish_drink():
    params = signature(replenish_drink).parameters

    def skip_condition(drink_id):
        return drink_id not in drinks

    def end_condition(drink_id):
        return drinks[drink_id]["quantity"] > 5

    args = get_user_input_for_params(params, skip_condition, end_condition)

    replenish_drink(*args)


def get_user_input_for_params(params, skip_condition, end_condition):
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
                        return
            except:
                # print an error message if input received is invalid
                print("Please enter a valid", param)
                continue

            # if input is valid, append it to an array and move on to next param
            args.append(arg)
            break

    # return arguments received
    return args
