# Voting-system


# Age Validation Program 🧑‍💻

This is a simple Python program that asks the user to input their age and determines whether they are eligible to vote.  
It includes **error handling** to make sure the input is a valid number.

---

## 📋 Features
- Takes user input for age.
- Handles invalid input (non-numeric values).
- Checks if the user is **18 or older** to determine voting eligibility.
- Provides clear messages based on the input.

---

## 💻 Code Example

```python
try:
    age = int(input("Please enter your age: "))
except ValueError:
    print("Invalid input. Please enter a valid number for your age.")
else:
    if age >= 18:
        print("You are an adult and are allowed to vote.")
    elif age < 18:
        print("You are not yet 18 and are not allowed to vote.")

## Author
Sahil
LinkedIn-https://www.linkedin.com/in/sahiljha10/
