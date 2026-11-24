def ask_number(prompt, low, high):
    while True:
        try:
            number = int(input(prompt))
        except ValueError:
            print("The number should be an integer.")
        else:
            if low <= number <= high:
                return number
            else:
                print(f"The number should be between {low} and {high}")

if __name__ == "__main__":
    age = ask_number("Age: ", 0, 120)
    print(f"Your age: {age}")