def instruction():
    print("""                               **INSTRUCTIONS** 
    Welcome to the Ocean Pollution app. This app consists of few things.
    1. Waste calculator:
            Where you calculate the amount of waste you create compared to the average person,
            and how to reduce it.
    2. Quiz:
            Where you can test your knowledge about Ocean Pollution.
    3. Solutions:
            List of solutions you can perform to reduce waste.
    4. Instructions:
            Just in case you wanted to see Instruction again.  

    **If you want to go back to Home section, Type Home[H]**
    If you are presented with options to choose from, Enter the corresponding number to the option
    If you want to quit the program type, Quit[Q]""")
    redo_home = check_redo_or_home(""" Enter Home['H'] to return to home
        : """)
    if redo_home == "redo":
        pass
    elif redo_home == "home":
        home()
    elif redo_home == "quit":
        exit()
    else:
        print("Please enter valid option")


def week_year(question):
    while True:
        try:
            string = input(question).strip().lower()
            if string == "w" or string == "weekly":
                return "Week"
            elif string == "y" or string == "yearly":
                return "Year"
            else:
                print("Please enter valid option")
        except TypeError:
            print("Please choose a valid option")


# this checks if the user wants to redo or wants to return to home
def check_redo_or_home(question):
    while True:
        try:
            checker = input(question).strip().lower()
            if checker == "redo" or checker == "r":
                return "redo"
            elif checker == "h" or checker == "home":
                return "home"
            elif checker == "q" or checker == "quit":
                return "quit"
            else:
                print("Please input a valid option")
        except TypeError:
            print("Please input a valid option")


# yearly calculations
def waste_calc_year(waste_kg):
    # amount of waste produced by a average person in a year
    garbage_year = 3200
    # amount of waste produced by the user per week compared to average person
    # if user produces more waste than average
    if waste_kg > garbage_year:
        waste_change = waste_kg - garbage_year
        waste_percent = (waste_kg / garbage_year) * 100
        waste_percent_change = waste_percent - 100
        store_info["more_less"] = "More"
        store_info["percentage"] = str(round(waste_percent_change))
        store_info["amount"] = str((round(waste_change)))
    # if user produces less waste than average
    elif waste_kg < garbage_year:
        waste_change = garbage_year - waste_kg
        waste_percent = (waste_kg / garbage_year) * 100
        waste_percent_change = 100 - waste_percent
        store_info["more_less"] = "Less"
        store_info["percentage"] = str(round(waste_percent_change))
        store_info["amount"] = str((round(waste_change)))
    # if user produces the same amount as the average
    elif waste_kg == round(garbage_year):
        pass
    # if the input is invalid
    else:
        print("Enter valid number!")


# weekly calculations
def waste_calc_week(waste_kg):
    # amount of waste produced by a average person in a week
    garbage_week = 3200 / 52
    # amount of waste produced by the user per week compared to average person
    # if the user produces more waste than average
    if waste_kg > garbage_week:
        waste_change = waste_kg - garbage_week
        waste_percent = (waste_kg / garbage_week) * 100
        waste_percent_change = waste_percent - 100
        store_info["more_less"] = "More"
        store_info["percentage"] = str(round(waste_percent_change))
        store_info["amount"] = str((round(waste_change)))
    # if the user produces less waste than average
    elif waste_kg < garbage_week:
        waste_change = garbage_week - waste_kg
        waste_percent = (waste_kg / garbage_week) * 100
        waste_percent_change = 100 - waste_percent
        store_info["more_less"] = "Less"
        store_info["percentage"] = str(round(waste_percent_change))
        store_info["amount"] = str((round(waste_change)))
    # if user produces the same amount of waste as average
    elif waste_kg == round(garbage_week):
        pass
    # if the input is invalid
    else:
        print("Enter valid number!")


# this dictionary will store info about the users production of garbage
store_info = {"more_less": "", "percentage": "", "amount": ""}


def waste_calc():
    waste_time = week_year("Do you want calculate Weekly['W'] or Yearly['Y']: ")
    print("Please Enter waste amount in kg!")
    amount_waste = int(input("""Please enter the approximate amount of waste 'garbage' you produce in a {} in kg: """
                             .format(waste_time)))
    if waste_time == "Week":
        waste_calc_week(amount_waste)
    elif waste_time == "Year":
        waste_calc_year(amount_waste)

    if amount_waste == 62 or amount_waste == 3200:
        print("""You produce the exact amount of garbage produced by an average New Zealander in a {}
Which is 62kg""".format(waste_time))
    else:
        print("""You produce {0}kg {1} garbage in a {2} compared to an average New Zealander!
Which is {3}% {1} garbage!""".format(store_info["amount"], store_info["more_less"], waste_time, store_info["percentage"]))
    redo_home = check_redo_or_home("""Enter Redo['R'] to redo or Home['H'] to return to home
    : """)
    if redo_home == "redo":
        waste_calc()
    elif redo_home == "home":
        home()
    else:
        print("Please enter valid option")


# this is the home part of the program(includes all the program features)
def home():
    print(""" ***Choose activity number*** 
    1. Waste calculator
    2. Instruction""")
    acti_input = input("""    : """)
    if acti_input == "1":
        waste_calc()
    elif acti_input == "2":
        instruction()
    else:
        print("Thanks for using the program")


name_amount = 0
while True:
    if name_amount == 0:
        name_amount += 1
        name = input("What is your name: ").title()
        print("""**Welcome {} to Ocean app**""".format(name))
        home()
    else:
        pass
