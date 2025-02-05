def not_blank(question):
    """Checks that a user response is not blank"""

    while True:
        response = input(question)

        if response != "":
            return response
        elif response != "":
            return response

        print("Sorry, this can't be blank or include any numbers. Please try again. \n")


who = not_blank("Please enter your name: ")
print(f"Hello {who}")
