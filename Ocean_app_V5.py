import time
import solutions_dict_V2
import random
import quiz_question__answer_V1
import displayed_info_V1


# this def exits the code
def exit_app():
    print("|Exiting...")
    time.sleep(1)
    print(f"|Thank You, {name} for using the Ocean Care app")
    print("_________________________________________________________________")
    time.sleep(1)
    exit()


# this code display a "loading..." to make the user wait just like a normal app
def main_loader(section):
    i = 1
    i2 = 1
    print("_________________________________________________________________")
    print(f"| Loading {section}", end="")
    while i <= 4:
        time.sleep(0.25)
        print(".", end="")
        i += 1
    print("")
    time.sleep(0.15)
    print("| Loading Complete...")
    print(f"| Displaying {section}", end="")
    while i2 <= 4:
        time.sleep(0.1)
        print(".", end="")
        i2 += 1
    print("\n" * 9)
    print("_________________________________________________________________")


def sub_loader(section):
    i = 1
    i2 = 1
    i3 = 1
    print("_________________________________________________________________")
    print(f"| Calculating {section}", end="")
    while i <= 4:
        time.sleep(0.25)
        print(".", end="")
        i += 1
    print("")
    time.sleep(0.15)
    print("| Finalising Calculations", end="")
    while i2 <= 4:
        time.sleep(0.25)
        print(".", end="")
        i2 += 1
    print("")
    time.sleep(0.15)
    print(f"| Displaying {section}", end="")
    while i3 <= 4:
        time.sleep(0.1)
        print(".", end="")
        i3 += 1
    print("\n" * 7)
    print("_________________________________________________________________")


# checks if the users input is a digit, if not print error message
def num_validator(num):
    while True:
        try:
            num_value = int(input(num))
            if 0 < num_value < 5:
                return num_value
            else:
                print("|Please choose a valid number")
        except ValueError:
            print("|Please choose a valid number")


# this checks if the users input is a string, if not print error message
def string_validator(prompt):
    while True:
        try:
            string = input(prompt).strip().lower()
            if string.isalpha():
                return string.title()
            else:
                print("|Please choose a valid input")
        except TypeError:
            print("|Please choose a valid choice")


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
                exit_app()
                break
            else:
                print("|Please input a valid option")
        except TypeError:
            print("|Please input a valid option")


# this is the home part of the program(includes all the program features)
def home():
    main_loader("Home")
    print(""" *** Choose activity number ***
|1. Waste calculator
|2. Solutions
|3. Quiz
|4. Instructions""")
    acti_input = num_validator(""": """)
    if acti_input == 1:
        waste_calc()
    elif acti_input == 2:
        solutions()
    elif acti_input == 3:
        quiz()
    elif acti_input == 4:
        instruction()
    else:
        print("|Thanks for using the program")


# waste calculator user defined functions
# this checks if the users input is a string, if not print error message
def week_year(question):
    while True:
        try:
            string = input(question).strip().lower()
            if string == "w" or string == "weekly":
                return "Week"
            elif string == "y" or string == "yearly":
                return "Year"
            elif string == "h" or string == "home":
                home()
            else:
                print("|Please enter valid option")
        except TypeError:
            print("|Please choose a valid option")


# checks if the users input is a digit, if not print error message
def num_validator_waste_calc(num):
    while True:
        try:
            num_value = float(input(num))
            if "-" in str(num_value):
                print("|Please choose a valid number")
            else:
                return num_value
        except ValueError:
            print("|Please choose a valid number")


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
                print("|Please choose a valid option")
        except TypeError:
            print("|Please choose a valid option")


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
        print("|Enter valid number!")


# this is where the results are printed from
def display_info(g_or_kg, waste_time, info, amount_waste):
    amount_g = info["amount_kg"] * 1000
    print("""                  *** Results ***""")
    if g_or_kg == "g":
        if amount_waste == 62 or amount_waste == 3200:
            print(random.choice(print_lines[6:8]))
            print(displayed_info_V1.displayed_info[0])
        else:
            print(displayed_info_V1.displayed_info[1].
                  format(amount_g, store_info["more_less"],
                         waste_time, store_info["percentage"]))
    elif g_or_kg == "kg":
        if amount_waste == 62 or amount_waste == 3200:
            print(displayed_info_V1.displayed_info[0])
        else:
            print(displayed_info_V1.displayed_info[2].
                  format(store_info["amount_kg"],
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
        print("|Enter valid number!")


# user defined function for calculating garbage
def waste_calc():
    main_loader("Waste Calculator")
    print("""            *** Waste Calculator ***""")
    waste_time = week_year("|Do you want calculate Weekly['W'] or Yearly"
                           "['Y']:")
    g_or_kg = g_kg("|Would you like to calculate in grams[g] or kilograms"
                   "[kg]:")
    amount_waste = num_validator_waste_calc("|Please enter the approximate "
                                            "amount of waste/rubbish you "
                                            "produce in"
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
    if store_info["more_less"] == "More":
        print(random.choice(print_lines[8:10]),
              "\n|You can try some of our Solutions from Home section")
    elif store_info["more_less"] == "Less":
        print(random.choice(print_lines[6:8]))
    else:
        print("", end="")
    redo_home = check_redo_or_home("""|Enter Redo['R'] or return Home['H']
: """)
    if redo_home == "redo":
        waste_calc()
    elif redo_home == "home":
        home()
    else:
        print("|Please enter valid option")


# solutions user defined functions
# displays solutions
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
    print("|Enter Solutions[S] to see list of solutions")
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
                print("_____________________________________________________")
                print(solutions_dict_V2.solution_dict[choice])
            else:
                print("|Enter valid option")
        except KeyError:
            print("|Enter valid option")


# quiz user defined functions
# checks if the users input is a digit, if not print error message
def num_validator_quiz(num):
    while True:
        try:
            num_value = float(input(num))
            if 0 < num_value < 10:
                return num_value
            else:
                print("|Enter a number between 1-9")
        except ValueError:
            print("|Please choose a valid number")


# checks if the users answer input is between 1-3
def answer_validator(answer):
    while True:
        try:
            num_value = int(input(answer))
            if 0 < num_value < 4:
                return num_value
            else:
                print("|Enter the corresponding number to the answer")
        except ValueError:
            print("|Please choose a valid number")


# main quiz program, randomizes questions
def quiz():
    score = 0
    main_loader("Quiz")
    num_of_question = num_validator_quiz("|How many question would you like to"
                                         " try(Max=9): ")
    question_list = random.sample(range(0, 9), int(num_of_question))
    question_number = 0
    main_loader("Questions")
    for i in question_list:
        question_number += 1
        print(quiz_question__answer_V1.questions_and_answers[i][0]
              .format(question_number))
        user_answer = answer_validator(":")
        if user_answer == quiz_question__answer_V1.questions_and_answers[i][1]:
            print("|Correct!\n ***",
                  quiz_question__answer_V1.questions_and_answers[i][2],
                  "***")
            score += 1
        else:
            print("|Incorrect!\n ***",
                  quiz_question__answer_V1.questions_and_answers[i][2],
                  "***")
        print(f"|Current score: {score}/{question_number}")
        print("_________________________________________________________________")
        time.sleep(1)
    print("""                               *** Results ***""")
    print(f"|Correct:{score}\n|Incorrect:{len(question_list) - score}")
    time.sleep(0.25)
    print("|You got", score, "out of", len(question_list),
          "\n|That is", round(float(score / len(question_list)) * 100),
          "% Correct")
    if round(score / len(question_list)) * 100 >= 50:
        print(random.choice(print_lines[0:4]))
    else:
        print(random.choice(print_lines[4:6]))
    time.sleep(1.5)
    print("_________________________________________________________________")
    redo_home = check_redo_or_home("""|Enter Redo['R'] or return Home['H']
        : """)
    if redo_home == "redo":
        quiz()
    elif redo_home == "home":
        home()
    else:
        print("|Please enter valid option")


# instruction user defined function
def instruction():
    main_loader("Instructions")
    print("""                               **INSTRUCTIONS**
    |Welcome to the Ocean Pollution app. This app consists of few things.
    |1. Waste calculator:
            Where you calculate the amount of waste you create compared to the average person,
            and how to reduce it.
    |2. Solutions:
            List of solutions you can perform to reduce waste.
    |3. Quiz:
            Quiz about Ocean pollution and Ocean issues.
    |4. Instructions:
            Just in case you wanted to see the instructions again

    **If you want to go back to Home section, Type Home[H]**
    **If you are presented with options to choose from,
      Enter the corresponding number to the option**
    **If you want to quit the program type, quit[q]**""")
    redo_home = check_redo_or_home(""" |Enter Home['H'] to return to home: """)
    if redo_home == "redo":
        instruction()
    elif redo_home == "home":
        home()
    else:
        print("|Please enter valid option")


# start of the app
# this dictionary will store info about the users production of waste/rubbish
store_info = {"more_less": "", "percentage": int(), "amount_kg": int()}
# this list will store multiple strings
print_lines = ["|Great Job!", "|Nice Job!", "|Amazing!", "|You're a Genius!",
               "|Better luck next time!", "|Nice Try!", "|You're doing great!",
               "|Good Job!", "|You can do better!", "|Not so good!"]

main_loader("Ocean Care app")


name = string_validator("|What is your name: ")
print("""** Welcome {} to Ocean Care app **""".format(name))
time.sleep(0.5)
while True:
    show_instruction = string_validator("|Would you like to see the "
                                        "Instructions\nYes[Y] or No[N]:")
    if show_instruction == "Yes" or show_instruction == "Y":
        instruction()
    elif show_instruction == "No" or show_instruction == "N":
        home()
    else:
        print("|Please enter a valid option")
