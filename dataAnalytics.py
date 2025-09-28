'''print(12345)'''
'''print("sahil")'''

'''a = 10
b = 5

sum = a + b
print(f"The sum of {a} and {b} is: {sum}")

difference = a - b
print(f"The difference between {a} and {b} is: {difference}")

product = a * b
print(f"The product of {a} and {b} is: {product}")

quotient = a / b
print(f"The quotient of {a} and {b} is: {quotient}")'''

'''name=input("enter your name:-")'''

'''name=input("Please enter your name:")
age=int(input("Please enter your age:"))
city=input("Please enter your city:")'''

'''a=int(input("enter no1:-"))
b=int(input("enter no2:-"))

print(a+b)'''

try:
    age = int(input("Please enter your age: "))
except ValueError:
    print("Invalid input. Please enter a valid number for your age.")
else:
    if age >= 18:
        print("You are an adult and are allowed to vote.")
    elif age < 18:
        print("You are not yet 18 and are not allowed to vote.")


