# functions
def make_statement(statement, decoration):
    """Emphasises headings by adding decorations
    at the start and end"""

    print(f"{decoration * 3} {statement} {decoration * 3}")


def string_check(question, valid_answers=('yes', 'no'), letter_amt_req=1):
    """Checks that users enter the full world or a chosen amount of letters of a word from a list of valid responses. """

    while True:

        response = input(question).lower()

        for item in valid_answers:
            if response == item:
                return item

            elif response == item[:letter_amt_req]:
                return item

        print(f"Please choose an answer from {valid_answers}. ")


# main routine

# lists
payment_list = ('cash', 'credit')

make_statement("Instructions", "ℹ️")
want_instructions = string_check("Would you like to read the instructions? ")
print(f"You chose {want_instructions}")
pay_method = string_check("How would you like to pay? ", payment_list, 2)
print(f"You chose {pay_method}")
