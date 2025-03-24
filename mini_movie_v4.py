import pandas
import random


# functions
def make_statement(statement, decoration):
    """Emphasises headings by adding decorations
    at the start and end"""

    return f"{decoration * 3} {statement} {decoration * 3}"


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

        for func_item in valid_answers:
            if response == func_item:
                return func_item

            elif response == func_item[:letter_amt_req]:
                return func_item

        print(f"Please enter either {valid_answers[0]} or {valid_answers[1]}. ")


def instructions():
    print(make_statement("Instructions", "ℹ️"))

    print('''

For each ticket holder enter: 
- Their name
- Their age
- The payment method (cash / credit)

The program will record the ticket sale and calculate the 
ticket cost (and profit). 

Once you have either sold all of the tickets or entered the 
exit code ('xxx'), the program will display the ticket sales 
information and write the data to a text file. 

It will also choose one lucky ticket holder who wins the 
draw (their ticket is free). 
    ''')


def currency(x):
    """Formats numbers as currency ($#.##)"""
    return "${:.2f}".format(x)


# main routine

# initialise ticket numbers
MAX_TICKETS = 5
tickets_sold = 0
# initialise variables / non-default options
payment_ans = ('cash', 'credit')

# ticket price list
CHILD_PRICE = 7.50
ADULT_PRICE = 10.50
SENIOR_PRICE = 6.50

# credit card surcharge
CREDIT_SURCHARGE = 0.05

# pandas lists
all_names = []
all_ticket_costs = []
all_surcharges = []

# dictionary
mini_movie_dict = {
    'Name': all_names,
    'Ticket Price': all_ticket_costs,
    'Surcharge': all_surcharges
}

# program main heading
print(make_statement("Mini Movie Fundraiser Tickets", "🍿"))
print()
# ask user if they want to see instructions
want_instructions = string_check("Would you like to read the instructions? ")
if want_instructions == "yes":
    # print instructions if wanted
    instructions()
print()
# Loop to get name, age and payment details
while tickets_sold < MAX_TICKETS:

    # ask user for their name
    name = not_blank("Name: ")

    # exit code
    if name == "xxx":
        break

    # check age and output error if too young / old
    print()
    age = num_check("Age: ", "integer")

    if age < 12:
        print(f"Sorry, but {name} is too young for this movie. ")
        print()
        continue

    # child ticket $7.50
    elif age < 16:
        ticket_price = CHILD_PRICE

    # adult ticket $10.50
    elif age < 65:
        ticket_price = ADULT_PRICE

    # senior ticket $6.50
    elif age < 121:
        ticket_price = SENIOR_PRICE

    elif age > 120:
        print(f"That looks like a typo (too old) ")
        print()
        continue
    else:
        ticket_price = 0
        pass

    # ask user what payment method
    pay_method = string_check("How would you like to pay? ", payment_ans, 2)
    print()

    # if paying through credit calculate surcharge.
    if pay_method == "cash":
        surcharge = 0
    else:
        surcharge = ticket_price * CREDIT_SURCHARGE

    all_names.append(name)
    all_ticket_costs.append(ticket_price)
    all_surcharges.append(surcharge)

    tickets_sold += 1

# --- End of ticket loop ---

# create dataframe / table from directory
mini_movie_frame = pandas.DataFrame(mini_movie_dict)

# calculate total payable & profit for each ticket
mini_movie_frame['Total'] = mini_movie_frame['Ticket Price'] + mini_movie_frame['Surcharge']
mini_movie_frame['Profit'] = mini_movie_frame['Ticket Price'] - 5.00

total_paid = mini_movie_frame['Total'].sum()
total_profit = mini_movie_frame['Profit'].sum()

# choose a random winner
winner = random.choice(all_names)

# find index of winner (position in list)
winner_index = all_names.index(winner)

# retrieve total won
profit_won = mini_movie_frame.at[winner_index, 'Total']
ticket_won = mini_movie_frame.at[winner_index, 'Total']

add_dollars = ['Ticket Price', 'Surcharge', 'Total', 'Profit']
for var_item in add_dollars:
    mini_movie_frame[var_item] = mini_movie_frame[var_item].apply(currency)

# print mini movie frame
mini_movie_string = mini_movie_frame.to_string(index=False)

total_paid_string = f"total paid : ${total_paid:.2f}"
total_profit_string = f"total profit : ${total_profit:.2f}"

lucky_winner_string = f"The lucky winner is {winner}. Their ticket worth ${ticket_won:.2f} is free!"

final_total_paid_string = "Total paid is now ${total_paid - ticket_won:.2f}"
final_profit_string = "Total profit is now ${total_profit - profit_won:.2f}"


if tickets_sold == MAX_TICKETS:
    num_sold_string = make_statement(f"You have sold all the tickets (ie: {MAX_TICKETS} tickets).", "-")
else:
    num_sold_string = make_statement(f"You have sold {tickets_sold} tickets.", "-")

# additional strings / headings
heading_string = make_statement("Mini Movie Fundraiser", "=")
ticket_details_heading = make_statement("Ticket details", "-")
raffle_heading = make_statement("Raffle winner", "-")
adjusted_sales_heading = make_statement("Adjusted Sales & Profit", "-")

adjusted_explanation = (f"We have given away a ticket worth ${ticket_won:.2f} "
                        f"which \nmeans our sales have decreased by ${ticket_won:.2f} \n"
                        f"and our profit by ${profit_won:.2f}")

# list of strings to be outputted / written to file
to_write = [
    heading_string, "\n",
    ticket_details_heading,
    mini_movie_string, "\n",
    total_paid_string,
    total_profit_string, "\n",
    raffle_heading,
    lucky_winner_string, "\n",
    adjusted_sales_heading,
    adjusted_explanation, "\n",
    final_total_paid_string,
    final_profit_string, "\n",
    num_sold_string]

# print area
print()
for item in to_write:
    print(item)


# create file to hold data (add txt extension)
file_name = "MMF_ticket_details"
write_to = "{}.txt".format(file_name)

text_file = open(write_to, "w+")


# write the item to the file
for item in to_write:
    text_file.write(item)
    text_file.write("\n")
