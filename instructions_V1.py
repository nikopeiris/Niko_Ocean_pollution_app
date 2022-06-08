def instruction():
    print("""                               **INSTRUCTIONS** 
    Welcome {} to the Ocean Pollution app. This app consists of few things.
    1. Waste calculator:
            Where you calculate the amount of waste you create compared to the average person,
            and how to reduce it.
    2. Quiz:
            Where you can test your knowledge about Ocean Pollution.
    3. Solutions:
            List of solutions you can perform to reduce waste.
    4. Instructions:
            Just in case you wanted to see Instruction again.  
            
    **If you want to go back to Home section, Type "Home"**
    If you are presented with options to choose from, Enter the corresponding number to the option""".format(name))


name = input("What is your name: ").title()

instruction()
