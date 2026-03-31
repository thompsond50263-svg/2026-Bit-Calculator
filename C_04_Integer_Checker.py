# Ask user for width and loop until they
# enter a number that is more than zero
def int_check(question, low):
    error = f"Please enter a number that is more than {low}\n"

    while True:
        try:
            # ask the user for a number
            response = int(input(question))

            # check that the number is more than or equal to low
            if response >= low:
                return response
            else:
                print(error)
        except ValueError:
            print(error)


# Main Routine
for item in range(2):
    integer = int_check(question="Integer: ", low=0)
    print(integer)

print()

for item in range(2):
    width = int_check(question="Width: ", low=1)
    print(width)

for item in range(2):
    height = int_check(question="Height: ", low=1)
    print(height)