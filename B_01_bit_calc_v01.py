# Functions go here
def statement_generator(statement, decoration):
    print(f"\n{decoration * 5} {statement} {decoration * 5}")


def instructions():
    statement_generator("Instructions", "-")
    print('''
This program calculates how many bits are needed to store:
- Integers
- Images
- Text

Choose a file type and follow the prompts.
Type 'xxx' at any time to exit.
    ''')


# Checks for valid integer input
def int_check(question, low):
    error = f"Please enter a number that is more than or equal to {low}\n"

    while True:
        try:
            response = int(input(question))
            if response >= low:
                return response
            else:
                print(error)
        except ValueError:
            print(error)


# Ask user for file type
def get_filetype():
    while True:
        response = input("File type (integer / image / text): ").lower()

        if response == "xxx":
            return "xxx"

        elif response in ['integer', 'int', 'i']:
            return "integer"

        elif response in ['image', 'picture', 'img', 'p']:
            return "image"

        elif response in ['text', 'txt', 't']:
            return "text"

        else:
            print("Please enter a valid file type.")


# Integer calculation
def integer_calc():
    integer = int_check("Integer: ", 0)

    binary = bin(integer)[2:]
    num_bits = len(binary)

    return f"{integer} in binary is {binary}. We need {num_bits} bits to represent it."


# Image calculation
def image_calc():
    width = int_check("Width: ", 1)
    height = int_check("Height: ", 1)

    num_pixels = width * height
    num_bits = num_pixels * 24

    return (f"Number of pixels: {width} x {height} = {num_pixels}"
            f"\nNumber of bits: {num_pixels} x 24 = {num_bits}")


# Text calculation
def calc_text_bits():
    response = input("Enter some text: ")

    num_chars = len(response)
    num_bits = num_chars * 8

    return (f"{response} has {num_chars} characters."
            f"\nWe need {num_chars} x 8 bits = {num_bits} bits.")


# Main routine
want_instructions = input("Press <enter> to read instructions or any key to continue: ")

if want_instructions == "":
    instructions()


while True:
    file_type = get_filetype()

    if file_type == "xxx":
        print("Goodbye!")
        break

    if file_type == "integer":
        print(integer_calc())

    elif file_type == "image":
        print(image_calc())

    else:
        print(calc_text_bits())