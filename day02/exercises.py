# a) Is the number odd or even
number = int(input("Enter a number to check whether it's an odd or an even number.\n"))

if number % 2 == 0:
    print(f"{number} is an even number.")
else:
    print(f"{number} is an odd number.")


# b) Is the year a leap year
year = int(input("Enter a year to check whether it's a leap year or not.\n"))

if year % 4 == 0:
    if year % 400 == 0 or year % 100 != 0:
        print(f"{year} is a leap year.")
    else:
        print(f"{year} is not a leap year.")
else:
    print(f"{year} is not a leap year.")

# c) Convert note to letter
note = int(input("Enter your note to convert to a letter.\n"))
if note > 100:
    print("Note can't be bigger than 100")
elif note >= 90:
    print("A")
elif note >= 80:
    print("B")
elif note >= 70:
    print("C")
elif note >= 60:
    print("D")
elif note < 0:
    print("Note can't be lower than 0")
else:
    print("F")