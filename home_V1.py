# this is the home part of the program(includes all the program features)
def home():
    print(""" ***Choose activity number*** 
    1. Solutions
    2. Waste calculator
    3. Instructions""")
    acti_input = input("""    : """)
    if acti_input == "1":
        solutions()
    elif acti_input == "2":
        waste_calc()
    elif acti_input == "3":
        instruction()
    else:
        print("Thanks for using the program")


home()
