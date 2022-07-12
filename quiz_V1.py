import time


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
    print("\n"*3)


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


quiz()
