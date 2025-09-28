a = float(input("Enter first number: "))
b = float(input("Enter second number: "))

print("\nChoose the operation you want to perform:")
print("+. Addition")
print("-. Subtraction")
print("*. Multiplication")
print("/. Division")

choice = int(input("\nEnter your choice (1/2/3/4): "))

if choice == 1:

    
    print(a + b)
elif choice == 2:
    print(a - c)
elif choice == 3:
    print(a * b)
elif choice == 4:
    print(a / b)
    
else:
    print("Invalid choice!")

