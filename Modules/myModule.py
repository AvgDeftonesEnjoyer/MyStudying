def factorial(num):
    if num < 0:
        return print(f"Factorial cant be  a negative number!")
    elif num == 0:
        return print(f"Factorial for {num} is 1")
    
    result = 1
    for i in range(1, num + 1):
        result *= i
    return print(f"The factorial for {num} is {result}")