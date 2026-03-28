# Practice 1
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

sum_result = num1 + num2
difference = num1 - num2
product = num1 * num2

if num2 != 0:
    division = num1 / num2
else:
    division = "Cannot divide by zero"

print("Sum:", sum_result)
print("Difference:", difference)
print("Product:", product)
print("Division:", division)


# Practice 2
num = int(input("Enter a number: "))

if num > 0:
    print("This Number is Positive")
elif num < 0:
    print("This Number is Negative")
else:
    print("Zero")


# Practice 3
age = int(input("Enter age: "))

if age >= 18:
    print("Adult")
else:
    print("Minor")


# Practice 4
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

if num1 > num2:
    print("First number is larger")
elif num2 > num1:
    print("Second number is larger")
else:
    print("Both numbers are equal")


# Practice 5
num = int(input("Marks: "))

if num >= 90:
    print("Grade is A")
elif num >= 86:
    print("Grade is B")
elif num >= 74:
    print("Grade is C")
else:
    print("Fail")
