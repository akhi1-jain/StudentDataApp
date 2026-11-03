# 1. Hello World (The absolute basics)
print("Wake up boi, we have a city to burn.")

# 2. Variables and User Input
user_name = input("What is your name? ")
print(f"Hello, {user_name}! I'm Python, can we be friends?.")

# 3. Simple Calculator (Basic Math & Conditionals)
num1 = float(input("Enter first number: "))
operator = input("Enter an operator (+, -, *, /): ")
num2 = float(input("Enter second number: "))

if operator == "+":
    result = num1 + num2
elif operator == "-":
    result = num1 - num2
elif operator == "*":
    result = num1 * num2
elif operator == "/":
    if num2 != 0:
        result = num1 / num2
    else:
        result = "Error! Division by zero."
else:
    result = "Invalid operator!"

print(f"Result: {result}")

# 4. Loops (Printing a multiplication table)
table_number = int(input("Enter a number for a multiplication table: "))
for i in range(1, 11):
    print(f"{table_number} x {i} = {table_number * i}")

# 5. Functions (Reusable Code)
def is_even(number):
    """Returns True if a number is even, False otherwise."""
    return number % 2 == 0

test_num = int(input("Enter a number to check if it's even or odd: "))
if is_even(test_num):
    print(f"{test_num} is an Even number.")
else:
    print(f"{test_num} is an Odd number.")