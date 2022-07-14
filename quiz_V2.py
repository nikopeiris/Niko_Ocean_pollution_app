import time
import random
import quiz_question__answer_V1


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
            else:
                print("Please input a valid option")
        except TypeError:
            print("Please input a valid option")


# this gives a loading bar to the app
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
    print("\n" * 9)


# checks if the users input is a digit, if not print error message
def num_validator_quiz(num):
    while True:
        try:
            num_value = float(input(num))
            if 0 < num_value < 10:
                return num_value
            else:
                print("Enter a number between 1-9")
        except ValueError:
            print("Please choose a valid number")


def answer_validator(answer):
    while True:
        try:
            num_value = int(input(answer))
            if 0 < num_value < 4:
                return num_value
            else:
                print("Enter the corresponding number to the answer")
        except ValueError:
            print("Please choose a valid number")


def quiz():
    score = 0
    main_loader("Quiz")
    num_of_question = num_validator_quiz("How many question would you like to try(Max=9)\n"
                                         ": ")
    question_list = random.sample(range(0, 9), int(num_of_question))
    print(question_list)
    question_number = 0
    for i in question_list:
        question_number += 1
        print(quiz_question__answer_V1.questions_and_answers[i][0]
              .format(question_number))
        user_answer = answer_validator(":")
        if user_answer == quiz_question__answer_V1.questions_and_answers[i][1]:
            print("Correct!\n ***", quiz_question__answer_V1.questions_and_answers[i][2],
                  "***")
            score += 1
        else:
            print("Incorrect!\n ***", quiz_question__answer_V1.questions_and_answers[i][2],
                  "***")
        print("___________________________________________________________________________________________________")
        time.sleep(0.8)
    print("""                               *** Results ***""")
    print(f"Correct:{score}\nIncorrect:{len(question_list) - score}")
    time.sleep(0.25)
    print("You got", score, "out of", len(question_list), "\nThat is", round(float(score / len(question_list)) * 100),
          "% Correct")
    if round(score / len(question_list)) * 100 >= 50:
        print(random.choice(print_lines[0:4]))
    else:
        print(random.choice(print_lines[4:6]))
    time.sleep(1.5)
    print("________________________________________________________________________________________________________")
    redo_home = check_redo_or_home("""Enter Redo['R'] to redo or Home['H'] to return to home
        : """)
    if redo_home == "redo":
        quiz()
    elif redo_home == "home":
        home()
    else:
        print("Please enter valid option")


print_lines = ["Great Job!", "Nice Job!", "Amazing!", "You're a Genius!", "Better luck next time!", "Nice Try!",
               "You're doing great!", "Good Job!", "You can do better!", "Not so good!"]


quiz()
