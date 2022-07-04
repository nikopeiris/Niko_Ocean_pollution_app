import time
import solutions_dict_V2


def exit_app():
    print(f"Thank You, {name} for using the Ocean Care app")
    print("________________________________________")
    time.sleep(1)
    exit()

# this code display a "loading..." to make the user wait just like a normal app
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
    print("\n"*3)
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
                print(solutions_dict_V2.solution_dict[choice])
            else:
                print("Enter valid option")
        except KeyError:
            print("Enter valid option")


solutions()
