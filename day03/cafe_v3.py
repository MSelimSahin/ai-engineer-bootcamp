should_break = False

while not should_break:
    name = input("What's the name of the cafe?\n").upper()
    bill = float(input("What's the total bill?\n$"))
    tip_percentage = float(input("What percentage would you like to tip? (10, 12 or 15)\n%"))
    while tip_percentage != 10 and tip_percentage != 12 and tip_percentage != 15:
        tip_percentage = float(input("What percentage would you like to tip? (10, 12 or 15)\n%"))
    person = int(input("Between how many people will you split the bill?\n"))
    while person < 1:
        person = int(input("Between how many people will you split the bill?\n"))
    tip = bill * tip_percentage / 100
    total = bill + tip
    per_person = total / person

    print(f"\n{name}\n{'=' * len(name)}")
    print(f"Bill: ${bill:.2f}\nTip: ${tip:.2f}\nThe total price is: ${total:.2f}\nEach person should pay ${per_person:.2f}\n ")

    question = input("Do you want to make another calculation? (y, n)").lower()
    while question != "n" and question != "y":
        print("Did you do a typo?")
        question = input("Do you want to make another calculation? (y, n)").lower()
    if question == "y":
        continue
    elif question == "n":
        should_break = True

