# functions goes here.
def num_check(question, num_type, exit_code=None):
    """Checks that users enter an integer / float more than 0 (or optional exit code)"""
    if num_type == "integer":
        error = "Oops - Please enter an integer (no decimals) more than 0"
        change_to = int
    else:
        error = "Oops - Please enter a number more than 0"
        change_to = float

    while True:
        response = input(question).lower()

        # checks for the exit code
        if response == exit_code:
            return response
        try:
            # check response is an integer and is more than 0
            response = change_to(response)

            if response > 0:
                return response
            else:
                print(error)

        except ValueError:
            print(error)


# main routine goes here

# loop for testing purposes...
while True:
    print()

    my_float = num_check("Please enter a number more than 0. ", "float")
    print(f"Thanks. You chose {my_float}")
    print()

    my_int = num_check("Please enter an integer more than 0", "integer", "")

    if my_int == "":
        print("You have chosen infinite mode. ")
        print()
    else:
        print(f"Thanks. You chose {my_int}")
        print()
