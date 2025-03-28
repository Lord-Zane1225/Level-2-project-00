# functions
def not_blank(question):
    """Checks that a user response is not blank"""

    while True:
        response = input(question)

        if response != "":
            return response

        print("Sorry, this can't be blank. Please try again. \n")
        print()


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


def string_check(question, valid_answers=('yes', 'no'), letter_amt_req=1):
    """Checks that users enter the full world or a chosen amount of letters of a word from a list of valid responses. """

    while True:

        response = input(question).lower()

        for item in valid_answers:
            if response == item:
                return item

            elif response == item[:letter_amt_req]:
                return item

        print(f"Please choose an answer from {valid_answers[0]} / {valid_answers[1]}. ")


# main routine

# initialise variables / non-default options
payment_ans = ('cash', 'credit')

while True:
    print()
    name = not_blank("Name: ")

    if name == "xxx":
        break

    # check age
    print()
    age = num_check("Age: ", "integer")

    if age < 12:
        print(f"Sorry, but {name} is too young for this movie. ")
        continue
    elif age > 120:
        print(f"That looks like a typo (too old) ")
        continue
    else:
        pass

    # ask user how they want to pay
    print()
    pay_method = string_check("How would you like to pay? ", payment_ans, 2)
    print()
    print(f"{name} has bought a ticket with {pay_method}. ")
