name = input("What's the name of the cafe?\n").upper()
bill = float(input("What's the total bill?\n$"))
tip_percentage = float(input("What percentage would you like to tip? (10, 12 or 15)\n%"))
if tip_percentage == 10 or tip_percentage == 12 or tip_percentage == 15:
    person = int(input("Between how many people will you split the bill?\n"))
    if person >= 1:
        tip = bill * tip_percentage / 100
        total = bill + tip
        per_person = total / person

        print(f"\n{name}\n{'=' * len(name)}")
        print(f"Bill: ${bill:.2f}\nTip: ${tip:.2f}\nThe total price is: ${total:.2f}\nEach person should pay ${per_person:.2f}\n ")
    else:
        print("You cannot enter a value less than 1.")
        print("Restart the application please.")
else:
    print("Please select the tip percentage from the values shown (10, 12, 15).")
    print("Restart the application please.")
