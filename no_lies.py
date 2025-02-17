# functions go here.
def int_check(question):
    """Checks that users enter an integer more than 0"""
    error = "Oops - Please enter an integer. "
    while True:
        response = input(question).lower()

        try:
            # return response if it's an integer
            response = int(response)

            return response

        except ValueError:
            print(error)


def not_blank(question):
    """Checks that a user response is not blank"""

    while True:
        response = input(question)

        if response != "":
            return response

        print("Sorry, this can't be blank. Please try again. \n")


# Main routine

while True:
    print()

    # ask user for their name
    name = not_blank("Name: ")
    # ask user for their age and check it's between 12 and 120
    age = int_check("Age: ")

    # Output error / success message
    if age < 12:
        print(f"{name} is too young. ")
        continue
    elif age > 120:
        print(f"{name} is too old. ")
        continue
    else:
        print(f"{name} bought a ticket")
