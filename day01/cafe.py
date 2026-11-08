name = input("What's the name of the cafe?\n").upper()
bill = float(input("What's the total bill?\n$"))
tip_percentage = float(input("What percentage would you like to tip? (10, 12 or 15)\n%"))
person = int(input("Between how many people will you split the bill?\n"))
tip = bill * tip_percentage / 100
total = bill + tip
per_person = total / person

print(f"\n{name}\n{'=' * len(name)}")
print(f"The total price is: ${total:.2f}\nEach person should pay ${per_person:.2f}")