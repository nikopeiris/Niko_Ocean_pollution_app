import time


# this checks if the users input is a string, if not print error message
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


# checks if the users input is a digit, if not print error message
def num_validator(num):
    while True:
        try:
            num_value = float(input(num))
            if "-" in str(num_value):
                print("Please choose a valid number")
            else:
                return num_value
        except ValueError:
            print("Please choose a valid number")


def main_loader(section):
    i = 1
    i2 = 1
    print(f"Loading {section}", end="")
    while i <= 4:
        time.sleep(0.5)
        print(".", end="")
        i += 1
    print("")
    print("Loading Complete...")
    print(f"Displaying {section}", end="")
    while i2 <= 4:
        time.sleep(0.25)
        print(".", end="")
        i2 += 1
    print("\n" * 3)


def sub_loader(section):
    i = 1
    i2 = 1
    i3 = 1
    print(f"Calculating {section}", end="")
    while i <= 4:
        time.sleep(0.5)
        print(".", end="")
        i += 1
    print("")
    print("Finalising Calculations", end="")
    while i2 <= 4:
        time.sleep(0.5)
        print(".", end="")
        i2 += 1
    print("")
    print(f"Displaying {section}", end="")
    while i3 <= 4:
        time.sleep(0.25)
        print(".", end="")
        i3 += 1
    print("")


# checks if users inputs g or kg
def g_kg(string):
    while True:
        try:
            unit_value = input(string).lower().strip()
            if unit_value == "g" or unit_value == "grams":
                return "g"
            elif unit_value == "kg" or unit_value == "kilograms":
                return "kg"
            else:
                print("Please choose a valid option")
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
        store_info["percentage"] = round(waste_percent_change)
        store_info["amount_kg"] = round(waste_change)
    # if user produces less waste than average
    elif waste_kg < garbage_year:
        waste_change = garbage_year - waste_kg
        waste_percent = (waste_kg / garbage_year) * 100
        waste_percent_change = 100 - waste_percent
        store_info["more_less"] = "Less"
        store_info["percentage"] = round(waste_percent_change)
        store_info["amount_kg"] = round(waste_change)
    # if user produces the same amount as the average
    elif waste_kg == round(garbage_year):
        pass
    # if the input is invalid
    else:
        print("Enter valid number!")


# this is where the results are printed from
def display_info(g_or_kg, waste_time, info, amount_waste):
    amount_g = info["amount_kg"] * 1000
    print("""                  *** Results ***""")
    if g_or_kg == "g":
        if amount_waste == 62 or amount_waste == 3200:
            print("""You produce the exact amount of garbage produced by an average New Zealander,
Which is 62000g a Week and 3200000g a Year! """)
        else:
            print("""An average New Zealander produces around 62000g garbage a Week, and
3200000g garbage a Year.
You produce {0}g {1} garbage in a {2} compared to an average New Zealander!
Which is {3}% {1} garbage!""".format(amount_g, store_info["more_less"],
                                     waste_time, store_info["percentage"]))
    elif g_or_kg == "kg":
        if amount_waste == 62 or amount_waste == 3200:
            print("""You produce the exact amount of garbage produced by an average New Zealander,
Which is 62kg a Week and 3200kg a Year """)
        else:
            print(""" An average New Zealander produces around 62kg garbage a Week, and
3200kg garbage a Year.
You produce {0}kg {1} garbage in a {2} compared to an average New Zealander!
Which is {3}% {1} garbage!""".format(store_info["amount_kg"],
                                     store_info["more_less"], waste_time,
                                     store_info["percentage"]))
    else:
        pass


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
        store_info["percentage"] = round(waste_percent_change)
        store_info["amount_kg"] = round(waste_change)
    # if the user produces less waste than average
    elif waste_kg < garbage_week:
        waste_change = garbage_week - waste_kg
        waste_percent = (waste_kg / garbage_week) * 100
        waste_percent_change = 100 - waste_percent
        store_info["more_less"] = "Less"
        store_info["percentage"] = round(waste_percent_change)
        store_info["amount_kg"] = round(waste_change)
    # if user produces the same amount of waste as average
    elif waste_kg == round(garbage_week):
        pass
    # if the input is invalid
    else:
        print("Enter valid number!")


def waste_calc():
    main_loader("Waste Calculator")
    print("""            *** Waste Calculator ***""")
    waste_time = week_year("Do you want calculate Weekly['W'] or Yearly['Y']:")
    g_or_kg = g_kg("Would you like to calculate in grams[g] or kilograms[kg]:")
    amount_waste = num_validator("Please enter the approximate amount of waste/rubbish you produce in"
                                 f" a {waste_time} in {g_or_kg}: ")
    if g_or_kg == "g":
        amount_waste = amount_waste / 1000
    else:
        pass

    if waste_time == "Week":
        waste_calc_week(amount_waste)
    elif waste_time == "Year":
        waste_calc_year(amount_waste)
    else:
        pass

    sub_loader("Results")
    display_info(g_or_kg, waste_time, store_info, amount_waste)
    redo_home = check_redo_or_home("""Enter Redo['R'] to redo or Home['H'] to return to home
        : """)
    if redo_home == "redo":
        waste_calc()
    elif redo_home == "home":
        home()
    else:
        print("Please enter valid option")


# this dictionary will store info about the users production of waste/rubbish
store_info = {"more_less": "", "percentage": int(), "amount_kg": int()}

waste_calc()
