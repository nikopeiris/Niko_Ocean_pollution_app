import time
import solutions_dict_V2


def exit_app():
    print(f"Thank You, {name.title()} for using the Ocean Care app")
    print("____________________________________________________")
    time.sleep(1)
    exit()


def instruction():
    main_loader("Instructions")
    print("""                               **INSTRUCTIONS**
    Welcome to the Ocean Pollution app. This app consists of few things.
    1. Waste calculator:
            Where you calculate the amount of waste you create compared to the average person,
            and how to reduce it.
    2. Solutions:
            List of solutions you can perform to reduce waste.
    3. Instructions:
            Just in case you wanted to see Instruction again.

    **If you want to go back to Home section, Type Home[H]**
    If you are presented with options to choose from, Enter the corresponding number to the option
    If you want to quit the program type, quit[q]""")
    redo_home = check_redo_or_home(""" Enter Home['H'] to return to home
            : """)
    if redo_home == "redo":
        pass
    elif redo_home == "home":
        home()
    elif redo_home == "quit":
        exit_app()
    else:
        print("Please enter valid option")


# checks if the users input is a digit, if not print error message
def num_validator(num):
    while True:
        try:
            num_value = int(input(num))
            if 0 < num_value < 4:
                return num_value
            else:
                print("Please choose a valid number")
        except ValueError:
            print("Please choose a valid number")


# this checks if the users input is a string, if not print error message
def string_validator(prompt):
    while True:
        try:
            string = input(prompt).strip().lower()
            if string.isalpha():
                return string
            else:
                print("Please choose a valid choice")
        except TypeError:
            print("Please choose a valid choice")


# this is the home part of the program(includes all the program features)
def home():
    main_loader("Home")
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
def num_validator_waste_calc(num):
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
    print(f"| Loading {section}", end="")
    while i <= 4:
        time.sleep(0.5)
        print(".", end="")
        i += 1
    print("")
    time.sleep(0.2)
    print("| Loading Complete...")
    print(f"| Displaying {section}", end="")
    while i2 <= 4:
        time.sleep(0.25)
        print(".", end="")
        i2 += 1
    print("\n" * 3)


def sub_loader(section):
    i = 1
    i2 = 1
    i3 = 1
    print(f"| Calculating {section}", end="")
    while i <= 4:
        time.sleep(0.5)
        print(".", end="")
        i += 1
    print("")
    time.sleep(0.2)
    print("| Finalising Calculations", end="")
    while i2 <= 4:
        time.sleep(0.5)
        print(".", end="")
        i2 += 1
    print("")
    time.sleep(0.2)
    print(f"| Displaying {section}", end="")
    while i3 <= 4:
        time.sleep(0.25)
        print(".", end="")
        i3 += 1
    print("\n" * 2)


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
Which is 62000g a Week and 3200000g a Year!""")
        else:
            print("""An average New Zealander produces around 62000g garbage a Week, and
3200000g garbage a Year.
You produce {0}g {1} garbage in a {2} compared to an average New Zealander!
Which is {3}% {1} garbage!""".format(amount_g, store_info["more_less"],
                                     waste_time, store_info["percentage"]))
    elif g_or_kg == "kg":
        if amount_waste == 62 or amount_waste == 3200:
            print("""You produce the exact amount of garbage produced by an average New Zealander,
Which is 62kg a Week and 3200kg a Year!""")
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


# where the user finds his waste amount
def waste_calc():
    main_loader("Waste Calculator")
    print("""            *** Waste Calculator ***""")
    waste_time = week_year("Do you want calculate Weekly['W'] or Yearly['Y']:")
    g_or_kg = g_kg("Would you like to calculate in grams[g] or kilograms[kg]:")
    amount_waste = num_validator_waste_calc("Please enter the approximate amount of waste/rubbish you produce in"
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


def solutions():
    solution_list = """                        *****************
 _______________________*** Solutions ***_____________________________
|**Enter corresponding number to learn more or Home[H] to visit Home**|
|1. Use a reusable bottle/cup                                         |
|2. Recycle                                                           |
|3. Avoid single-use food and drink containers and utensils           |
|4. Buy things in bulk with less packaging                            |
|5. Bring your own bag                                                |
|6. Composting                                                        |
|7. Buy rechargeable batteries                                        |
|8. Get Involved                                                      |
 ---------------------------------------------------------------------  """
    main_loader("Solutions")
    print(solution_list)
    print("Enter Solutions[S] to see list of solutions")
    while True:
        try:
            choice = input(": ").lower()
            if choice == "home" or choice == "h":
                home()
                break
            elif choice == "quit" or choice == "q":
                exit_app()
            elif choice == "solutions" or choice == "s":
                print(solution_list)
            elif "0" < choice < "9":
                time.sleep(1)
                print(solutions_dict_V2.solution_dict[choice])
            else:
                print("Enter valid option")
        except KeyError:
            print("Enter valid option")


questions = ["1. where does most ocean pollution come from?",
             "2. elevated water temperature can cause corals to do what?",
             "3. industrial fishing is thought to have wiped out what percentage of large, predatory fish?",
             "4. what area of the ocean is suffering most from habitat destruction?",
             "5. in the summer of 2014, researchers recorded the highest global mean sea-surface temperatures "
             "in history. where was the warming anomaly concentrated?",
             "6. what is the rate of sea-level rise over the past century?",
             "7. where is the world's largest marine protected area?",
             "8. which fishery is not depleted?",
             "9. what animals are most at risk from ocean acidification?"]

answer_choices = [""" 1. marine activities.\n 2. land activities.\n 3. both, it is fairly evenly divided.""",
                  """ 1. grow too quickly.\n 2. bleach.\n 3. eat themselves.""",
                  """ 1. 25%.\n 2. 55%.\n 3. 66%.""",
                  """ 1. seafloor.\n 2. deep sea\n 3. coasts.""",
                  """ 1. south pacific\n 2. north pacific\n 3. indian.""",
                  " 1. 0.01 to 0.04 inch per year,(0.254 mm to 1.016 mm per year)\n 2. 0.04 to 0.1 inch per year,"
                  "(1.016 mm to 2.54 mm per year)\n 3. 0.1 to 0.12 inch per year,(2.54 mm to 3.048 mm per year)",
                  """ 1. coral sea\n 2. pitcairn islands\n 3. hawaiian islands""",
                  """ 1. atlantic cod\n 2. south pacific bluefin tuna\n 3. atlantic herring""",
                  """ 1. shellfish\n 2. marine mammals\n 3. bottom-feeding fish"""]

correct_choices = [["land activities", "2"],
                   ["bleach", "2"],
                   ["66%", "66", "3"],
                   ["coasts", "3"],
                   ["north pacific", "2", "north"],
                   ["0.04 to 0.1 inch per year", "1.016 mm to 2.54 mm per year", "2", ],
                   ["coral sea", "1"],
                   ["atlantic herring", "3"],
                   ["shellfish", "1"]]

answers = ["""More than 80% of all ocean pollution comes from land. 
oil from cities and factories washes down drains and into the ocean.""",
           """Elevated temperatures trigger mass episodes bleaching""",
           """In the 20th century, humans reduced the biomass of predatory fish by more than two-thirds""",
           """Coastal areas, with their closeness to human population centers have suffered disproportionately""",
           """The 2014 global ocean warming was mostly due to the north pacific""",
           """Records and research show tha sea level has been steadily rising at a rate of about, 
0.04 to 0.1 inches per year(1.016 mm to 2.54 mm per year) since 1900.""",
           """The natural park of the coral sea protects 1.3 million square kilometers
(501,930 square miles) of marine ecosystems""",
           """Atlantic herring fish stocks range from underexploited to recovering. 
Atlantic cod and pacific bluefin tuna fisheries are both depleted""",
           """Ocean acidity has already increased more than 30% from pre-industrial levels"""]

possible_answers = [["land activities", "marine activities", "both, it is fairly evenly divided", "2", "1", "3", ],
                       ["bleach", "grow too quickly", "eat themselves", "2", "1", "3"],
                       ["66%", "66", "25%", "25", "55%", "55", "1", "2", "3"],
                       ["coasts", "seafloor", "deep sea", "3", "2", "1"],
                       ["north pacific", "2", "north", "3", "1", "south pacific", "indian"],
                       ["0.04 to 0.1 inch per year", "1.016 mm to 2.54 mm per year", "2", "3", "1",
                        "0.1 to 0.12 inch per year", "2.54 mm to 3.048 mm per year", "0.01 to 0.04 inch per year",
                        "0.254 mm to 1.016 mm per year"],
                       ["coral sea", "1", "2", "3", "pitcairn islands", "hawaiian islands"],
                       ["atlantic herring", "3", "2", "1", "atlantic cod", "south pacific bluefin tuna"],
                       ["shellfish", "1", "2", "3", "marine mammals", "bottom-feeding fish"]]

def quiz():
    score = 0
    main_loader("Quiz")
    for question, choices, correct_choice, answer, possible_answer in zip(questions, answer_choices, correct_choices,
                                                                          answers, possible_answers):
        print(question)
        print(choices)
        user_answer = input(":").lower()
        if user_answer in correct_choice:
            print("Correct\n", answer, "\n")
            score += 1
        else:
            print("Incorrect\n", answer, "\n")
    print(score, "out of", len(questions), "that is", round(float(score / len(questions)) * 100), "%")


# start of the main program
# this dictionary will store info about the users production of waste/rubbish
store_info = {"more_less": "", "percentage": int(), "amount_kg": int()}

main_loader("Ocean Care app")

while True:
    name = string_validator("What is your name: ")
    if name.isalpha():
        print("""**Welcome {} to Ocean Care app**""".format(name.title()))
        home()
    else:
        pass
