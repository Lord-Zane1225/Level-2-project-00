# functions go here.

def yes_no_check(question):
    """Checks that user inputs either <Yes> or <No>. """
    while True:
        # asks user for input and makes it lowercase.
        user_yesno = input(question).lower()

        # checks what user entered and returns answer or asks user again.
        if user_yesno == "yes" or user_yesno == "y":
            return "yes"

        elif user_yesno == "no" or user_yesno == "n":
            return "no"
        else:
            print("Please input either <yes> (y) or <no> (n). ")


# main routine goes here.
# loop for testing.
while True:
    # calling yes no function.
    user_answer = yes_no_check("Enter yes or no ")
    print(f"you entered {user_answer}. ")
