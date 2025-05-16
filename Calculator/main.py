# Create input variable
# Create a function that takes the input variable as an argument

first = int(input("Write your first number: "))
operator = str(input("Write an arithmetic sign: "))
second = int(input("Write your second number: "))

def calculator(one, second, third):
    if second == "*":
        print(one * third)
    elif second == "+":
        print(one + third)
    elif second == "-":
        print(one - third)
    elif second == "/":
        print(one / third)

calculator(first, operator, second)
