# checks if the users input is a digit, if not print error message
def num_validator(num):
    while True:
        try:
            num_value = int(input(num))
            return num_value
        except ValueError:
            print("Please choose a valid number")


# this checks if the users input is a string, if not print error message
def string_validator(string):
    while True:
        try:
            string = input(string).strip().lower()
            return string
        except TypeError:
            print("Please choose a valid choice")


# this is the home part of the program(includes all the program features)
def home():
    print(""" ***Choose activity number***
    1. Waste calculator
    2. Solutions
    3. Instruction""")
    acti_input = num_validator("""    : """)
    if acti_input == 1:
        waste_calc()
    elif acti_input == 2:
        solutions()
    elif acti_input == 3:
        instruction()
    else:
        print("Thanks for using the program")
