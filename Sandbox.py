# functions go here

def sandbox_first_testing():
    """Shows reminders for integers and counting characters in strings. """
    # reminder - an integer that has been multiplied by three
    number = 5
    print(number * 3)

    # string multiplied by 3
    # note speech marks and colour
    num_string = "5"
    print(num_string * 3)

    # an example showing what the
    example_text = "hello world"
    text_length = len(example_text)

    print(f"'{example_text}' is {text_length} characters long")


def sandbox_second_testing():
    fruit_list = ['apple', 'banana', 'cherry', 'dragonfruit']
    for item in fruit_list:

        print()

        # print fruit name
        print("Fruit name: ", item)

        # print first letter in name
        print("First letter: ", item[0])

        # print first 2 letters
        print("First 2 letters: ", item[0], item[1])

        # better way for printing multiple first letters
        print("First 2 letters different code: ", item[:2])
        # item[:2] uses ":" to tell program to count up to but not including number (starts from 0)


# main routine
which_sandbox = input("What sandbox? ")

if which_sandbox == "1":
    sandbox_first_testing()
elif which_sandbox == "2":
    sandbox_second_testing()
else:
    print("No sandbox of that name/type")
