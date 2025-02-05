def not_blank(question):
    """Checks that a user response is not blank"""

    while True:
        response = input(question)

        if response == "":
            print("Please enter something")

        else:
            return response


who = not_blank("Please enter your name: ")
print(f"Hello {who}")
