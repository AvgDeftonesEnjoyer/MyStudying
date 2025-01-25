check = int(input("Choose homework 1, 2, 3: "))
if check == 1 :
    
    """1. Создайте программу, которая запрашивает у пользователя его имя, возраст и город, а затем выводит сообщение:
    Привет, <имя>! Тебе <возраст> лет, и ты живешь в <город>."""

    name = input("Enter your name: ")
    age = input("Enter your age: ")
    city = input("Enter your city: ")
    print(f"Your name is {name}. You are {age} years old, you live in {city} city ")

elif check == 2:
    """2. Напишите программу, которая принимает от пользователя два числа, умножает их и выводит результат."""

    a = int(input("Enter the value of a: "))
    b = int(input("Enter the value of b: "))
    print(f"Sum of a * b is {a * b}")

elif check == 3:
    """Создайте программу, которая рассчитывает площадь круга. Пользователь вводит радиус, а программа выводит площадь"""
    import math
    r = int(input("Enter the value of radius: "))
    print(f"if r = {r} - square of circle = {round(math.pi * (r**2), 3)}")