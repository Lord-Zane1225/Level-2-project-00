# functions go here.
def string_check(question, valid_ans_list, letter_amt_req):
    """Checks that users enter the full world or a chosen amount of letters of a word from a list of valid responses. """

    while True:

        response = input(question).lower()

        for item in valid_ans_list:
            if response == item:
                return item

            elif response == item[:letter_amt_req]:
                return item

        print(f"Please choose an answer from {valid_ans_list}. ")


# main routine goes here.
yes_no_list = ['yes', 'no']
payment_list = ['cash', 'credit']

like_coffee = string_check("Do you like coffee? ", yes_no_list, 1)
print(f"You chose {like_coffee}. ")
choose_payment = string_check("Choose a payment type: ", payment_list, 2)
print(f"You chose {choose_payment}. ")
