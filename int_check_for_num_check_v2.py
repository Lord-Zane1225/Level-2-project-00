# functions go here.
def int_check(question, low, high):
    """Checks that users enter an integer more than 0"""
    error = f"Oops - Please enter an integer more than {low} and less than {high}. "

    while True:

        try:
            # gets user's response
            response = input(question).lower()

            # check response is an integer and is more than the low value and less than the high value.
            response = int(response)

            if low <= response <= high:
                return response
            else:
                print(error)

        except ValueError:
            print(error)


# main routine
# loop for testing
while True:
    print()

    # ask user for integer
    my_num = int_check("Choose a number", 1, 10)
    print(f"you chose {my_num}")
