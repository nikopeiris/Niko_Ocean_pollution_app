import time

# this code display a "loading..." to make the user wait just like a normal app
def main_loader(section):
    i = 1
    i2 = 1
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
        time.sleep(0.25)
        print(".", end="")
        i2 += 1
    print("\n" * 9)


def sub_loader(section):
    i = 1
    i2 = 1
    i3 = 1
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
        time.sleep(0.25)
        print(".", end="")
        i3 += 1
    print("\n" * 7)
