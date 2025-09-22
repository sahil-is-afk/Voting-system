try:
    age = int(input("Please enter your age: "))
except ValueError:
    print("Invalid input. Please enter a valid number for your age.")
else:
    if age >= 18:
        print("You are an adult and are allowed to vote.")
    elif age < 18:
        print("You are not yet 18 and are not allowed to vote.")

