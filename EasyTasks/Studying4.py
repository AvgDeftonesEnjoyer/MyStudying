def total(a,b):
    return print(f"sum of {a} and {b} is {a + b}")
def reversed_text(text):
    return print(f"Reversed text is '{text[::-1]}'")
def simple_num(a):
    if a % a == 0 and a % 1 == 0 and a % 2 != 0 and a % 3 != 0:
        return print(f"{a} is a simple number")
    else :
        return print(f"{a} is not a simple number")
def factorial(a):
    import math
    return print(f"Factorial of {a} is {math.factorial(a)}")



check = int(input("Choose homework: 1, 2, 3, 4: "))

if check == 1 :
    a = int(input("Enter the value of a: "))
    b = int(input("Enter the value of b: "))
    total(a, b)

elif check == 2 :
    text = input("Enter the text: ")
    reversed_text(text)

elif check == 3 :
    a = int(input("enter the value of a: "))
    simple_num(a)

elif check == 4:
    a = int(input("Enter the value of a: "))
    factorial(a)